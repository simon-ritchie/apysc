import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_easing_value_type() -> None:
    for easing in ap.Easing:
        assert isinstance(easing.value, str)


@apply_test_settings()
def test_easing_num() -> None:
    assert (len(ap.Easing) - 1) % 3 == 0


@apply_test_settings()
def test_easing_const_names() -> None:
    for easing in ap.Easing:
        if easing.name == "LINEAR":
            continue
        assert easing.name.startswith("EASE_IN_") or easing.name.startswith("EASE_OUT_")
