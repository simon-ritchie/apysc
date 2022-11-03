from random import randint

from retrying import retry

from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._type.blank_object_mixin import BlankObjectMixIn


class TestBlankObjectMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_blank_object_if_not_initialized(self) -> None:
        expression_data_util.empty_expression()
        mixin: BlankObjectMixIn = BlankObjectMixIn()
        mixin._initialize_blank_object_if_not_initialized()
        assert mixin._initialize_blank_object_if_not_initialized
        assert mixin._blank_object_variable_name.startswith(
            f"{var_names.BLANK_OBJECT}_"
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var {mixin._blank_object_variable_name} = {{}};"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_blank_object_variable_name(self) -> None:
        mixin: BlankObjectMixIn = BlankObjectMixIn()
        blank_object_variable_name: str = mixin.blank_object_variable_name
        assert blank_object_variable_name.startswith(f"{var_names.BLANK_OBJECT}_")
