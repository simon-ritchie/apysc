import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestMask:

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        mask: ap.Mask = ap.Mask()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {mask.variable_name} = {ap.get_stage().variable_name}" ".mask();"
        )
        assert expected in expression

    @apply_test_settings()
    def test___init__(self) -> None:
        mask: ap.Mask = ap.Mask(variable_name_suffix="test_suffix")
        assert var_names.MASK in mask.variable_name
        assert mask._variable_name_suffix == "test_suffix"
