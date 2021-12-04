from random import randint

from retrying import retry

import apysc as ap
from tests.testing_helper import assert_attrs


class TestPathLineTo:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(
            x=50, y=100, relative=True)
        assert_attrs(
            expected_attrs={
                '_x': 50,
                '_y': 100,
                '_path_label': ap.PathLabel.LINE_TO,
                '_relative': True,
            },
            any_obj=path_line_to,
        )
        assert isinstance(path_line_to._x, ap.Int)
        assert isinstance(path_line_to._y, ap.Int)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_str(self) -> None:
        path_line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=100)
        svg_str: str = path_line_to._get_svg_str()
        expected: str = (
            f'"L " + String({path_line_to._x.variable_name}) + '
            f'" " + String({path_line_to._y.variable_name})'
        )
        assert svg_str == expected
