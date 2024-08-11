import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.line_joints_mixin import LineJointsMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    LineJointsMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestLineJointsMixIn:
    @apply_test_settings()
    def test__initialize_line_joints_if_not_initialized(self) -> None:
        instance: _TestObject = _TestObject()
        instance._initialize_line_joints_if_not_initialized()
        assert instance._line_joints == ap.LineJoints.MITER.value

        instance._line_joints = ap.String(ap.LineJoints.BEVEL.value)
        instance._initialize_line_joints_if_not_initialized()
        assert instance._line_joints == ap.LineJoints.BEVEL.value

    @apply_test_settings()
    def test_line_joints(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_joints_mixin"
        instance._initialize_line_joints_if_not_initialized()
        assert instance.line_joints == ap.LineJoints.MITER.value

        instance.line_joints = ap.LineJoints.BEVEL
        assert instance.line_joints == ap.LineJoints.BEVEL.value  # type: ignore # noqa

    @apply_test_settings()
    def test__update_line_joints_and_skip_appending_exp(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_joints_mixin"
        assert_raises(
            expected_error_class=TypeError,
            callable_=instance._update_line_joints_and_skip_appending_exp,
            match=r"Not supported line_joints type specified: ",
            value="miter",
        )

        instance._update_line_joints_and_skip_appending_exp(
            value=ap.String(ap.LineJoints.BEVEL.value)
        )
        assert instance.line_joints == ap.LineJoints.BEVEL.value
        expression: str = expression_data_util.get_current_expression()
        assert ".attr" not in expression

        instance._update_line_joints_and_skip_appending_exp(value=ap.LineJoints.MITER)
        assert instance.line_joints == ap.LineJoints.MITER.value

    @apply_test_settings()
    def test__append_line_joints_update_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_joints_mixin"
        instance.line_joints = ap.LineJoints.BEVEL
        instance._append_line_joints_update_expression()
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{instance.variable_name}.attr" rf'\({{"stroke-linejoin": .+?}}\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_joints_mixin"
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._line_joints_snapshots == {
            snapshot_name: ap.LineJoints.MITER.value
        }

        instance.line_joints = ap.LineJoints.BEVEL
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._line_joints_snapshots == {
            snapshot_name: ap.LineJoints.MITER.value
        }

    @apply_test_settings()
    def test__revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_line_joints_mixin"
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance.line_joints = ap.LineJoints.BEVEL
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.line_joints == ap.LineJoints.MITER.value  # type: ignore # noqa

        instance.line_joints = ap.LineJoints.BEVEL
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.line_joints == ap.LineJoints.BEVEL.value  # type: ignore # noqa
