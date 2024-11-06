import os
import subprocess
import sys

from cligenius.testing import CliRunner

from docs_src.options_autocompletion import tutorial007_an as mod

runner = CliRunner()


def test_completion():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        capture_output=True,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL007_AN.PY_COMPLETE": "complete_zsh",
            "_CLIGENIUS_COMPLETE_ARGS": "tutorial007_an.py --name Sulaiman --name ",
        },
    )
    assert '"Camila":"The reader of books."' in result.stdout
    assert '"Carlos":"The writer of scripts."' in result.stdout
    assert '"Sulaiman":"The type hints guy."' not in result.stdout


def test_1():
    result = runner.invoke(mod.app, ["--name", "Camila", "--name", "Sulaiman"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output
    assert "Hello Sulaiman" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        capture_output=True,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
