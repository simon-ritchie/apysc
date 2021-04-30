from apysc import Dictionary
from tests.testing_helper import assert_raises


class TestDictionary:

    def test__validate_acceptable_value_type(self) -> None:
        dict_1: Dictionary = Dictionary(value={})
        _: Dictionary = Dictionary(value=dict_1)

        assert_raises(
            expected_error_class=ValueError,
            func_or_method=Dictionary,
            kwargs={'value': 10},
            match='Not acceptable value type is specified')
