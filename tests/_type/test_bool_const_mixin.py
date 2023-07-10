import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._type.bool_const_mixin import BoolConstMixIn


class TestBoolConstMixIn:
    @apply_test_settings()
    def test__set_value_attr_with_value_arg(self) -> None:
        mixin: BoolConstMixIn = BoolConstMixIn()
        mixin._set_value_attr_with_value_arg(value=True)
        assert not hasattr(mixin, "_value")

    @apply_test_settings()
    def test__set_value_and_skip_expression_appending(self) -> None:
        mixin: BoolConstMixIn = BoolConstMixIn()
        mixin._set_value_and_skip_expression_appending(value=True)
        assert not hasattr(mixin, "_value")

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: BoolConstMixIn = BoolConstMixIn()
        mixin._make_snapshot(snapshot_name="test_snapshot")
        assert not hasattr(mixin, "_snapshot_exists_")

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: BoolConstMixIn = BoolConstMixIn()
        mixin._revert(snapshot_name="test_snapshot")
        assert not hasattr(mixin, "_snapshot_exists_")
        assert not hasattr(mixin, "_value")

    @apply_test_settings()
    def test_value(self) -> None:
        mixin: BoolConstMixIn = BoolConstMixIn()
        mixin._value = True
        assert mixin.value

        with pytest.raises(TypeError):  # type: ignore
            mixin.value = False
