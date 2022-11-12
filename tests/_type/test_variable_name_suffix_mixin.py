from random import randint

from retrying import retry

from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class TestVariableNameSuffixMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_variable_name_suffix(self) -> None:
        mixin: VariableNameSuffixMixIn = VariableNameSuffixMixIn()
        assert mixin._variable_name_suffix == ""

        mixin._variable_name_suffix = "test_instance"
        assert mixin._variable_name_suffix == "test_instance"
