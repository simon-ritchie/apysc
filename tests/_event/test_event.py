from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from tests import testing_helper


class TestEvent:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        int_1: ap.Int = ap.Int(10)
        event: ap.Event = ap.Event(this=int_1)
        testing_helper.assert_attrs(
            expected_attrs={
                '_this': int_1,
            },
            any_obj=event)
        assert event.variable_name.startswith(
            f'{var_names.EVENT}_'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stop_propagation(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(10)
        e: ap.Event = ap.Event(this=int_1)
        e.stop_propagation()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{e.variable_name}.stopPropagation();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        expression_data_util.empty_expression()
        int_1: ap.Int = ap.Int(10)
        e: ap.Event = ap.Event(this=int_1)
        e.prevent_default()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{e.variable_name}.preventDefault();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_this(self) -> None:
        stage: ap.Stage = ap.Stage()
        e: ap.Event[ap.Stage] = ap.Event(this=stage)
        this: ap.Stage = e.this
        assert this == stage

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__validate_type_name_and_self_type(self) -> None:

        class AnyEvent(ap.Event):
            ...

        int_1: ap.Int = ap.Int(10)
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=ap.Event,
            kwargs={
                'this': int_1,
                'type_name': 'any_event',
            })
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=AnyEvent,
            kwargs={
                'this': int_1,
            })

        _ = ap.Event(this=int_1)
        _ = AnyEvent(this=int_1, type_name='any_event')
