"""This module is for checking whether there is no error in
each document's code block execution result.

Command examples:
$ python scripts/check_docs_code_block_error --alphabets_group abcdef
"""

import sys
from logging import Logger
from typing import List
from argparse import ArgumentParser
from argparse import Namespace
from string import ascii_lowercase

from typing_extensions import TypedDict

sys.path.append('./')

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


class _CommandOptions(TypedDict):
    alphabets_group: List[str]


def _main() -> None:
    """Entry point of this command.
    """
    command_options: _CommandOptions = _get_command_options()
    pass


def _get_command_options() -> _CommandOptions:
    """
    Get a command-line options.

    Returns
    -------
    options : _CommandOptions
        Command argument values and options.
    """
    parser: ArgumentParser = ArgumentParser(
        description='The command for checking whether there is no '
        'error in each document\'s code block execution result.')
    parser.add_argument(
        '-a',
        '--alphabets_group',
        action='store',
        type=str,
        default='',
        help='An alphabets group string. This command uses this argument '
        'to split target documents. For instance, if `abc` is specified, '
        'the document that a file name starts with `a` or `b` or `c` '
        'becomes checking target.',
    )
    args: Namespace = parser.parse_args()
    alphabets_group: List[str] = _split_alphabets_group_str(
        alphabets_group_str=args.alphabets_group)
    pass


def _split_alphabets_group_str(
        *, alphabets_group_str: str) -> List[str]:
    """
    Split an alphabets group string to a list.

    Parameters
    ----------
    alphabets_group_str : str
        A target alphabets group string.

    Returns
    -------
    alphabets_group : List[str]
        A splitted alphabets' list.

    Raises
    ------
    ValueError
        - If a specified string is blank.
        - If a specified string contains non-alphabets characters.
        - If there is a duplicated alphabets in a specified string.
    """
    if alphabets_group_str == '':
        raise ValueError(
            'An `--alphabets_group` argument\' value cannot be blank.')
    alphabets_group: List[str] = []
    for alphabet in alphabets_group_str:
        alphabet = alphabet.lower()
        if alphabet not in ascii_lowercase:
            raise ValueError(
                'There is a non-alphabet character in a specified '
                f'`--alphabets_group` argument\'s value: {alphabet}')
        alphabets_group.append(alphabet)
    if len(alphabets_group) != len(set(alphabets_group)):
        raise ValueError(
            'There are duplicated alphabets in a specified '
            f'`--alphabets_group` argument\'s value: {alphabets_group}')
    return alphabets_group


if __name__ == '__main__':
    _main()
