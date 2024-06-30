from apysc._type.disable_value_modification_mixin import DisableValueModificationMixIn
from apysc._testing.testing_helper import apply_test_settings, assert_raises


class TestDisableValueModificationMixIn:
    @apply_test_settings()
    def test_disable_value_modification(self) -> None:
        mixin: DisableValueModificationMixIn = DisableValueModificationMixIn()
        assert not mixin._disabled_value_modification
        mixin.disable_value_modification()
        assert mixin._disabled_value_modification

    @apply_test_settings()
    def test_raise_if_value_modification_is_disabled(self) -> None:
        mixin: DisableValueModificationMixIn = DisableValueModificationMixIn()
        mixin.raise_if_value_modification_is_disabled()

        mixin.disable_value_modification()
        assert_raises(
            expected_error_class=ValueError,
            callable_=mixin.raise_if_value_modification_is_disabled,
        )
