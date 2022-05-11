"""This module is for alphabets group's parameter-related
interfaces and definitions.
"""


from typing import Any, Dict, List
from argparse import ArgumentParser
from argparse import Namespace


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
