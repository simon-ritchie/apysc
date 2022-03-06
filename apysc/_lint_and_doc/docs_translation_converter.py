"""This module is for the translation conversion
of the documents.
"""

from typing import Dict
from typing import List
from typing import Union

from apysc._lint_and_doc.docs_lang import Lang


class _TranslationMappingNotFound(Exception):
    pass


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
    translated_doc: str = ''
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
            translated_doc += key_
            continue

        translated_str: str = mapping_data.get(key_, '')
        translated_doc += translated_str
        _validate_translated_str_is_not_blank(
            translated_str=translated_str, key=key,
            md_file_path=md_file_path)

    translated_file_path: str = translation_mapping_utils.\
        get_translated_file_path_from_src_path(
            source_doc_path=md_file_path, lang=lang)
    file_util.save_plain_txt(
        txt=translated_doc, file_path=translated_file_path)

    return translated_file_path


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
