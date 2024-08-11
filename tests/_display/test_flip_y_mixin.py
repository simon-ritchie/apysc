import apysc as ap
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    FlipYMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    def __init__(self) -> None:
        """
        The class for the testing of the FlipYMixIn.
        """
        self.variable_name = "test_flip_y_interface"


class TestFlipYMixIn:
    @apply_test_settings()
    def test__initialize_flip_y_if_not_initialized(self) -> None:
        instance: _TestObject = _TestObject()
        instance._initialize_flip_y_if_not_initialized()
        assert not instance._flip_y

        instance._flip_y._value = True
        instance._initialize_flip_y_if_not_initialized()
        assert instance._flip_y

    @apply_test_settings()
    def test_flip_y(self) -> None:
        instance: _TestObject = _TestObject()
        assert not instance.flip_y

        instance.flip_y = ap.Boolean(True)
        assert instance.flip_y

    @apply_test_settings()
    def test__append_flip_y_update_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.flip_y = ap.Boolean(True)
        expression: str = expression_data_util.get_current_expression()
        assert '.flip("y");' in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        instance: _TestObject = _TestObject()
        instance.flip_y = ap.Boolean(True)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if instance._flip_y_snapshots is None:
            raise AssertionError()
        assert instance._flip_y_snapshots[snapshot_name]

        instance.flip_y = ap.Boolean(False)
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._flip_y_snapshots[snapshot_name]

    @apply_test_settings()
    def test__revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance.flip_y = ap.Boolean(True)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance.flip_y = ap.Boolean(False)
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.flip_y

        instance.flip_y = ap.Boolean(False)
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not instance.flip_y

    @apply_test_settings()
    def test__append_flip_y_attr_linking_setting(self) -> None:
        instance: _TestObject = _TestObject()
        instance._initialize_flip_y_if_not_initialized()
        assert instance._attr_linking_stack["flip_y"] == [ap.Boolean(False)]
