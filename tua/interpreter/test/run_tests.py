import os
import sys
from io import StringIO
import yaml
from ..main import run_interpreter_full_program
from antlr4 import InputStream
import click
from enum import Enum
from ..visitor import SemanticError, InternalError

class TestResult(Enum):
    SUCCESS = 0
    FAILURE = 1
    SKIPPED = 2
    NOT_FOUND = 3

def execute(program) -> tuple[str, str]:
    # Create a StringIO object to capture the stdout
    stdout_capture = StringIO()

    # Redirect the stdout to the StringIO object
    sys.stdout = stdout_capture

    error_output = ""
    try:
        run_interpreter_full_program(InputStream(program))
    except (SemanticError, InternalError) as e:
        error_output = str(e)

    # Get the captured output
    output = stdout_capture.getvalue() or ""

    # Restore the original stdout
    sys.stdout = sys.__stdout__

    return output, error_output

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
    if not expected.endswith("\n"):
        expected += "\n"
    expected_error = test.get("error", "")

    output, error = execute(program)
    if not expected_error and output != expected:
        print("Test failed. Output of the program not as expected")
        print("Expected:")
        print(expected)
        print("Got:")
        print(output)
        print()
        return TestResult.FAILURE
    elif error != expected_error:
        print("Test failed. Error message not as expected")
        print("Expected:")
        print(expected_error)
        print("Got:")
        print(error)
        print()
        return TestResult.FAILURE
    elif verbose:
        print(output)
        if error:
            print(error)

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
