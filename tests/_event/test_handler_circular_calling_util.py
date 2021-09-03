from random import randint
from typing import List

from retrying import retry

from apysc._event import handler_circular_calling_util
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_handler_names() -> None:
    expression_data_util.empty_expression()
    with HandlerScope(handler_name='test_handler_1'):
        with HandlerScope(handler_name='test_handler_2'):
            handler_names: List[str] = handler_circular_calling_util.\
                _read_handler_names()
            assert handler_names == ['test_handler_1', 'test_handler_2']

        handler_names = handler_circular_calling_util._read_handler_names()
        assert handler_names == ['test_handler_1']

    handler_names = handler_circular_calling_util._read_handler_names()
    assert handler_names == []


def _is_circular_calling() -> bool:
    """
    Get a current scope's boolean value.

    Returns
    -------
    result : bool
        A boolean value whether the current scope is circular calling
        or not.
    """
    return handler_circular_calling_util.is_handler_circular_calling(
        handler_name='test_handler_2')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_handler_circular_calling() -> None:
    with HandlerScope(handler_name='test_handler_1'):
        result: bool = _is_circular_calling()
        assert not result
        with HandlerScope(handler_name='test_handler_2'):
            result = _is_circular_calling()
            assert not result
            with HandlerScope(handler_name='test_handler_3'):
                result = _is_circular_calling()
                assert not result
                with HandlerScope(handler_name='test_handler_1'):
                    result = _is_circular_calling()
                    assert not result
                    with HandlerScope(handler_name='test_handler_2'):
                        result = _is_circular_calling()
                        assert result
