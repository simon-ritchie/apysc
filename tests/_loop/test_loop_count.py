from apysc._expression import expression_data_util
from apysc._loop import loop_count
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


@apply_test_settings()
def test_get_current_loop_count() -> None:
    ap.Stage()

    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 0

    loop_count._save_loop_count(loop_count=3)
    loop_count_ = loop_count.get_current_loop_count()
    assert loop_count_ == 3


@apply_test_settings()
def test_increment_current_loop_count() -> None:
    ap.Stage()
    loop_count.increment_current_loop_count()
    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 1

    loop_count.increment_current_loop_count()
    loop_count_ = loop_count.get_current_loop_count()
    assert loop_count_ == 2


@apply_test_settings()
def test_decrement_current_loop_count() -> None:
    ap.Stage()
    loop_count.increment_current_loop_count()
    loop_count.decrement_current_loop_count()
    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 0

    loop_count.decrement_current_loop_count()
    loop_count_ = loop_count.get_current_loop_count()
    assert loop_count_ == 0


@apply_test_settings()
def test__save_loop_count() -> None:
    loop_count._save_loop_count(loop_count=3)
    loop_count_: int = loop_count.get_current_loop_count()
    assert loop_count_ == 3
