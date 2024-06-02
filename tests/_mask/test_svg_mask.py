import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestSvgMask:

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        mask: ap.SvgMask = ap.SvgMask()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {mask.variable_name} = {ap.get_stage().variable_name}" ".mask();"
        )
        assert expected in expression

    @apply_test_settings()
    def test___init__(self) -> None:
        mask: ap.SvgMask = ap.SvgMask(variable_name_suffix="test_suffix")
        assert var_names.MASK in mask.variable_name
        assert mask._variable_name_suffix == "test_suffix"

    @apply_test_settings(retrying_max_attempts_num=0)
    def test_add_svg_masking_object(self) -> None:
        rectangle_1: ap.Rectangle = ap.Rectangle(
            x=50, y=50, width=50, height=50, fill_color=ap.Color("#0af")
        )
        mask: ap.SvgMask = ap.SvgMask()
        mask.add_svg_masking_object(masking_object=rectangle_1)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mask.variable_name}.add({rectangle_1.variable_name});"
        assert expected in expression
        assert (
            rectangle_1._fill_color._value.lower() == ap.Color("#FFFFFF")._value.lower()
        )

        rectangle_2: ap.Rectangle = ap.Rectangle(
            x=150, y=50, width=50, height=50, fill_color=ap.Color("#f0a")
        )
        mask.add_svg_masking_object(masking_object=rectangle_2, alpha=0.0)
        assert (
            rectangle_2._fill_color._value.lower() == ap.Color("#000000")._value.lower()
        )
