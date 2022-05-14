"""This module is for alphabets group's parameter-related
interfaces and definitions.
"""


from argparse import ArgumentParser
from string import ascii_lowercase
from typing import List


def add_alphabets_group_arg_to_parser(
        *, parser: ArgumentParser) -> None:
    """
    Add the alphabets group argument to a command parser.

    Parameters
    ----------
    parser : _type_
        A target command parser.
    """
    parser.add_argument(
        '-a',
        '--alphabets_group',
        action='store',
        type=str,
        default='',
        help='An alphabets group string. This command uses this argument '
        'to split target files or directory. For instance, '
        'if `abc` is specified, '
        'the file or directory that a name starts with `a` or `b` or `c` '
        'becomes target one.',
    )


def split_alphabets_group_str(
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
