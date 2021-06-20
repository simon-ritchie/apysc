from random import randint

from retrying import retry

from apysc import Stage
from apysc import trace
from apysc._expression import expression_file_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_trace() -> None:
    stage: Stage = Stage()
    trace(stage, 100, 'Hello!')
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'console.log({stage.variable_name}, "100", "Hello!");'
    )
    assert expected in expression
