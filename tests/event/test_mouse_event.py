from random import randint

from retrying import retry

from apysc import MouseEvent, Int
from apysc.expression import var_names, expression_file_util
from apysc.display.stage import get_stage_element_id
from apysc import Stage


class TestMouseEvent:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        int_1: Int = Int(10)
        mouse_event: MouseEvent[Int] = MouseEvent(this=int_1)
        assert mouse_event.this == int_1
        assert mouse_event.variable_name.startswith(
            f'{var_names.MOUSE_EVENT}_')

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_stage_x(self) -> None:
        int_1: Int = Int(10)
        mouse_event: MouseEvent[Int] = MouseEvent(this=int_1)
        stage_x: Int = mouse_event.stage_x
        assert isinstance(stage_x, Int)
        assert stage_x == 0

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_stage_x_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        mouse_event: MouseEvent[Stage] = MouseEvent(this=stage)
        stage_x: Int = mouse_event.stage_x
        stage_var_name: str = stage.variable_name
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{stage_x.variable_name} = '
            f'{mouse_event.variable_name}.pageX - '
            f'{stage_var_name}.offset().left - '
            f'parseInt({stage_var_name}.css("margin-left")) - '
            f'parseInt({stage.variable_name}.css("padding-left"));'
        )
        assert expected in expression
