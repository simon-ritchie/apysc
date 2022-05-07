import os
from random import randint
from typing import Callable
from typing import List

from playwright.sync_api import ConsoleMessage
from playwright.sync_api import Error
from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing import e2e_testing_helper
from apysc._testing.e2e_testing_helper import LocalFileData
from apysc._testing.testing_helper import assert_raises


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
        """
        Get a type text.

        Returns
        -------
        type : str
            A type text.
        """
        return self._type

    @property
    def text(self) -> str:
        """
        Get a console text.

        Returns
        -------
        text : str
            A console text.
        """
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

    log_file_path: str = e2e_testing_helper.\
        _get_local_file_assertion_err_file_path(file_path=file_path)
    assert os.path.exists(log_file_path)
    e2e_testing_helper._delete_local_file_assertion_error_logs(
        file_path=file_path)


class _MockError(Error):

    _message: str
    _stack: str

    def __init__(self, *, message: str, stack: str) -> None:
        """
        The mock class for the Error class.

        Parameters
        ----------
        message : str
            An error message.
        stack : str
            A stack trace string.
        """
        self._message = message
        self._stack = stack

    @property
    def message(self) -> str:
        """
        Get an error message.

        Returns
        -------
        message : str
            An error message.
        """
        return self._message

    @property
    def stack(self) -> str:
        """
        Get a stack trace string.

        Returns
        -------
        stack : str
            Get a stack trace string.
        """
        return self._stack


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_local_file_page_err_handler() -> None:
    file_path: str = 'file://test/path.html'
    handler: Callable[[Error], None] = e2e_testing_helper.\
        _get_local_file_page_err_handler(
            file_path=file_path)
    err: Error = _MockError(
        message='Test error!',
        stack='Uncaught Error: Test error!\nat <anonymous>:1:7')
    assert_raises(
        expected_error_class=AssertionError,
        func_or_method=handler,
        kwargs={
            'err': err,
        },
        match='There is an unexpected error',
    )

    log_file_path: str = e2e_testing_helper.\
        _get_local_file_page_err_file_path(file_path=file_path)
    assert os.path.exists(log_file_path)
    e2e_testing_helper._delete_local_file_assertion_error_logs(
        file_path=file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__replace_paths_symbols_by_underscore() -> None:
    file_path: str = e2e_testing_helper._replace_paths_symbols_by_underscore(
        file_path='file://docs/en/index.html')
    assert file_path == 'file___docs_en_index_html'


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_local_file_page_err_file_path() -> None:
    log_file_path: str = e2e_testing_helper.\
        _get_local_file_page_err_file_path(
            file_path='file://docs/en/index.html')
    assert log_file_path == (
        './tmp/e2e_testing_local_file_page_error_file'
        '___docs_en_index_html.log'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_local_file_assertion_err_file_path() -> None:
    log_file_path: str = e2e_testing_helper.\
        _get_local_file_assertion_err_file_path(
            file_path='file://docs/en/index.html')
    assert log_file_path == (
        './tmp/e2e_testing_local_file_assertion_error_file'
        '___docs_en_index_html.log'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__delete_local_file_assertion_error_logs() -> None:
    file_path: str = 'file://docs/en/index.html'
    local_file_page_err_file_path: str = e2e_testing_helper.\
        _get_local_file_page_err_file_path(file_path=file_path)
    file_util.save_plain_txt(txt='', file_path=local_file_page_err_file_path)

    local_file_assertion_err_file_path: str = e2e_testing_helper.\
        _get_local_file_assertion_err_file_path(file_path=file_path)
    file_util.save_plain_txt(
        txt='', file_path=local_file_assertion_err_file_path)

    e2e_testing_helper._delete_local_file_assertion_error_logs(
        file_path=file_path)
    assert not os.path.exists(local_file_page_err_file_path)
    assert not os.path.exists(local_file_assertion_err_file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__assert_local_file_error_log_not_exits() -> None:
    file_path: str = 'file://docs/en/index.html'
    e2e_testing_helper._delete_local_file_assertion_error_logs(
        file_path=file_path)
    e2e_testing_helper._assert_local_file_error_log_not_exits(
        file_path=file_path)

    local_file_page_err_file_path: str = e2e_testing_helper.\
        _get_local_file_page_err_file_path(file_path=file_path)
    file_util.save_plain_txt(txt='', file_path=local_file_page_err_file_path)
    assert_raises(
        expected_error_class=AssertionError,
        func_or_method=e2e_testing_helper.
        _assert_local_file_error_log_not_exits,
        kwargs={'file_path': file_path})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_assert_local_files_not_raise_error() -> None:
    file_path: str = e2e_testing_helper.get_docs_local_file_path(
        lang=Lang.EN, file_name='index')
    local_file_data_list: List[LocalFileData] = [{
        'file_path': file_path,
        'expected_assertion_failed_msgs': None,
    }]
    e2e_testing_helper.assert_local_files_not_raise_error(
        local_file_data_list=local_file_data_list)

    file_path = e2e_testing_helper.get_docs_local_file_path(
        lang=Lang.EN, file_name='assert_equal_and_not_equal')
    local_file_data_list = [{
        'file_path': file_path,
        'expected_assertion_failed_msgs': None,
    }]
    assert_raises(
        expected_error_class=AssertionError,
        func_or_method=e2e_testing_helper.assert_local_files_not_raise_error,
        kwargs={'local_file_data_list': local_file_data_list},
    )
