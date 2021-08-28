from random import randint

from retrying import retry

import apysc as ap


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_easing_value_type() -> None:
    for easing in ap.Easing:
        assert isinstance(easing.value, str)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_easing_num() -> None:
    assert len(ap.Easing) % 3 == 0


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_easing_const_names() -> None:
    for easing in ap.Easing:
        assert easing.name.startswith('EASE_IN_') \
            or easing.name.startswith('EASE_OUT_')
