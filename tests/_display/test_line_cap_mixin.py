import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.line_cap_mixin import LineCapMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import VariableNameSuffixAttrOrVarMixIn


class _TestObject(
    LineCapMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestLineCapMixIn:
    @apply_test_settings()
    def test__initialize_line_cap_if_not_initialized(self) -> None:
        instance: _TestObject = _TestObject()
        instance._initialize_line_cap_if_not_initialized()
        assert instance._line_cap == ap.LineCaps.BUTT.value

        instance._line_cap = ap.String(ap.LineCaps.ROUND.value)
        instance._initialize_line_cap_if_not_initialized()
        assert instance._line_cap == ap.LineCaps.ROUND.value

    @apply_test_settings()
    def test_line_cap(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_cap_mixin"
        assert instance.line_cap == ap.LineCaps.BUTT.value

        instance.line_cap = ap.LineCaps.ROUND
        assert instance.line_cap == ap.LineCaps.ROUND.value  # type: ignore

        instance.line_cap = ap.String(ap.LineCaps.BUTT.value)
        assert instance.line_cap == ap.LineCaps.BUTT.value

    @apply_test_settings()
    def test__append_line_cap_update_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_cap_mixin"
        instance.line_cap = ap.LineCaps.ROUND
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{instance.variable_name}.attr\({{"
                rf'"stroke-linecap": {var_names.STRING}\_.+?}}\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_cap_mixin"
        instance.line_cap = ap.LineCaps.ROUND
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._line_cap_snapshots == {snapshot_name: ap.LineCaps.ROUND.value}

        instance.line_cap = ap.LineCaps.BUTT
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._line_cap_snapshots == {snapshot_name: ap.LineCaps.ROUND.value}

    @apply_test_settings()
    def test__revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_cap_mixin"
        instance.line_cap = ap.LineCaps.ROUND
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance.line_cap = ap.LineCaps.BUTT
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.line_cap == ap.LineCaps.ROUND.value  # type: ignore

        instance.line_cap = ap.LineCaps.BUTT
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.line_cap == ap.LineCaps.BUTT.value  # type: ignore

    @apply_test_settings()
    def test__update_line_cap_and_skip_appending_exp(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_cap_mixin"
        instance._update_line_cap_and_skip_appending_exp(value=ap.LineCaps.ROUND)
        assert instance.line_cap == ap.LineCaps.ROUND.value
        instance._update_line_cap_and_skip_appending_exp(
            value=ap.String(ap.LineCaps.BUTT.value)
        )
        assert instance.line_cap == ap.LineCaps.BUTT.value
        expression: str = expression_data_util.get_current_expression()
        assert f"{instance.variable_name}.attr" not in expression
