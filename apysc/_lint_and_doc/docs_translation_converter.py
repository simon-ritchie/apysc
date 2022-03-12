"""This module is for the translation conversion
of the documents.
"""

import os
import re
from typing import Dict
from typing import List
from typing import Match
from typing import Optional
from typing import Pattern
from typing import Union

from apysc._lint_and_doc.docs_lang import Lang


class _TranslationMappingNotFound(Exception):
    pass


_GITHUB_ISSUE_URL: str = 'https://github.com/simon-ritchie/apysc/issues'

_EACH_LANG_HEADING_INFO_FORMAT: Dict[Lang, str] = {
    Lang.JP:
    '<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプト'
    'によって出力・同期されています。内容が怪しそうな場合は'
    f'<a href="{_GITHUB_ISSUE_URL}" target="_blank">GitHubに'
    'issue</a>を追加したり[英語の原文]({source_doc_basename})の'
    '確認をお願いします。</span>',
}

_EACH_LANG_API_INTERFACE_SIGNATURE_MAPPING: Dict[Lang, str] = {
    Lang.JP: 'インターフェイスの構造',
}

_API_SIGNATURE_PATTERN: Pattern = re.compile(
    pattern=(
        r'^\*\*\[Interface signature\]\*\*'
        r'(?P<tail_str>.*?)$'
    ))


def apply_translation_to_doc(
        *, md_file_path: str, lang: Lang) -> str:
    """
    Apply a translation mapping to a specified markdown
    document. This interface saves a translated file
    with a file name with a language suffix (e.g.,
    jp_your_doc.md).

    Parameters
    ----------
    md_file_path : str
        A source markdown file path.
    lang : Lang
        A target language setting.

    Returns
    -------
    translated_file_path : str
        A translated document file path.
    """
    from apysc._file import file_util
    from apysc._lint_and_doc import translation_mapping_utils
    from apysc._lint_and_doc.document_text_split_util import BodyText
    from apysc._lint_and_doc.document_text_split_util import CodeBlock
    from apysc._lint_and_doc.document_text_split_util import Heading
    from apysc._lint_and_doc.document_text_split_util import \
        split_markdown_document
    markdown: str = file_util.read_txt(file_path=md_file_path)
    splitted_values: List[Union[Heading, BodyText, CodeBlock]] = \
        split_markdown_document(markdown_txt=markdown)
    mapping_data: Dict[str, str] = translation_mapping_utils.\
        read_mapping_data(src_doc_file_path=md_file_path, lang=lang)
    keys: List[str] = translation_mapping_utils.\
        convert_splitted_values_to_keys(splitted_values=splitted_values)
    keys = translation_mapping_utils.remove_empty_keys(keys=keys)
    translated_doc: str = ''
    translated_doc = _add_heading_info_if_exists(
        translated_doc=translated_doc, lang=lang,
        md_file_path=md_file_path)
    for key in keys:
        key_: str = translation_mapping_utils.\
            remove_escaping_from_key_or_value(key_or_val=key)

        if translation_mapping_utils.is_translation_skipping_key(key=key_):
            continue

        if translated_doc != '':
            translated_doc += '\n\n'

        is_mapping_unnecessary_key: bool = translation_mapping_utils.\
            is_mapping_unnecessary_key(key=key_)
        if is_mapping_unnecessary_key:
            key_ = _apply_mapping_if_translated_str_is_api_sig(
                translated_str=key_,
                lang=lang)
            translated_doc += key_
            continue

        translated_str: str = mapping_data.get(key_, '')
        translated_doc += translated_str
        _validate_translated_str_is_not_blank(
            translated_str=translated_str, key=key,
            md_file_path=md_file_path)
        _validate_sharp_heading_symbol_num_are_same(
            translated_str=translated_str, key=key,
            md_file_path=md_file_path)

    translated_file_path: str = translation_mapping_utils.\
        get_translated_file_path_from_src_path(
            source_doc_path=md_file_path, lang=lang)
    file_util.save_plain_txt(
        txt=translated_doc, file_path=translated_file_path)

    return translated_file_path


class _InvalidHeadingSharpSymbolNumber(Exception):
    pass


def _validate_sharp_heading_symbol_num_are_same(
        *, translated_str: str, key: str,
        md_file_path: str) -> None:
    """
    Validate whether a sharp heading symbol of source and
    translated string are the same.

    Parameters
    ----------
    translated_str : str
        A translated string.
    key : str
        A key (source) string.
    md_file_path : str
        A source markdown file path.

    Raises
    ------
    _InvalidHeadingSharpSymbolNumber
        The symbol number is different for a specified translated
        string and a source string's sharp symbol heading.
    """
    translated_str_sharp_symbol_num: int = _get_sharp_heading_symbol_num(
        target_str=translated_str)
    key_str_sharp_symbol_num: int = _get_sharp_heading_symbol_num(
        target_str=key)
    if translated_str_sharp_symbol_num == key_str_sharp_symbol_num:
        return
    raise _InvalidHeadingSharpSymbolNumber(
        'There is a difference between source document and '
        'translated document\'s sharp heading symbol number.'
        f'\n\nSource string: {key}'
        f'\nTranslated string: {translated_str}'
        f'\nSource document path: {md_file_path}')


def _get_sharp_heading_symbol_num(*, target_str: str) -> int:
    """
    Get a sharp heading symbol number from a specified string.

    Parameters
    ----------
    target_str : str
        A target string to check.

    Returns
    -------
    sharp_symbol_num : int
        - A sharp heading symbol number.
    """
    sharp_symbol_num: int = 0
    for char in target_str:
        if char != '#':
            break
        sharp_symbol_num += 1
    return sharp_symbol_num


def _apply_mapping_if_translated_str_is_api_sig(
        *, translated_str: str, lang: Lang) -> str:
    """
    Apply an API signature translation mapping if a specified
    translated string is a signature string.

    Parameters
    ----------
    translated_str : str
        A target tlanslated string.
    lang : Lang
        A target language.

    Returns
    -------
    translated_str : str
        An applied string. This interface returns an argument
        value if a specified translated string is not a signature
        string.
    """
    sig_label_mapping: str = _EACH_LANG_API_INTERFACE_SIGNATURE_MAPPING.get(
        lang, '')
    if sig_label_mapping == '':
        return translated_str
    match: Optional[Match] = _API_SIGNATURE_PATTERN.search(
        string=translated_str)
    if match is None:
        return translated_str
    translated_str = _API_SIGNATURE_PATTERN.sub(
        repl=rf'**[{sig_label_mapping}]**\g<tail_str>',
        string=translated_str, count=1)
    return translated_str


def _add_heading_info_if_exists(
        *, translated_doc: str, lang: Lang,
        md_file_path: str) -> str:
    """
    Add a target language's heading information text
    to a specified translated text.

    Parameters
    ----------
    translated_doc : str
        A target translated document's text.
    lang : Lang
        A target language.
    md_file_path : str
        A target source document path.

    Returns
    -------
    translated_doc : str
        A result translated document's text.
        This interface directly returns argument value
        if there is no heading information setting.
    """
    heading_info_format: str = _EACH_LANG_HEADING_INFO_FORMAT.get(
        lang, '')
    if heading_info_format == '':
        return translated_doc
    basename: str = os.path.basename(md_file_path)
    heading_info_format = heading_info_format.format(
        source_doc_basename=basename,
    )
    translated_doc += heading_info_format
    return translated_doc


def _validate_translated_str_is_not_blank(
        *, translated_str: str, key: str,
        md_file_path: str) -> None:
    """
    Validate whether a translated string is not a blank string.

    Parameters
    ----------
    translated_str : str
        A target translated string.
    key : str
        A target key string (original source text).
    md_file_path : str
        A source markdown file path.

    Raises
    ------
    _TranslationMappingNotFound
        If a specified translated string is a blank string.
    """
    if translated_str != '':
        return
    raise _TranslationMappingNotFound(
        'There is no translation mapping.'
        f'\nOriginal source text: {key}'
        f'\nSource document path: {md_file_path}')
