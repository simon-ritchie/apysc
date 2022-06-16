from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises
from apysc._type import _delete
from apysc._type.deleted_object_interface import _DisabledObjectError


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_delete_expression() -> None:
    expression_data_util.empty_expression()

    value: ap.Int = ap.Int(10)
    _delete._append_delete_expression(value=value)
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f'delete {value.variable_name};'
        f'\n{value.variable_name} = undefined;'
    )
    assert expected in expression


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_delete() -> None:
    expression_data_util.empty_expression()
    value: ap.Int = ap.Int(10)
    ap.delete(value=value)
    assert_raises(
        expected_error_class=_DisabledObjectError,
        callable_=value.unbind_custom_event_all,
        custom_event_type='test_event',
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_from_parent() -> None:
    int_val: ap.Int = ap.Int(value=10)
    _delete._remove_from_parent(value=int_val)

    ap.Stage()
    sprite: ap.Sprite = ap.Sprite()
    _delete._remove_from_parent(value=sprite)
    assert sprite.parent is None
