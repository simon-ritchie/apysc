from random import randint

from retrying import retry

from apysc._lint_and_doc.fixed_translation_mapping.base import Base
from tests.testing_helper import assert_attrs


class TestBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        base: Base = Base(key='Lorem', value='ipsum')
        assert_attrs(
            expected_attrs={
                '_key': 'Lorem',
                '_value': 'ipsum',
            },
            any_obj=base)
