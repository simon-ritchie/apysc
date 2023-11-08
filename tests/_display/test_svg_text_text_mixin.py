import apysc as ap
from apysc._display.svg_text_text_mixin import SvgTextTextMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SvgTextTextMixIn,
):
    pass


class TestSvgTextTextMixIn:
    @apply_test_settings()
    def test__append_text_getter_expression(self) -> None:
        mixin: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin.variable_name = "test_mixin"
        text: ap.String = ap.String("Lorem ipsum")
        mixin._append_text_getter_expression(text=text)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name} = {mixin._variable_name}.text();"
        assert expected in expression

    @apply_test_settings()
    def test_text(self) -> None:
        mixin_1: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin_1.variable_name = "test_mixin"
        mixin_1._text = "Lorem ipsum"
        text: ap.String = mixin_1.text
        assert text._value == "Lorem ipsum"
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{text.variable_name} = {mixin_1._variable_name}.text();"
        assert expected in expression

        mixin_1.text = ap.String("test text")
        assert mixin_1._text == "test text"
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin_1.variable_name}.text({text.variable_name});"

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2._variable_name_suffix = "test_suffix"
        mixin_2._text = "Lorem ipsum"
        text = mixin_2.text
        assert "test_suffix" in text.variable_name

    @apply_test_settings()
    def test__append_text_setter_expression(self) -> None:
        mixin: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin.variable_name = "test_mixin"
        text: ap.String = ap.String("Lorem ipsum")
        mixin._append_text_setter_expression(text=text)
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.text({text.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot_and_revert(self) -> None:
        mixin: SvgTextTextMixIn = SvgTextTextMixIn()
        mixin._text = "Lorem"
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._text = "ipsum"
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._text == "Lorem"

        mixin._text = "ipsum"
        mixin._run_all_revert_methods(snapshot_name="not existing snapshot")
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._text == "ipsum"
