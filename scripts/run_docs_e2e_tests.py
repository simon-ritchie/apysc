"""This module is for the documents' E2E testing.

Command example:
$ python ./scripts/run_docs_e2e_tests.py --lang en
"""

import os
import sys
from argparse import ArgumentParser
from argparse import Namespace
from concurrent import futures
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from typing import Dict
from typing import List
from typing import Optional

from typing_extensions import TypedDict

sys.path.append("./")

from apysc._lint_and_doc.docs_lang import Lang
from apysc._testing import e2e_testing_helper
from apysc._testing.e2e_testing_helper import LocalFileData

_EXPECTED_ASSERTION_FAILED_MSGS: Dict[str, List[str]] = {
    "assertion_basic_behavior": ["", "Values are not equal!"],
    "assert_equal_and_not_equal": ["Values are equal!", "Values are not equal!"],
    "assert_true_and_false": [
        "Boolean value is not True!",
        "Value is not Boolean(True)!",
    ],
    "assert_arrays_equal_and_arrays_not_equal": ["Values are not equal!"],
    "assert_dicts_equal_and_dicts_not_equal": ["Values are not equal!"],
    "assert_defined_and_undefined": ["Value is not defined!"],
}


class _CommandOptions(TypedDict):
    lang: Lang


def _main() -> None:
    """Entry point of this script."""
    command_options: _CommandOptions = _get_command_options()

    file_names: List[str] = _get_file_names(lang=command_options["lang"])
    local_file_data_2dim_list: List[
        List[LocalFileData]
    ] = _create_local_file_data_2dim_list(file_names=file_names)

    future_list: List[Future] = []
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        for local_file_data_list in local_file_data_2dim_list:
            future: Future = executor.submit(
                e2e_testing_helper.assert_local_files_not_raise_error,
                local_file_data_list=local_file_data_list,
            )
            future_list.append(future)
    completed_futures = futures.as_completed(future_list)
    for future in completed_futures:
        future.result()


def _get_command_options() -> _CommandOptions:
    """
    Get command's arguments options.

    Returns
    -------
    options : _CommandOptions
        Command's arguments options.
    """
    parser: ArgumentParser = ArgumentParser(
        description="Run the documents' E2E testing."
    )
    parser.add_argument(
        "-l",
        "--lang",
        action="store",
        choices=[lang.value for lang in Lang],
        type=str,
        help="A target language setting (e.g., en).",
    )
    args: Namespace = parser.parse_args()
    options: _CommandOptions = {
        "lang": Lang(args.lang),
    }
    return options


def _create_local_file_data_2dim_list(
    *, file_names: List[str], single_list_max_len: int = 30
) -> List[List[LocalFileData]]:
    """
    Create a local file data's 2-dimensional list.

    Parameters
    ----------
    file_names : List[str]
        A target file names list.
    single_list_max_len : int, optional
        A single list's maximum length.

    Returns
    -------
    local_file_data_2dim_list : List[List[LocalFileData]]
        A local file data's 2-dimensional list.
    """
    local_file_data_2dim_list: List[List[LocalFileData]] = []
    count: int = 0
    for file_name in file_names:
        if count == 0:
            local_file_data_2dim_list.append([])
        lang: Lang = Lang.EN
        for lang_ in Lang:
            if file_name.startswith(lang_.value):
                lang = lang_
                break
        file_path: str = e2e_testing_helper.get_docs_local_file_path(
            lang=lang, file_name=file_name
        )
        expected_assertion_failed_msgs: Optional[
            List[str]
        ] = _get_expected_assertion_failed_msgs(file_name=file_name)
        local_file_data_2dim_list[-1].append(
            {
                "file_path": file_path,
                "expected_assertion_failed_msgs": expected_assertion_failed_msgs,
            }
        )
        count += 1
        if count >= single_list_max_len:
            count = 0
    return local_file_data_2dim_list


def _get_expected_assertion_failed_msgs(*, file_name: str) -> Optional[List[str]]:
    """
    Get expected assertion failure messages if exist.

    Parameters
    ----------
    file_name : str
        A target document file name.

    Returns
    -------
    expected_assertion_failed_msgs : Optional[List[str]]
        Expected assertion failure messages. If there is no
        definition, this interface returns None.
    """
    for lang in Lang:
        if file_name.startswith(f"{lang.value}_"):
            file_name = file_name.replace(f"{lang.value}_", "", 1)
            break
    expected_assertion_failed_msgs: Optional[
        List[str]
    ] = _EXPECTED_ASSERTION_FAILED_MSGS.get(file_name)
    return expected_assertion_failed_msgs


def _get_file_names(*, lang: Lang) -> List[str]:
    """
    Get target document's file names.

    Parameters
    ----------
    lang : Lang
        A target language.

    Returns
    -------
    file_names : List[str]
        Target document's file names.'
    """
    file_names: List[str] = []
    dir_path: str = f"./docs/{lang.value}/"
    file_names_: List[str] = os.listdir(dir_path)
    file_name: str
    for file_name in file_names_:
        if not file_name.endswith(".html"):
            continue
        file_name = file_name.rsplit(sep=".", maxsplit=1)[0]
        file_names.append(file_name)
    return file_names


if __name__ == "__main__":
    _main()
