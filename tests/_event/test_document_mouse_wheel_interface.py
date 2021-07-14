from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from apysc._event.handler import get_handler_name
from apysc._expression import expression_file_util
from apysc._expression import var_names


def on_mouse_wheel_1(e: ap.WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler for mouse wheel event.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    assert options['msg'] == 'Hello!'


def on_mouse_wheel_2(e: ap.WheelEvent, options: Dict[str, Any]) -> None:
    """
    Test handler for mouse wheel event.

    Parameters
    ----------
    e : WheelEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    assert options == {}


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_bind_wheel_event_to_document() -> None:
    expression_file_util.remove_expression_file()
    name: str = ap.bind_wheel_event_to_document(
        handler=on_mouse_wheel_1, options={'msg': 'Hello!'})
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'$({ap.document.variable_name}).on("mousewheel", {name});'
    )
    assert expected in expression

    expression = expression_file_util.\
        get_current_event_handler_scope_expression()
    expected = (
        f'function {name}({var_names.WHEEL_EVENT}_'
    )
    assert expected in expression

    _ = ap.bind_wheel_event_to_document(handler=on_mouse_wheel_2)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_unbind_wheel_event_from_document() -> None:
    expression_file_util.remove_expression_file()
    ap.unbind_wheel_event_from_document(handler=on_mouse_wheel_1)
    name: str = get_handler_name(
        handler=on_mouse_wheel_1, instance=ap.document)
    expression: str = expression_file_util.get_current_expression()
    expected: str = (
        f'$({ap.document.variable_name}).off("mousewheel", {name});'
    )
    assert expected in expression


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_unbind_wheel_event_all_from_document() -> None:
    expression_file_util.remove_expression_file()
    ap.unbind_wheel_event_all_from_document()
    expression: str = expression_file_util.get_current_expression()
    expected: str = f'$({ap.document.variable_name}).off("mousewheel");'
    assert expected in expression
