from random import randint
from datetime import datetime

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._time import now_mixin


class TestNowMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_now(self) -> None:
        expression_data_util.empty_expression()
        now_: datetime = datetime.now()
        now: ap.DateTime = ap.DateTime.now()
        assert now.year == now_.year
        assert now.month == now_.month
        assert now.day == now_.day
        assert now.hour >= now_.hour
        assert now.minute >= now_.minute
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{now.variable_name} = new Date();"
        assert expected in expression


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_now_expression() -> None:
    expression_data_util.empty_expression()
    datetime: ap.DateTime = ap.DateTime(
        year=2022,
        month=3,
        day=5,
    )
    now_mixin._append_now_expression(dt=datetime)
    expression: str = expression_data_util.get_current_expression()
    expected: str = f"{datetime.variable_name} = new Date();"
    assert expected in expression
