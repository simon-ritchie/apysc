from random import randint
from typing import List, Optional, Tuple

from retrying import retry

from apysc._event import handler_circular_calling_util
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__read_handler_names() -> None:
    expression_data_util.empty_expression()
    with HandlerScope(handler_name='test_handler_a_1'):
        with HandlerScope(handler_name='test_handler_b_1'):
            handler_names: List[str] = handler_circular_calling_util.\
                _read_handler_names()
            assert handler_names == ['test_handler_a', 'test_handler_b']

        handler_names = handler_circular_calling_util._read_handler_names()
        assert handler_names == ['test_handler_a']

    handler_names = handler_circular_calling_util._read_handler_names()
    assert handler_names == []


def _is_circular_calling(handler_name: str) -> bool:
    """
    Get a current scope's boolean value.

    Parameters
    ----------
    handler_name : str
        Target handler's name.

    Returns
    -------
    result : bool
        A boolean value whether the current scope is circular calling
        or not.
    """
    return handler_circular_calling_util.is_handler_circular_calling(
        handler_name=handler_name)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_handler_circular_calling() -> None:
    with HandlerScope(handler_name='test_handler_a_1'):
        result: bool = _is_circular_calling('test_handler_a_1')
        assert not result
        with HandlerScope(handler_name='test_handler_b_1'):
            result = _is_circular_calling('test_handler_b_1')
            assert not result
            with HandlerScope(handler_name='test_handler_c_1'):
                result = _is_circular_calling('test_handler_c_1')
                assert not result
                with HandlerScope(handler_name='test_handler_a_2'):
                    result = _is_circular_calling('test_handler_a_2')
                    assert not result
                    with HandlerScope(handler_name='test_handler_b_2'):
                        result = _is_circular_calling('test_handler_b_2')
                        assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_handler_name_to_last_of_list() -> None:
    handler_names: List[str] = handler_circular_calling_util.\
        _append_handler_name_to_last_of_list(
            handler_name='test_handler_a',
            handler_names=[])
    assert handler_names == ['test_handler_a']

    handler_names = handler_circular_calling_util.\
        _append_handler_name_to_last_of_list(
            handler_name='test_handler_a',
            handler_names=[
                'test_handler_a', 'test_handler_b', 'test_handler_a'])
    assert handler_names == [
        'test_handler_a', 'test_handler_b', 'test_handler_a']

    handler_names = handler_circular_calling_util.\
        _append_handler_name_to_last_of_list(
            handler_name='test_handler_a',
            handler_names=['test_handler_a', 'test_handler_b'])
    assert handler_names == [
        'test_handler_a', 'test_handler_b', 'test_handler_a']


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_same_name_prev_hadler_name() -> None:
    with HandlerScope(handler_name='test_handler_a_1'):
        with HandlerScope(handler_name='test_handler_b_1'):
            with HandlerScope(handler_name='test_handler_a_2'):
                same_name_prev_hadler_name: str = \
                    handler_circular_calling_util.\
                    _get_same_name_prev_hadler_name(
                        handler_name='test_handler_a_2')
    assert same_name_prev_hadler_name == 'test_handler_a_1'

    with HandlerScope(handler_name='test_handler_a_1'):
        assert_raises(
            expected_error_class=ValueError,
            func_or_method=handler_circular_calling_util.
            _get_same_name_prev_hadler_name,
            kwargs={'handler_name': 'test_handler_a_1'},
            match='Previous same name handler does not exitst in the SQLite.')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_circular_calling_handler_name() -> None:
    with HandlerScope(handler_name='test_handler_a_1'):
        with HandlerScope(handler_name='test_handler_b_1'):
            with HandlerScope(handler_name='test_handler_a_2'):
                handler_circular_calling_util.\
                    _save_circular_calling_handler_name(
                        handler_name='test_handler_a_2')
    table_name: str = expression_data_util.TableName.\
        CIRCULAR_CALLING_HANDLER_NAME.value
    query: str = (
        f'SELECT handler_name, prev_handler_name FROM {table_name} '
        f"WHERE handler_name = 'test_handler_a_2'; "
    )
    expression_data_util.cursor.execute(query)
    result: Optional[Tuple[str, str]] = expression_data_util.cursor.fetchone()
    expression_data_util.connection.commit()
    assert result == ('test_handler_a_2', 'test_handler_a_1')


# @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_already_saved_circular_calling() -> None:
    expression_data_util.empty_expression()
    with HandlerScope(handler_name='test_handler_a_1'):
        handler_circular_calling_util.is_handler_circular_calling(
            handler_name='test_handler_a_1')
        result: bool = handler_circular_calling_util.\
            _is_already_saved_circular_calling(
                handler_name='test_handler_a_1')
    assert not result

    with HandlerScope(handler_name='test_handler_a_1'):
        with HandlerScope(handler_name='test_handler_b_1'):
            with HandlerScope(handler_name='test_handler_a_2'):
                with HandlerScope(handler_name='test_handler_b_2'):
                    handler_circular_calling_util.is_handler_circular_calling(
                        handler_name='test_handler_b_2')
    result = handler_circular_calling_util.\
        _is_already_saved_circular_calling(
            handler_name='test_handler_b_2')
    assert result
