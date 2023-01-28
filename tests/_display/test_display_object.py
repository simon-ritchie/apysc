from random import randint

from retrying import retry

import apysc as ap
from apysc._display.any_display_object import AnyDisplayObject
from apysc._expression import expression_data_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestDisplayObject:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        display_object: AnyDisplayObject = AnyDisplayObject(
            variable_name="test_display_object"
        )
        testing_helper.assert_attrs(
            expected_attrs={
                "stage": stage,
            },
            any_obj=display_object,
        )

    @apply_test_settings()
    def test_variable_name(self) -> None:
        ap.Stage()
        display_object: AnyDisplayObject = AnyDisplayObject(
            variable_name="test_display_object_1"
        )
        display_object.variable_name = "test_display_object_2"
        assert display_object.variable_name == "test_display_object_2"

    @apply_test_settings()
    def test__set_overflow_visible_setting(self) -> None:
        expression_data_util.empty_expression()
        ap.Stage()
        display_object: AnyDisplayObject = AnyDisplayObject(
            variable_name="test_display_object"
        )
        display_object._set_overflow_visible_setting()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{display_object.variable_name}.css("overflow", "visible");'
        assert expected in expression
