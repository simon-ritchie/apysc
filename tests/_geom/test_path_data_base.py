from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathDataBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_data: ap.PathMoveTo = ap.PathMoveTo(
            x=10, y=20, relative=True)
        assert_attrs(
            expected_attrs={
                '_path_label': ap.PathLabel.MOVE_TO,
                '_relative': True
            },
            any_obj=path_data)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_char(self) -> None:
        path_data: ap.PathMoveTo = ap.PathMoveTo(
            x=10, y=20, relative=False)
        svg_char: str = path_data._get_svg_char()
        assert svg_char == 'M'

        path_data = ap.PathMoveTo(
            x=10, y=20, relative=True)
        svg_char = path_data._get_svg_char()
        assert svg_char == 'm'
