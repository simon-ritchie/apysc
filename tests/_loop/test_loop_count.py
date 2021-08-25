from random import randint

from retrying import retry

from apysc._expression import expression_data_util
from apysc._loop import loop_count


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_loop_count() -> None:
    expression_data_util.empty_expression()

    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 0

    loop_count._save_loop_count(loop_count=3)
    loop_count_ = loop_count.get_current_loop_count()
    assert loop_count_ == 3


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_increment_current_loop_count() -> None:
    expression_data_util.empty_expression()
    loop_count.increment_current_loop_count()
    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 1

    loop_count.increment_current_loop_count()
    loop_count_ = loop_count.get_current_loop_count()
    assert loop_count_ == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_decrement_current_loop_count() -> None:
    expression_data_util.empty_expression()
    loop_count.increment_current_loop_count()
    loop_count.decrement_current_loop_count()
    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 0

    loop_count.decrement_current_loop_count()
    loop_count_ = loop_count.get_current_loop_count()
    assert loop_count_ == 0


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_loop_count() -> None:
    loop_count._save_loop_count(loop_count=3)
    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 3
