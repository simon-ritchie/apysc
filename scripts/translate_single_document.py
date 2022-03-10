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
from apysc._lint_and_doc import docs_lang


class _CommandOptions(TypedDict):
    src: str
    lang: str


def _main() -> None:
    """
    Translate a specified single document file.
    """
    command_options: _CommandOptions = _get_command_options()
    _validate_src_option(src=command_options['src'])
    _validate_lang_option(lang=command_options['lang'])
    lang: Lang = docs_lang.get_lang_from_str_value(
        str_value=command_options['lang'])
    _delete_translation_mapping_hash(
        lang=lang, src_file_path=command_options['src'])
    pass


def _delete_translation_mapping_hash(
        *, lang: Lang, src_file_path: str) -> None:
    """
    Delete a specified source file's mapping hash file.

    Parameters
    ----------
    lang : Lang
        A target translation language.
    src_file_path : str
        A source file path.
    """
    from apysc._lint_and_doc import lint_and_doc_hash_util
    from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
    from apysc._lint_and_doc import translation_mapping_utils
    from apysc._file import file_util
    hash_type: HashType = translation_mapping_utils.get_hash_type_from_lang(
        lang=lang)
    hash_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=src_file_path, hash_type=hash_type)
    file_util.remove_file_if_exists(file_path=hash_path)


class _UndefinedLanguage(Exception):
    pass


def _validate_lang_option(*, lang: str) -> None:
    """
    Validate a specified language string.

    Parameters
    ----------
    lang : str
        A target language string to check.

    Raises
    ------
    _UndefinedLanguage
        If a specified language string is undefined,
        this interface raises an exception.
    """
    for lang_ in Lang:
        if lang == lang_.value:
            return
    raise _UndefinedLanguage(
        'A specified language string is undefined (currently '
        f'not supported): {lang}')


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
