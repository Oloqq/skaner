import os
import sys
from io import StringIO
import yaml
from ..main import run_interpreter_full_program
from antlr4 import InputStream
import click
from enum import Enum
from ..visitor import SemanticError

class TestResult(Enum):
    SUCCESS = 0
    FAILURE = 1
    SKIPPED = 2
    NOT_FOUND = 3

def run_test(dir: str, debug: bool, case: str, verbose: bool = False) -> TestResult:
    if not case.endswith(".yaml"):
        return TestResult.NOT_FOUND

    try:
        with open(dir + "\\" + case, "r") as f:
            test = yaml.safe_load(f)
    except FileNotFoundError as e:
        print(f"Test case not found: {case}")
        return TestResult.NOT_FOUND

    if test.get("skip", False):
        print("Skipping test case: " + case)
        return TestResult.SKIPPED

    print()
    print("Running test case: " + case)
    program = test["program"]
    expected = test.get("output", "")

    # Create a StringIO object to capture the stdout
    stdout_capture = StringIO()

    # Redirect the stdout to the StringIO object
    sys.stdout = stdout_capture

    error_output = ""
    try:
        run_interpreter_full_program(InputStream(program))
        threw = False
    except SemanticError as e:
        threw = True
        error_output = str(e)

    # Get the captured output
    output = stdout_capture.getvalue() or ""

    # Restore the original stdout
    sys.stdout = sys.__stdout__

    if not expected.endswith("\n"):
        expected += "\n"

    is_failed = threw or output != expected
    should_fail = test.get("fail", False)
    show_output = (threw and error_output) or verbose

    if is_failed and not should_fail:
        print(f"Test failed: {case}")
    elif not is_failed and should_fail:
        print(f"Test was expected to fail: {case}")
    elif show_output:
        print(f"Test case: {case}")

    if threw and error_output:
        print(output)
        print("Error output:", error_output)
        print()
        return TestResult.FAILURE
    elif is_failed != should_fail:
        print("Expected:")
        print(expected)
        print("Got:")
        print(output)
        print()
        return TestResult.FAILURE
    elif verbose:
        print("Output:")
        print(output)

    return TestResult.SUCCESS

def run_all_tests(dir: str, debug: bool, verbose: bool = False):
    print("Running all tests...")

    failed = []
    not_found = []
    skipped = []
    testcases = os.listdir(dir)

    for case in testcases:
        res = run_test(dir, debug, case, verbose)
        if res == TestResult.FAILURE:
            failed.append(case)
        elif res == TestResult.NOT_FOUND:
            not_found.append(case)
        elif res == TestResult.SKIPPED:
            skipped.append(case)

    if len(failed) == 0:
        print("All tests passed!")
        if len(skipped) > 0:
            print(f"Skipped tests ({len(skipped)}):")
            for case in skipped:
                print(case)
    else:
        print(f"Failed tests ({len(failed)}):")
        for case in failed:
            print(case)

@click.command()
@click.argument("testcase", nargs=-1)
@click.option("--debug", "-d", is_flag=True, help="Enable debug logging")
@click.option("--verbose", "-v", is_flag=True, help="Print output of successful tests")
def run_tests(testcase, debug, verbose):
    current_file_path = os.path.realpath(__file__)
    dir = current_file_path.replace("/", "\\").rpartition("\\")[0]
    if not testcase:
        run_all_tests(dir, debug, verbose)
    else:
        for t in testcase:
            if not t.endswith(".yaml"):
                t += ".yaml"
            run_test(dir, debug, t, verbose)
