from random import randint
from typing import Callable

from retrying import retry
from playwright.sync_api import Playwright, Page, ConsoleMessage, Error, Browser

from tests import e2e_testing_helper
from apysc._lint_and_doc.docs_lang import Lang
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_docs_local_file_path() -> None:
    file_path: str = e2e_testing_helper.get_docs_local_file_path(
        lang=Lang.EN, file_name='index')
    assert file_path.startswith('file://')
    assert file_path.endswith('/docs/en/index.html')


class _MockConsoleMessage(ConsoleMessage):

    _type: str
    _text: str

    def __init__(self, *, type: str, text: str) -> None:
        """
        This class is the mock class for the ConsoleMessage.

        Parameters
        ----------
        type : str
            A target type string.
        text : str
            A message text.
        """
        self._type = type
        self._text = text

    @property
    def type(self) -> str:
        return self._type

    @property
    def text(self) -> str:
        return self._text


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_local_file_console_event_handler() -> None:
    file_path: str = e2e_testing_helper.get_docs_local_file_path(
        lang=Lang.EN, file_name='index')
    handler: Callable[[ConsoleMessage], None] = e2e_testing_helper.\
        _get_local_file_console_event_handler(
            file_path=file_path)
    message: ConsoleMessage = _MockConsoleMessage(
        type='log', text='Test message 1.')
    handler(message)

    message = _MockConsoleMessage(
        type='assert', text='Test message 1.')
    handler = e2e_testing_helper._get_local_file_console_event_handler(
        file_path=file_path,
        expected_assert_f_msgs=['Test message 1.'])
    handler(message)

    message = _MockConsoleMessage(
        type='assert', text='Test message 2.')
    assert_raises(
        expected_error_class=AssertionError,
        func_or_method=handler,
        kwargs={'message': message},
        match='There is an unexpected assertion error')
