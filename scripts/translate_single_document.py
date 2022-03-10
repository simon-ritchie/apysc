"""This module is for translation script of a single
document file.

Command examle:
$ python scripts/translate_single_document.py \
    --src docs_src/source/any_document.md \
    --lang jp
"""

from argparse import ArgumentParser
from argparse import Namespace
import os

from typing_extensions import TypedDict

from apysc._lint_and_doc.docs_lang import Lang


class _CommandOptions(TypedDict):
    src: str
    lang: str


def _main() -> None:
    """
    Translate a specified single document file.
    """
    command_options: _CommandOptions = _get_command_options()
    _validate_src_option(src=command_options['src'])
    pass


class _SourceFileNotFound(Exception):
    pass


class _SourceFileIsNotEnglish(Exception):
    pass


def _validate_src_option(*, src: str) -> None:
    """
    Validate a specified source file path option.

    Parameters
    ----------
    src : str
        A target source file path option to check.

    Raises
    ------
    _SourceFileNotFound
        If there is no such source file, this interface
        raises an exception.
    _SourceFileIsNotEnglish
        If a specified source file path is not an English
        document, this interface raises an exception.
    """
    if not os.path.isfile(src):
        raise _SourceFileNotFound(
            f'There is no such source file: {src}'
            '\nPlease check an -s or --src argument.')

    basename: str = os.path.basename(src)
    for lang in Lang:
        if not basename.startswith(f'{lang.value}_'):
            continue
        raise _SourceFileIsNotEnglish(
            'A specified source file path\'s basename is '
            f'not an English document: {src}')


def _get_command_options() -> _CommandOptions:
    """
    Get a command-line options.

    Returns
    -------
    options : _CommandOptions
        Command argument values and options.
    """
    parser: ArgumentParser = ArgumentParser(
        description='Translate a specified single document file.')

    parser.add_argument(
        '-s', '--src', action='store', type=str,
        help='Source document\'s file path (e.g., '
             'docs_src/source/sprite.md).')
    parser.add_argument(
        '-l', '--lang', action='store', type=str,
        help='A language of the translation (e.g., jp).')
    args: Namespace = parser.parse_args()
    options: _CommandOptions = {
        'src': args.src,
        'lang': args.lang,
    }
    return options


if __name__ == '__main__':
    _main()
