from setuptools import setup, find_packages

setup(
    name="tua",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tua = interpreter.main:cli_run_interpreter',
            'tuatest = interpreter.test.run_tests:run_tests'
        ],
    },
)
