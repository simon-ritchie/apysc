import apysc as ap
from apysc._display.svg_text_bold_mixin import SVGTextBoldMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMIxIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextBoldMixIn
):
    pass


class TestSVGTextBoldMixIn:
    @apply_test_settings()
    def test_bold(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMIxIn = _TestMIxIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        bold: ap.Boolean = mixin.bold
        assert not bold
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{bold.variable_name} = {mixin.variable_name}.font("weight") === "bold";'
        )
        assert expected in expression

        bold: ap.Boolean = ap.Boolean(True)
        mixin.bold = bold
        assert bold
        expression = expression_data_util.get_current_expression()
        expected = (
            f"if ({bold.variable_name}) {{"
            f'\n  {mixin.variable_name}.font("weight", "bold");'
            "\n} else {"
            f'\n  {mixin.variable_name}.font("weight", "normal");'
            "\n}"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot__revert(self) -> None:
        mixin: _TestMIxIn = _TestMIxIn()
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._bold = True
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._bold = False
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._bold

        mixin._bold = False
        mixin._run_all_revert_methods(snapshot_name="not_existing_snapshot")
        assert not mixin._bold
