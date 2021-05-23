import apply_lints_and_build_docs
from apply_lints_and_build_docs import LintCommand


def test__run_lint_command() -> None:
    lint_command: LintCommand = {
        'command': 'ls -l',
        'lint_name': 'test',
    }
    stdout: str = apply_lints_and_build_docs._run_lint_command(
        lint_command=lint_command)
    assert 'apysc' in stdout
