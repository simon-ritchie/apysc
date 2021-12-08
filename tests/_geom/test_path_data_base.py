from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
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
        assert isinstance(path_data._relative, ap.Boolean)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_svg_char(self) -> None:
        expression_data_util.empty_expression()
        path_data: ap.PathMoveTo = ap.PathMoveTo(
            x=10, y=20, relative=False)
        svg_char: ap.String = path_data._get_svg_char()
        assert svg_char == 'M'
        assert isinstance(svg_char, ap.String)
        expression: str = expression_data_util.get_current_expression()
        assert 'if (' in expression
        assert 'else {' in expression

        path_data = ap.PathMoveTo(
            x=10, y=20, relative=True)
        svg_char = path_data._get_svg_char()
        assert svg_char == 'm'
        assert isinstance(svg_char, ap.String)
