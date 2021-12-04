from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathClose:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_close: ap.PathClose = ap.PathClose()
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.CLOSE,
                '_relative': False,
            },
            any_obj=path_close)
