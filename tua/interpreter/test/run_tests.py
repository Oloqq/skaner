import os
import sys
from io import StringIO
import yaml
from ..main import run_interpreter
from antlr4 import InputStream

def run_tests():
    print("Running tests...")

    failed = []
    current_file_path = os.path.realpath(__file__)
    dir = current_file_path.replace("/", "\\").rpartition("\\")[0]
    testcases = os.listdir(dir)

    for case in testcases:
        if case.endswith(".yaml"):
            print("Running test case: " + case)
            with open(dir + "\\" + case, "r") as f:
                test = yaml.safe_load(f)
                if test.get("skip", False):
                    continue
                program = test["program"]
                expected = test.get("output", "")

                # Create a StringIO object to capture the stdout
                stdout_capture = StringIO()

                # Redirect the stdout to the StringIO object
                sys.stdout = stdout_capture

                run_interpreter(InputStream(program), False)

                # Get the captured output
                output = stdout_capture.getvalue() or ""

                # Restore the original stdout
                sys.stdout = sys.__stdout__

                if not expected.endswith("\n"):
                    expected += "\n"

                is_failed = output != expected
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
                    failed.append(case)

    if len(failed) == 0:
        print("All tests passed!")
    else:
        print(f"Failed tests ({len(failed)}):")
        for case in failed:
            print(case)