from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathVertical:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_vertical: ap.PathVertical = ap.PathVertical(
            y=50, relative=True)
        assert_attrs(
            expected_attrs={
                '_y': 50,
                '_path_label': ap.PathLabel.Vertical,
                '_relative': True,
            },
            any_obj=path_vertical,
        )
        assert isinstance(path_vertical._y, ap.Int)
