from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestEvent:
    @apply_test_settings()
    def test___init__(self) -> None:
        int_1: ap.Int = ap.Int(10)
        event: ap.Event = ap.Event(this=int_1)
        testing_helper.assert_attrs(
            expected_attrs={
                "_this": int_1,
            },
            any_obj=event,
        )
        assert event.variable_name.startswith(f"{var_names.EVENT}_")

    @apply_test_settings()
    def test_this(self) -> None:
        stage: ap.Stage = ap.Stage()
        e: ap.Event[ap.Stage] = ap.Event(this=stage)
        this: ap.Stage = e.this
        assert this == stage

    @apply_test_settings()
    def test__validate_type_name_and_self_type(self) -> None:
        class AnyEvent(ap.Event):
            ...

        int_1: ap.Int = ap.Int(10)
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            callable_=ap.Event,
            this=int_1,
            type_name="any_event",
        )
        testing_helper.assert_raises(
            expected_error_class=ValueError, callable_=AnyEvent, this=int_1
        )

        _ = ap.Event(this=int_1)
        _ = AnyEvent(this=int_1, type_name="any_event")
