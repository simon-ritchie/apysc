"""This module is for the E2E testing common utilities
and definitions.
"""

import os
from typing import Callable, List
from typing import Optional as Op
from logging import Logger

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
    Asert a specified local file does not raise an error.

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
    pass


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
        raise AssertionError(
            'There is an unexpected error in the following '
            f'local file: {file_path}'
            f'\nError message: {err.message}'
            f'\nStack tace: {err.stack}')

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
        raise AssertionError(
            'There is an unexpected assertion error in the '
            f'following local file: {file_path}'
            f'\nError message: {message.text}')

    return handler
