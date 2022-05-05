"""This module is for the E2E testing common utilities
and definitions.
"""

import os
from typing import Callable, List
from typing import Optional as Op
from logging import Logger
import hashlib
from random import randint
from datetime import datetime
import sys
import traceback

from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, Page, ConsoleMessage, Error, Browser

from apysc._lint_and_doc.docs_lang import Lang
from apysc._console import loggers

LOCAL_FILE_PATH_PREFIX: str = f'file://{os.path.abspath("./")}/'
logger: Logger = loggers.get_info_logger()


def get_docs_local_file_path(
        *, lang: Lang, file_name: str) -> str:
    """
    Get a document's local file path for the E2E testing.

    Parameters
    ----------
    lang : Lang
        A target language.
    file_name : str
        A target file name (e.g., `index`).

    Returns
    -------
    file_path : str
        A target document's local file path.
    """
    file_path: str = os.path.join(
        LOCAL_FILE_PATH_PREFIX,
        f'docs/{lang.value}/{file_name}.html',
    )
    return file_path


def assert_local_file_not_raises_error(
        *, file_path: str,
        expected_assertion_failed_msgs: Op[List[str]] = None) -> None:
    """
    Assert a specified local file does not raise an error.

    Parameters
    ----------
    file_path : str
        A target local file path. This path is necessary to
        start with the `file://` prefix.
    expected_assertion_failed_msgs : list of str or None, default None
        Expected assertion failed messages.
        If specified, this interface ignores these assertions'
        error messages.

    Raises
    ------
    AssertionError
        If a specified (HTML or JavaScript) file
        raises an exception.
    """
    logger.info(
        f'Local file\'s assertion started: {file_path}')
    _delete_local_file_assertion_error_logs(file_path=file_path)
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch()
        page: Page = browser.new_page()
        page.on(
            event='console',
            f=_get_local_file_console_event_handler(
                file_path=file_path,
                expected_assert_f_msgs=expected_assertion_failed_msgs,
            ))
        page.on(
            event='pageerror',
            f=_get_local_file_page_err_handler(
                file_path=file_path))
        page.goto(url=file_path)


def _delete_local_file_assertion_error_logs(
        *, file_path: str) -> None:
    """
    Delete local files assertion error logs files if exist.

    Parameters
    ----------
    file_path : str
        A target local file path.
    """
    from apysc._file import file_util
    local_file_page_err_file_path: str = _get_local_file_page_err_file_path(
        file_path=file_path)
    file_util.delete_file_if_exists(file_path=local_file_page_err_file_path)

    local_file_assertion_err_file_path: str = \
        _get_local_file_assertion_err_file_path(file_path=file_path)
    pass


_FILE_PATH_SUFFIX_LOCAL_FILE_PAGE_ERR: str = \
    'e2e_testing_local_file_page_error_'
_FILE_PATH_SUFFIX_LOCAL_FILE_ASSERT_ERR: str = \
    'e2e_testing_local_file_assertion_error_'


def _get_local_file_assertion_err_file_path(*, file_path: str) -> str:
    """
    Get an assertion error log's file path of a local file.

    Parameters
    ----------
    file_path : str
        A target local file path.

    Returns
    -------
    log_file_path : str
        An assertion error log's file path of a local file.
    """
    file_path = _replace_paths_symbols_by_underscore(
        file_path=file_path)
    os.makedirs('./tmp/', exist_ok=True)
    log_file_path: str = (
        f'./tmp/{_FILE_PATH_SUFFIX_LOCAL_FILE_ASSERT_ERR}{file_path}.log'
    )
    return log_file_path


def _get_local_file_page_err_file_path(*, file_path: str) -> str:
    """
    Get a page error log's file path of a local file.

    Parameters
    ----------
    file_path : str
        A target local file path.

    Returns
    -------
    log_file_path : str
        A page error's log file path of a local file.
    """
    file_path = _replace_paths_symbols_by_underscore(
        file_path=file_path)
    os.makedirs('./tmp/', exist_ok=True)
    log_file_path: str = (
        f'./tmp/{_FILE_PATH_SUFFIX_LOCAL_FILE_PAGE_ERR}{file_path}.log'
    )
    return log_file_path


def _replace_paths_symbols_by_underscore(*, file_path: str) -> str:
    """
    Replace path's symbols by the underscore symbol.

    Parameters
    ----------
    file_path : str
        A target file path.

    Returns
    -------
    file_path : str
        A result file path.
    """
    symbols: List[str] = [':', '/', '.']
    for symbol in symbols:
        file_path = file_path.replace(symbol, '_')
    return file_path


def _get_local_file_page_err_handler(
        *,
        file_path: str) -> Callable[[Error], None]:
    """
    Get a page error's event handler.

    Parameters
    ----------
    file_path : str
        A target local file path.

    Returns
    -------
    halder : Callable
        A target handler.
    """

    def handler(err: Error) -> None:
        """
        A handler of this event.

        Parameters
        ----------
        err : Error
            _description_
        """
        err_msg: str = (
            'There is an unexpected error in the following '
            f'local file: {file_path}'
            f'\nError message: {err.message}'
            f'\nStack tace: {err.stack}'
        )
        raise AssertionError(err_msg)

    return handler


_ConsoleHandler = Callable[[ConsoleMessage], None]


def _get_local_file_console_event_handler(
        *, file_path: str,
        expected_assert_f_msgs: Op[List[str]] = None) -> _ConsoleHandler:
    """
    Get a console event's handler.

    Parameters
    ----------
    file_path : str
        A target local file path.
    expected_assert_f_msgs : list of str or None, default None
        Expected assertion failed messages.

    Returns
    -------
    halder : Callable
        A target handler.
    """

    def handler(message: ConsoleMessage) -> None:
        """
        A handler of this event.

        Parameters
        ----------
        message : ConsoleMessage
            A target console message instance.
        """
        if message.type != 'assert':
            return
        if (
                expected_assert_f_msgs is not None
                and message.text in expected_assert_f_msgs):
            return
        err_msg: str = (
            'There is an unexpected assertion error in the '
            f'following local file: {file_path}'
            f'\nError message: {message.text}'
        )
        raise AssertionError(err_msg)

    return handler
