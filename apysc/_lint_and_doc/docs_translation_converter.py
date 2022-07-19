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


_GITHUB_ISSUE_URL: str = "https://github.com/simon-ritchie/apysc/issues"

_EACH_LANG_HEADING_INFO_FORMAT: Dict[Lang, str] = {
    Lang.JP: '<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプト'
    "によって出力・同期されています。内容が怪しそうな場合は"
    f'<a href="{_GITHUB_ISSUE_URL}" target="_blank">GitHubに'
    "issue</a>を追加したり[英語の原文]({source_doc_path})の"
    "確認をお願いします。</span>",
}

_EACH_LANG_API_INTERFACE_SIGNATURE_MAPPING: Dict[Lang, str] = {
    Lang.JP: "インターフェイスの構造",
}

_API_SIGNATURE_PATTERN: Pattern = re.compile(
    pattern=(r"^\*\*\[Interface signature\]\*\*" r"(?P<tail_str>.*?)$")
)


def apply_translation_to_doc(*, md_file_path: str, lang: Lang) -> str:
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
    from apysc._lint_and_doc.document_text_split_util import split_markdown_document

    markdown: str = file_util.read_txt(file_path=md_file_path)
    splitted_values: List[
        Union[Heading, BodyText, CodeBlock]
    ] = split_markdown_document(markdown_txt=markdown)
    mapping_data: Dict[str, str] = translation_mapping_utils.read_mapping_data(
        src_doc_file_path=md_file_path, lang=lang
    )
    keys: List[str] = translation_mapping_utils.convert_splitted_values_to_keys(
        splitted_values=splitted_values
    )
    keys = translation_mapping_utils.remove_empty_keys(keys=keys)
    translated_doc: str = ""
    translated_doc = _add_heading_info_if_exists(
        translated_doc=translated_doc, lang=lang, md_file_path=md_file_path
    )
    for key in keys:
        key_: str = translation_mapping_utils.remove_escaping_from_key_or_value(
            key_or_val=key
        )
        if translation_mapping_utils.is_translation_skipping_key(key=key_):
            continue
        translated_doc = _append_double_line_breaks_if_txt_is_not_blank(
            txt=translated_doc
        )

        is_mapping_unnecessary_key: bool = (
            translation_mapping_utils.is_mapping_unnecessary_key(key=key_)
        )
        if is_mapping_unnecessary_key:
            key_ = _apply_mapping_if_translated_str_is_api_sig(
                translated_str=key_, lang=lang
            )
            translated_doc += key_
            continue

        translated_str: str = mapping_data.get(key_, "")
        translated_doc += translated_str
        _validate_translated_str_is_not_blank(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )
        _validate_sharp_heading_symbol_num_are_same(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )
        _validate_first_spaces_nums_are_same(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )
        _validate_markdown_list_hyphen_symbols_are_same(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )
        _validate_tail_hr_tag(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )
        _validate_first_br_tags_and_list_symbols_are_same(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )
        _validate_first_full_width_list_symbols_are_same(
            translated_str=translated_str, key=key, md_file_path=md_file_path
        )

    translated_file_path: str = (
        translation_mapping_utils.get_translated_file_path_from_src_path(
            source_doc_path=md_file_path, lang=lang
        )
    )
    translated_doc = _remove_unnecessary_line_break_between_list(
        translated_doc=translated_doc
    )
    translated_doc = _remove_line_break_between_api_docs_list_br_tag(
        translated_doc=translated_doc
    )
    file_util.save_plain_txt(txt=translated_doc, file_path=translated_file_path)

    return translated_file_path


def _append_double_line_breaks_if_txt_is_not_blank(*, txt: str) -> str:
    """
    Append double line breaks if a specified text is not
    a blank string.

    Parameters
    ----------
    txt : str
        A target text.

    Returns
    -------
    txt : str
        A result text.
    """
    if txt != "":
        txt += "\n\n"
    return txt


class _FirstFullWidthListSymbolsAreNotSame(Exception):
    pass


def _validate_first_full_width_list_symbols_are_same(
    *, translated_str: str, key: str, md_file_path: str
) -> None:
    """
    Validate whether specified first full-width list symbols
    are the same or not.

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
    _FirstFullWidthListSymbolsAreNotSame
        If specified strings' first full-width list symbols
        are not the same.
    """
    if not key.strip().startswith("・"):
        return
    if translated_str.strip().startswith("・"):
        return
    raise _FirstFullWidthListSymbolsAreNotSame(
        "Specified strings' first full-width list symbols "
        "are not the same:"
        f"\nSource string: {key}"
        f"\nTranslated string: {translated_str}"
        f"\nSource document path: {md_file_path}"
    )


class _BrTagsAndListSymbolsAreNotSame(Exception):
    pass


def _validate_first_br_tags_and_list_symbols_are_same(
    *, translated_str: str, key: str, md_file_path: str
) -> None:
    """
    Validate whether a string's first break tags and list
    symbols（・） are the same between a source string and
    a key string.

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
    _BrTagsAndListSymbolsAreNotSame
        This interface makes an exception if specified strings'
        first break tags and list symbols are not the same.
    """
    if not key.startswith("<br> ・"):
        return
    if translated_str.startswith("<br> ・"):
        return
    raise _BrTagsAndListSymbolsAreNotSame(
        "First break tags and list symbols are not the same:"
        f"\nSource string: {key}"
        f"\nTranslated string: {translated_str}"
        f"\nSource document path: {md_file_path}"
    )


def _remove_line_break_between_api_docs_list_br_tag(*, translated_doc: str) -> str:
    """
    Remove a line break between an API docs list's break tag.

    Parameters
    ----------
    translated_doc : str
        A translated string.

    Returns
    -------
    translated_doc : str
        A result string.
    """
    while "\n<br> ・" in translated_doc:
        translated_doc = translated_doc.replace("\n<br> ・", "<br> ・")
    return translated_doc


class _InvalidTailsHrTag(Exception):
    pass


def _validate_tail_hr_tag(*, translated_str: str, key: str, md_file_path: str) -> None:
    """
    Validate whether a tail of translated string's `<hr>`
    tag is valid or not.

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
    _InvalidTailsHrTag
        This interface makes an exception if a tail of
        a source text is the `<hr>` tag and a translated
        string is not.
    """
    if not key.endswith("<hr>"):
        return
    if translated_str.endswith("<hr>"):
        return
    raise _InvalidTailsHrTag(
        "End of a translated string is not the `<hr>` tag."
        f"\nSource string: {key}"
        f"\nTranslated string: {translated_str}"
        f"\nSource document path: {md_file_path}"
    )


class _MarkdownListHyphenSymbolsAreNotSame(Exception):
    pass


def _validate_markdown_list_hyphen_symbols_are_same(
    *, translated_str: str, key: str, md_file_path: str
) -> None:
    """
    Validate whether markdown's first hyphen symbols are the
    same or not.

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
    _MarkdownListHyphenSymbolsAreNotSame
        This interface makes an exception if markdown's first
        hyphen symbols are not the same.
    """
    if not key.strip().startswith("- "):
        return
    if translated_str.strip().startswith("- "):
        return
    raise _MarkdownListHyphenSymbolsAreNotSame(
        "First character of list's hyphen symbols are not the same."
        f"\nSource string: {key}"
        f"\nTranslated string: {translated_str}"
        f"\nSource document path: {md_file_path}"
    )


class _FirstSpacesNumAreDifferent(Exception):
    pass


def _validate_first_spaces_nums_are_same(
    *, translated_str: str, key: str, md_file_path: str
) -> None:
    """
    Validate whether first spaces numbers are the same between
    a source markdown and a translated markdown text.

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
    _FirstSpacesNumAreDifferent
        This interface raises an exception if first spaces
        numbers are different.
    """
    translated_str_first_spaces_num: int = _get_first_spaces_num(txt=translated_str)
    key_first_spaces_num: int = _get_first_spaces_num(txt=key)
    if translated_str_first_spaces_num == key_first_spaces_num:
        return
    raise _FirstSpacesNumAreDifferent(
        "First spaces numbers are not the same between a "
        "source markdown and a translated markdown text."
        f"\nSource string: {key}"
        f"\nTranslated string: {translated_str}"
        f"\nSource document path: {md_file_path}"
    )


def _get_first_spaces_num(*, txt: str) -> int:
    """
    Get a first spaces number of a specified string.

    Parameters
    ----------
    txt : str
        A target string.

    Returns
    -------
    first_spaces_num : int
        A first spaces number.
    """
    first_spaces_num: int = 0
    for char in txt:
        if char != " ":
            break
        first_spaces_num += 1
    return first_spaces_num


def _remove_unnecessary_line_break_between_list(*, translated_doc: str) -> str:
    """
    Remove an unnecessary line break between each markdown's list.

    Parameters
    ----------
    translated_doc : str
        A target translated document to remove an unnecessary line break.

    Returns
    -------
    result_translated_doc : str
        A target translated document to remove an unnecessary
        line break.
    """
    result_translated_doc: str = re.sub(
        pattern=(r"(?P<prev_part>\s*?- .+?$\n)\n(?P<after_part>\s*?- )"),
        repl=r"\g<prev_part>\g<after_part>",
        string=translated_doc,
        flags=re.MULTILINE,
    )
    return result_translated_doc


class _InvalidHeadingSharpSymbolNumber(Exception):
    pass


def _validate_sharp_heading_symbol_num_are_same(
    *, translated_str: str, key: str, md_file_path: str
) -> None:
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
        target_str=translated_str
    )
    key_str_sharp_symbol_num: int = _get_sharp_heading_symbol_num(target_str=key)
    if translated_str_sharp_symbol_num == key_str_sharp_symbol_num:
        return
    raise _InvalidHeadingSharpSymbolNumber(
        "There is a difference between source document and "
        "translated document's sharp heading symbol number."
        f"\n\nSource string: {key}"
        f"\nTranslated string: {translated_str}"
        f"\nSource document path: {md_file_path}"
    )


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
        if char != "#":
            break
        sharp_symbol_num += 1
    return sharp_symbol_num


def _apply_mapping_if_translated_str_is_api_sig(
    *, translated_str: str, lang: Lang
) -> str:
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
    sig_label_mapping: str = _EACH_LANG_API_INTERFACE_SIGNATURE_MAPPING.get(lang, "")
    if sig_label_mapping == "":
        return translated_str
    match: Optional[Match] = _API_SIGNATURE_PATTERN.search(string=translated_str)
    if match is None:
        return translated_str
    translated_str = _API_SIGNATURE_PATTERN.sub(
        repl=rf"**[{sig_label_mapping}]**\g<tail_str>", string=translated_str, count=1
    )
    return translated_str


def _add_heading_info_if_exists(
    *, translated_doc: str, lang: Lang, md_file_path: str
) -> str:
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
    heading_info_format: str = _EACH_LANG_HEADING_INFO_FORMAT.get(lang, "")
    if heading_info_format == "":
        return translated_doc
    source_doc_path: str = os.path.basename(md_file_path)
    source_doc_path = source_doc_path.replace(".md", ".html")
    source_doc_path = f"https://simon-ritchie.github.io/apysc/en/{source_doc_path}"
    heading_info_format = heading_info_format.format(
        source_doc_path=source_doc_path,
    )
    translated_doc += heading_info_format
    return translated_doc


def _validate_translated_str_is_not_blank(
    *, translated_str: str, key: str, md_file_path: str
) -> None:
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
    if translated_str != "":
        return
    raise _TranslationMappingNotFound(
        "There is no translation mapping."
        f"\nOriginal source text: {key}"
        f"\nSource document path: {md_file_path}"
    )
