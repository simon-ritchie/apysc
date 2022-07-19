"""This module is for the E2E testing common utilities
and definitions.
"""

import os
from logging import Logger
from typing import Callable
from typing import List
from typing import Optional as Op

from playwright.sync_api import Browser
from playwright.sync_api import ConsoleMessage
from playwright.sync_api import Error
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from typing_extensions import TypedDict

from apysc._console import loggers
from apysc._lint_and_doc.docs_lang import Lang

LOCAL_FILE_PATH_PREFIX: str = f'file://{os.path.abspath("./")}/'
logger: Logger = loggers.get_info_logger()


def get_docs_local_file_path(*, lang: Lang, file_name: str) -> str:
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
        f"docs/{lang.value}/{file_name}.html",
    )
    return file_path


def _assert_local_file_error_log_not_exits(*, file_path: str) -> None:
    """
    Assert that local file assertion's an error log does not exist.

    Parameters
    ----------
    file_path : str
        A target file path.

    Raises
    ------
    AssertionError
        If there is an error log file.
    """
    from apysc._file import file_util

    local_file_page_err_file_path: str = _get_local_file_page_err_file_path(
        file_path=file_path
    )
    local_file_assertion_err_file_path: str = _get_local_file_assertion_err_file_path(
        file_path=file_path
    )
    log_file_paths: List[str] = [
        local_file_page_err_file_path,
        local_file_assertion_err_file_path,
    ]
    for log_file_path in log_file_paths:
        if not os.path.isfile(log_file_path):
            continue
        log_txt: str = file_util.read_txt(file_path=log_file_path)
        raise AssertionError(log_txt)


def _delete_local_file_assertion_error_logs(*, file_path: str) -> None:
    """
    Delete local files assertion error logs files if they exist.

    Parameters
    ----------
    file_path : str
        A target local file path.
    """
    from apysc._file import file_util

    local_file_page_err_file_path: str = _get_local_file_page_err_file_path(
        file_path=file_path
    )
    file_util.delete_file_if_exists(file_path=local_file_page_err_file_path)

    local_file_assertion_err_file_path: str = _get_local_file_assertion_err_file_path(
        file_path=file_path
    )
    file_util.delete_file_if_exists(file_path=local_file_assertion_err_file_path)


_FILE_PATH_SUFFIX_LOCAL_FILE_PAGE_ERR: str = "e2e_testing_local_file_page_error_"
_FILE_PATH_SUFFIX_LOCAL_FILE_ASSERT_ERR: str = "e2e_testing_local_file_assertion_error_"


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
    file_path = _replace_paths_symbols_by_underscore(file_path=file_path)
    os.makedirs("./tmp/", exist_ok=True)
    log_file_path: str = (
        f"./tmp/{_FILE_PATH_SUFFIX_LOCAL_FILE_ASSERT_ERR}{file_path}.log"
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
    file_path = _replace_paths_symbols_by_underscore(file_path=file_path)
    os.makedirs("./tmp/", exist_ok=True)
    log_file_path: str = f"./tmp/{_FILE_PATH_SUFFIX_LOCAL_FILE_PAGE_ERR}{file_path}.log"
    return log_file_path


def _replace_paths_symbols_by_underscore(*, file_path: str) -> str:
    """
    Replace the path's symbols with the underscore symbol.

    Parameters
    ----------
    file_path : str
        A target file path.

    Returns
    -------
    file_path : str
        A result file path.
    """
    symbols: List[str] = [":", "/", "."]
    for symbol in symbols:
        file_path = file_path.replace(symbol, "_")
    return file_path


def _get_local_file_page_err_handler(*, file_path: str) -> Callable[[Error], None]:
    """
    Get a page error's event handler.

    Parameters
    ----------
    file_path : str
        A target local file path.

    Returns
    -------
    handler : Callable
        A target handler.
    """
    from apysc._file import file_util

    def handler(err: Error) -> None:
        """
        A handler of this event.

        Parameters
        ----------
        err : Error
            _description_
        """
        log_file_path: str = _get_local_file_page_err_file_path(file_path=file_path)

        file_path_: str = file_path.replace("file://", "", 1)
        file_txt: str = ""
        if os.path.isfile(file_path_):
            file_txt = file_util.read_txt(file_path=file_path_)
        err_msg: str = (
            "There is an unexpected error in the following "
            f"Local file: {file_path}"
            f"\nError message: {err.message}"
            f"\nStack trace: {err.stack}"
            f"\nLocal file text:\n\n{file_txt}"
        )
        file_util.save_plain_txt(txt=err_msg, file_path=log_file_path)
        raise AssertionError(err_msg)

    return handler


_ConsoleHandler = Callable[[ConsoleMessage], None]


def _get_local_file_console_event_handler(
    *, file_path: str, expected_assert_f_msgs: Op[List[str]] = None
) -> _ConsoleHandler:
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
    handler : Callable
        A target handler.
    """
    from apysc._file import file_util

    def handler(message: ConsoleMessage) -> None:
        """
        A handler of this event.

        Parameters
        ----------
        message : ConsoleMessage
            A target console message instance.
        """
        if message.type != "assert":
            return
        if (
            expected_assert_f_msgs is not None
            and message.text in expected_assert_f_msgs
        ):
            return
        log_file_path: str = _get_local_file_assertion_err_file_path(
            file_path=file_path
        )
        err_msg: str = (
            "There is an unexpected assertion error in the "
            f"following local file: {file_path}"
            f"\nError message: {message.text}"
        )
        file_util.save_plain_txt(txt=err_msg, file_path=log_file_path)
        raise AssertionError(err_msg)

    return handler


class LocalFileData(TypedDict):
    file_path: str
    expected_assertion_failed_msgs: Op[List[str]]


def assert_local_files_not_raise_error(
    *, local_file_data_list: List[LocalFileData]
) -> None:
    """
    Assert specified local files do not raise an error.

    Parameters
    ----------
    local_file_data_list : List[LocalFileData]
        A target local file data list.

    Raises
    ------
    AssertionError
        If specified files raise an exception.
    """
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch()
        for local_file_data in local_file_data_list:
            file_path: str = local_file_data["file_path"]
            _delete_local_file_assertion_error_logs(file_path=file_path)
            expected_assert_f_msgs: Op[List[str]] = local_file_data[
                "expected_assertion_failed_msgs"
            ]
            logger.info(f"Local file's assertion started: {file_path}")
            for _ in range(2):
                page: Page = browser.new_page()
                page.on(
                    event="console",
                    f=_get_local_file_console_event_handler(
                        file_path=file_path,
                        expected_assert_f_msgs=expected_assert_f_msgs,
                    ),
                )
                page.on(
                    event="pageerror",
                    f=_get_local_file_page_err_handler(file_path=file_path),
                )
                page.goto(url=file_path)
                _assert_local_file_error_log_not_exits(file_path=file_path)
