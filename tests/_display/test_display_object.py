from random import randint

from retrying import retry

import apysc as ap
from apysc._display.display_object import DisplayObject
from apysc._expression import expression_data_util
from tests import testing_helper


class TestDisplayObject:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object')
        testing_helper.assert_attrs(
            expected_attrs={
                'stage': stage,
                '_stage_cls': ap.Stage,
            },
            any_obj=display_object)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_variable_name(self) -> None:
        stage: ap.Stage = ap.Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object_1')
        display_object.variable_name = 'test_display_object_2'
        assert display_object.variable_name == 'test_display_object_2'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_overflow_visible_setting(self) -> None:
        expression_data_util.empty_expression()
        stage: ap.Stage = ap.Stage()
        display_object: DisplayObject = DisplayObject(
            stage=stage, variable_name='test_display_object')
        display_object._set_overflow_visible_setting()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{display_object.variable_name}.css("overflow", "visible");'
        )
        assert expected in expression
