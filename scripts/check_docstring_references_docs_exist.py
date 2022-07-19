"""This module is for checking whether docstring references
sections' document files exist.

Command examples:
$ python scripts/check_docstring_references_docs_exist.py
"""

import os
import sys
from logging import Logger
from types import ModuleType
from typing import List

from tqdm import tqdm

sys.path.append("./")

from apysc._console import loggers
from apysc._file import module_util
from apysc._lint_and_doc import docstring_util
from apysc._lint_and_doc.docstring_util import Reference

logger: Logger = loggers.get_info_logger()


def _main(*, dir_path: str = "./apysc/") -> List[str]:
    """
    Entry point of this command.

    Parameters
    ----------
    dir_path : str, default './apysc'
        A directory path to search modules recursively.

    Returns
    -------
    file_names : list of str
        A list of checked file names.
    """
    file_names: List[str] = _extract_file_names(dir_path=dir_path)

    logger.info("Checking whether each document file exists or not...")
    file_name: str
    for file_name in tqdm(file_names):
        expected_doc_path: str = os.path.join("./docs/en/", file_name)
        assert os.path.exists(
            expected_doc_path
        ), f"References section's document does not exist: {file_name}"
    return file_names


_DOC_DOMAIN: str = "https://simon-ritchie.github.io/apysc/"


def _extract_file_names(*, dir_path: str = "./apysc/") -> List[str]:
    """
    Extract file names from the apysc package modules.

    Parameters
    ----------
    dir_path : str, default './apysc'
        A directory path to search modules recursively.

    Returns
    -------
    file_names : List[str]
        Extracted file names.
    """
    file_names: List[str] = []

    logger.info("Loading each module...")
    module_paths: List[str] = module_util.get_module_paths_recursively(
        dir_path=dir_path
    )

    logger.info("Extracting references sections URLs...")
    for module_path in tqdm(module_paths):
        try:
            module: ModuleType = module_util.read_target_path_module(
                module_path=module_path
            )
        except Exception:
            continue
        docstrings: List[str] = docstring_util.extract_docstrings_from_module(
            module=module
        )
        for docstring in docstrings:
            references: List[
                Reference
            ] = docstring_util.extract_reference_values_from_docstring(
                docstring=docstring
            )
            for reference in references:
                if not reference.url.startswith(_DOC_DOMAIN):
                    continue
                if not reference.url.endswith(".html"):
                    continue
                _assert_url_contains_language_path(url=reference.url)
                file_name: str = reference.url.split("/")[-1]
                file_names.append(file_name)
    file_names = list(set(file_names))
    return file_names


def _assert_url_contains_language_path(*, url: str) -> None:
    """
    Assert whether a specified URL contains the language path (en).

    Parameters
    ----------
    url : str
        A target URL to check.

    Raises
    ------
    AssertionError
        If a specified URL does not contain the language path.
    """
    language_path: str = url.split("/")[-2]
    assert language_path == "en", url


if __name__ == "__main__":
    _main()
