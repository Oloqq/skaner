import os
import sys
from io import StringIO
import yaml
from ..main import run_interpreter
from antlr4 import InputStream
import click

def run_test(dir: str, case: str) -> bool|None:
    if not case.endswith(".yaml"):
        return

    try:
        with open(dir + "\\" + case, "r") as f:
            test = yaml.safe_load(f)
    except FileNotFoundError as e:
        print(f"Test case not found: {case}")
        return

    if test.get("skip", False):
        print("Skipping test case: " + case)
        return

    print("Running test case: " + case)
    program = test["program"]
    expected = test.get("output", "")

    # Create a StringIO object to capture the stdout
    stdout_capture = StringIO()

    # Redirect the stdout to the StringIO object
    sys.stdout = stdout_capture

    try:
        run_interpreter(InputStream(program), False)
        threw = False
    except Exception as e:
        threw = True

    # Get the captured output
    output = stdout_capture.getvalue() or ""

    # Restore the original stdout
    sys.stdout = sys.__stdout__

    if not expected.endswith("\n"):
        expected += "\n"

    is_failed = threw or output != expected
    should_fail = test.get("fail", False)
    if is_failed != should_fail:
        if should_fail:
            print(f"Test was expected to fail: {case}")
        else:
            print(f"Test failed: {case}")
        print("Expected:")
        print(expected)
        print("Got:")
        print(output)
        return False
    return True

def run_all_tests(dir: str):
    print("Running all tests...")

    failed = []
    testcases = os.listdir(dir)

    for case in testcases:
        if run_test(dir, case) == False:
            failed.append(case)

    if len(failed) == 0:
        print("All tests passed!")
    else:
        print(f"Failed tests ({len(failed)}):")
        for case in failed:
            print(case)

@click.command()
@click.argument("testcase", nargs=-1)
def run_tests(testcase):
    current_file_path = os.path.realpath(__file__)
    dir = current_file_path.replace("/", "\\").rpartition("\\")[0]
    if not testcase:
        run_all_tests(dir)
    else:
        for t in testcase:
            if not t.endswith(".yaml"):
                t += ".yaml"
            run_test(dir, t)
