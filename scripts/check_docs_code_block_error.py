"""This module is for checking whether there is no error in
each document's code block execution result.

Command examples:
$ python scripts/check_docs_code_block_error.py --alphabets_group abcdef
"""

import os
import sys
from argparse import ArgumentParser
from argparse import Namespace
from logging import Logger
from typing import List

from tqdm import tqdm
from typing_extensions import TypedDict

sys.path.append("./")

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


class _CommandOptions(TypedDict):
    alphabets_group: List[str]


def _main() -> None:
    """Entry point of this command."""
    command_options: _CommandOptions = _get_command_options()
    document_file_paths: List[str] = _get_target_document_file_paths(
        alphabets_group=command_options["alphabets_group"]
    )
    document_file_path: str
    for document_file_path in tqdm(document_file_paths):
        _run_document_code_blocks(document_file_path=document_file_path)


class _CodeBlockError(Exception):
    pass


def _run_document_code_blocks(*, document_file_path: str) -> None:
    """
    Run a specified document's code blocks and check whether
    there is no exception.

    Parameters
    ----------
    document_file_path : str
        A target document file path.

    Raises
    ------
    _CodeBlockError
        If a code block raises an exception.
    """
    from apysc._file.module_util import save_tmp_module_and_run_script
    from scripts.build_docs import get_runnable_scripts_in_md_code_blocks

    logger.info(
        f"Checking the {os.path.basename(document_file_path)} document's "
        "code blocks..."
    )
    code_blocks: List[str] = get_runnable_scripts_in_md_code_blocks(
        md_file_path=document_file_path
    )
    for code_block in code_blocks:
        stdout: str = save_tmp_module_and_run_script(script=code_block)
        if "Traceback" not in stdout:
            continue
        raise _CodeBlockError(
            "There is an exception in the code block execution."
            f"\nDocument file path: {document_file_path}"
            f"\nCode block:\n\n{code_block}"
            f"\n\nStdout:\n\n{stdout}"
        )


def _get_target_document_file_paths(*, alphabets_group: List[str]) -> List[str]:
    """
    Get target document file paths.

    Notes
    -----
    Translated documents do not become a target document
    since they have the same code block.

    Parameters
    ----------
    alphabets_group : str
        A target alphabets group list.

    Returns
    -------
    document_file_paths : List[str]
        Target document file paths.
    """
    file_names: List[str] = os.listdir("./docs_src/source/")
    document_file_paths: List[str] = []
    for file_name in file_names:
        if not file_name.endswith(".md"):
            continue
        file_name_first_lower_char: str = file_name[0].lower()
        if file_name_first_lower_char not in alphabets_group:
            continue
        if _target_file_is_translated_document(file_name=file_name):
            continue
        file_path: str = os.path.join("./docs_src/source/", file_name)
        document_file_paths.append(file_path)
    return document_file_paths


def _target_file_is_translated_document(*, file_name: str) -> bool:
    """
    Get a boolean indicating whether a scpecified file name's
    document is a translated document or not.

    Parameters
    ----------
    file_name : str
        A target document file name.

    Returns
    -------
    result : bool
        This interface returns True if a specified file name is
        a translated document.
    """
    from apysc._lint_and_doc.docs_lang import Lang

    for lang in Lang:
        if file_name.startswith(f"{lang.value}_"):
            return True
    return False


def _get_command_options() -> _CommandOptions:
    """
    Get a command-line options.

    Returns
    -------
    options : _CommandOptions
        Command argument values and options.
    """
    from scripts import alphabets_group_param

    parser: ArgumentParser = ArgumentParser(
        description="The command for checking whether there is no "
        "error in each document's code block execution result."
    )
    alphabets_group_param.add_alphabets_group_arg_to_parser(parser=parser)
    args: Namespace = parser.parse_args()
    alphabets_group: List[str] = alphabets_group_param.split_alphabets_group_str(
        alphabets_group_str=args.alphabets_group
    )
    options: _CommandOptions = {
        "alphabets_group": alphabets_group,
    }
    return options


if __name__ == "__main__":
    _main()
