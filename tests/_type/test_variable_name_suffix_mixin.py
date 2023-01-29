from random import randint

from retrying import retry

from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestVariableNameSuffixMixIn:
    @apply_test_settings()
    def test_variable_name_suffix(self) -> None:
        mixin: VariableNameSuffixMixIn = VariableNameSuffixMixIn()
        assert mixin._variable_name_suffix == ""

        mixin._variable_name_suffix = "test_instance"
        assert mixin._variable_name_suffix == "test_instance"
