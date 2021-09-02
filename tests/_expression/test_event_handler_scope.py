from random import randint
from typing import Optional, Tuple

from retrying import retry

from apysc._expression import event_handler_scope
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._expression.event_handler_scope import TemporaryNotHandlerScope


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def teardown() -> None:
    """
    Function that will be called when test ended.
    """
    expression_data_util.empty_expression()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_current_event_handler_scope_count() -> None:
    expression_data_util.empty_expression()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 0

    event_handler_scope._save_current_scope_count(count=3)
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 3


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_current_scope_count() -> None:
    event_handler_scope._save_current_scope_count(count=3)
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 3

    event_handler_scope._save_current_scope_count(count=5)
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 5


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__increment_scope_count() -> None:
    expression_data_util.empty_expression()
    event_handler_scope._increment_scope_count()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 1

    event_handler_scope._increment_scope_count()
    scope_count = event_handler_scope.get_current_event_handler_scope_count()
    assert scope_count == 2


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__decrement_scope_count() -> None:
    expression_data_util.empty_expression()

    event_handler_scope._increment_scope_count()
    event_handler_scope._increment_scope_count()
    event_handler_scope._decrement_scope_count()
    scope_count: int = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 1

    event_handler_scope._decrement_scope_count()
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 0

    event_handler_scope._decrement_scope_count()
    scope_count = event_handler_scope.\
        get_current_event_handler_scope_count()
    assert scope_count == 0


class TestHandlerScope:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        handler_scope: HandlerScope = HandlerScope(
            handler_name='test_handler_1')
        assert handler_scope._handler_name == 'test_handler_1'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        expression_data_util.empty_expression()

        with HandlerScope(handler_name='test_handler_1'):
            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 1

            with HandlerScope(handler_name='test_handler_2'):
                scope_count = event_handler_scope.\
                    get_current_event_handler_scope_count()
                assert scope_count == 2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        expression_data_util.empty_expression()

        with HandlerScope(handler_name='test_handler_1'):

            with HandlerScope(handler_name='test_handler_2'):
                pass

            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 1

        scope_count = event_handler_scope.\
            get_current_event_handler_scope_count()
        assert scope_count == 0


class TestTemporaryNotHandlerScope:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        event_handler_scope._save_current_scope_count(count=1)
        scope: TemporaryNotHandlerScope = TemporaryNotHandlerScope()
        event_handler_scope._save_current_scope_count(count=0)
        assert scope._original_scope_count == 1

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        event_handler_scope._save_current_scope_count(count=1)
        with TemporaryNotHandlerScope():
            scope_count: int = event_handler_scope.\
                get_current_event_handler_scope_count()
            assert scope_count == 0
        event_handler_scope._save_current_scope_count(count=0)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        event_handler_scope._save_current_scope_count(count=1)
        with TemporaryNotHandlerScope():
            pass
        scope_count: int = event_handler_scope.\
            get_current_event_handler_scope_count()
        assert scope_count == 1
        event_handler_scope._save_current_scope_count(count=0)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_handler_calling_stack() -> None:
    expression_data_util.empty_expression()
    with HandlerScope(handler_name='test_handler_1'):
        query: str = (
            'SELECT scope_count FROM '
            f'{expression_data_util.TableName.HANDLER_CALLING_STACK.value} '
            f"WHERE handler_name = 'test_handler_1' LIMIT 1;"
        )
        expression_data_util.cursor.execute(query)
        result: Optional[Tuple[int]] = expression_data_util.cursor.fetchone()
        expression_data_util.connection.commit()
    assert result is not None
    assert result[0] == 1
