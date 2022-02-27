from random import randint

from retrying import retry

from apysc._lint_and_doc.fixed_translation_mapping.data_model import Mapping
from tests.testing_helper import assert_attrs


class TestMapping:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        base: Mapping = Mapping(key='Lorem', value='ipsum')
        assert_attrs(
            expected_attrs={
                '_key': 'Lorem',
                '_value': 'ipsum',
            },
            any_obj=base)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_key(self) -> None:
        base: Mapping = Mapping(key='Lorem', value='ipsum')
        assert base.key == 'Lorem'
