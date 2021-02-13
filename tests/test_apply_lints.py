import apply_lints
from apply_lints import LintCommand


def test__run_lint_command() -> None:
    lint_command: LintCommand = {
        'command': 'ls -l',
        'lint_name': 'test',
    }
    stdout: str = apply_lints._run_lint_command(lint_command=lint_command)
    assert 'apyscript' in stdout
