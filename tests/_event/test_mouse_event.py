import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.stage import get_stage_elem_str
from apysc._expression import expression_file_util
from apysc._expression import var_names


class TestMouseEvent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        int_1: ap.Int = ap.Int(10)
        mouse_event: ap.MouseEvent[ap.Int] = ap.MouseEvent(this=int_1)
        assert mouse_event.this == int_1
        assert mouse_event.variable_name.startswith(
            f'{var_names.MOUSE_EVENT}_')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stage_x(self) -> None:
        int_1: ap.Int = ap.Int(10)
        mouse_event: ap.MouseEvent[ap.Int] = ap.MouseEvent(this=int_1)
        stage_x: ap.Int = mouse_event.stage_x
        assert isinstance(stage_x, ap.Int)
        assert stage_x == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_stage_x_getter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: ap.Stage = ap.Stage()
        mouse_event: ap.MouseEvent[ap.Stage] = ap.MouseEvent(this=stage)
        stage_x: ap.Int = mouse_event.stage_x
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{stage_x.variable_name} = '
            f'{mouse_event.variable_name}.pageX - '
            f'{get_stage_elem_str()}.offset().left;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stage_y(self) -> None:
        int_1: ap.Int = ap.Int(10)
        mouse_event: ap.MouseEvent[ap.Int] = ap.MouseEvent(this=int_1)
        stage_y: ap.Int = mouse_event.stage_y
        assert stage_y == 0
        assert isinstance(stage_y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_stage_y_getter_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        mouse_event: ap.MouseEvent[ap.Stage] = ap.MouseEvent(this=stage)
        stage_y: ap.Int = mouse_event.stage_y
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{stage_y.variable_name} = '
            f'{mouse_event.variable_name}.pageY - '
            f'{get_stage_elem_str()}.offset().top;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_local_x(self) -> None:
        int_1: ap.Int = ap.Int(10)
        mouse_event: ap.MouseEvent[ap.Int] = ap.MouseEvent(this=int_1)
        local_x: ap.Int = mouse_event.local_x
        assert local_x == 0
        assert isinstance(local_x, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_local_x_getter_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        mouse_event: ap.MouseEvent[ap.Sprite] = ap.MouseEvent(this=sprite)
        local_x: ap.Int = mouse_event.local_x
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{local_x.variable_name} = {var_names.INT}\_.+? \- '
                rf'get_total_x\({sprite.variable_name}\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_local_y(self) -> None:
        int_1: ap.Int = ap.Int(10)
        mouse_event: ap.MouseEvent[ap.Int] = ap.MouseEvent(this=int_1)
        local_y: ap.Int = mouse_event.local_y
        assert local_y == 0
        assert isinstance(local_y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_local_y_getter_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        mouse_event: ap.MouseEvent[ap.Sprite] = ap.MouseEvent(this=sprite)
        local_y: ap.Int = mouse_event.local_y
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{local_y.variable_name} = {var_names.INT}\_.+? \- '
                rf'get_total_y\({sprite.variable_name}\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        stage: ap.Stage = ap.Stage()
        mouse_event: ap.MouseEvent[ap.Stage] = ap.MouseEvent(this=stage)
        this: ap.Stage = mouse_event.this
        assert stage == this
