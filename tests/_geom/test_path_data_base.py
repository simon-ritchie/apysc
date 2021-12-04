from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathDataBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_data_base: ap.PathDataBase = ap.PathDataBase(
            path_label=ap.PathLabel.MOVE_TO, relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.MOVE_TO,
                '_relative': True
            },
            any_obj=path_data_base)
