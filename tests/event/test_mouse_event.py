from random import randint
import re
from typing import Optional, Match

from retrying import retry

from apysc import MouseEvent, Int, Sprite
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
        stage_elem_str: str = (
            f'$("#{stage.stage_elem_id}")'
        )
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{stage_x.variable_name} = '
            f'{mouse_event.variable_name}.pageX - '
            f'{stage_elem_str}.offset().left;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_stage_y(self) -> None:
        int_1: Int = Int(10)
        mouse_event: MouseEvent[Int] = MouseEvent(this=int_1)
        stage_y: Int = mouse_event.stage_y
        assert stage_y == 0
        assert isinstance(stage_y, Int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_stage_y_getter_expression(self) -> None:
        stage: Stage = Stage()
        mouse_event: MouseEvent[Stage] = MouseEvent(this=stage)
        stage_y: Int = mouse_event.stage_y
        expression: str = expression_file_util.get_current_expression()
        stage_elem_str: str = (
            f'$("#{stage.stage_elem_id}")'
        )
        expected: str = (
            f'{stage_y.variable_name} = '
            f'{mouse_event.variable_name}.pageY - '
            f'{stage_elem_str}.offset().top;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_local_x(self) -> None:
        int_1: Int = Int(10)
        mouse_event: MouseEvent[Int] = MouseEvent(this=int_1)
        local_x: Int = mouse_event.local_x
        assert local_x == 0
        assert isinstance(local_x, Int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_local_x_getter_expression(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        mouse_event: MouseEvent[Sprite] = MouseEvent(this=sprite)
        local_x: Int = mouse_event.local_x
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{local_x.variable_name} = {var_names.INT}\_.+? \- '
                rf'get_total_x\({sprite.variable_name}\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_local_y(self) -> None:
        int_1: Int = Int(10)
        mouse_event: MouseEvent[Int] = MouseEvent(this=int_1)
        local_y: Int = mouse_event.local_y
        assert local_y == 0
        assert isinstance(local_y, Int)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_local_y_getter_expression(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        mouse_event: MouseEvent[Sprite] = MouseEvent(this=sprite)
        local_y: Int = mouse_event.local_y
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{local_y.variable_name} = {var_names.INT}\_.+? \- '
                rf'get_total_y\({sprite.variable_name}\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_this(self) -> None:
        stage: Stage = Stage()
        mouse_event: MouseEvent[Stage] = MouseEvent(this=stage)
        this: Stage = mouse_event.this
        assert stage == this
