"""This module is for adding document translations mapping
dictionary's blank data.
"""

import os
import re
from typing import Dict
from typing import List
from typing import Match
from typing import Optional
from typing import Pattern
from typing import Union

from apysc._lint_and_doc import document_text_split_util
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.docstring_util import DOCSTRING_PATH_COMMENT_PATTERN
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME
from apysc._lint_and_doc.translation_mapping_utils import \
    get_mapping_module_path
from apysc._lint_and_doc.translation_mapping_utils import read_mapping_data

_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]

_HR_TAG_PATTERN: str = r'^<hr>$'

_INTERFACE_SIGNATURE_PATTERN: str = (
    r'\*\*\[Interface signature\]\*\* .*?<hr>'
)

_CODE_BLOCK_IFRAME_PATTERN: str = (
    r'<iframe src="static.*?index\.html".*?></iframe>'
)

_API_DOCS_AUTO_GEN_TXT_PATTERN: str = (
    r'^<span class="inconspicuous-txt">Note: the document build '
    r'script generates and updates this API document section '
    r'automatically\. Maybe this section is duplicated '
    r'compared with previous sections\.</span>$'
)

_SKIPPING_PATTERNS: List[Pattern] = [
    re.compile(pattern=DOCSTRING_PATH_COMMENT_PATTERN),
]

_MAPPING_UNNECESSARY_PATTERNS: List[Pattern] = [
    re.compile(pattern=_HR_TAG_PATTERN,),
    re.compile(pattern=_INTERFACE_SIGNATURE_PATTERN),
    re.compile(pattern=_CODE_BLOCK_IFRAME_PATTERN),
    re.compile(pattern=_API_DOCS_AUTO_GEN_TXT_PATTERN),
]


def add_mapping_blank_data(*, lang: Lang) -> None:
    """
    Add a mapping's blank data of document translations.

    Parameters
    ----------
    lang : Lang
        A target translation language.
    """
    from apysc._file import file_util
    src_docs_file_paths: List[str] = _get_src_docs_file_paths()
    hash_type: HashType = _get_hash_type_from_lang(lang=lang)
    src_docs_file_paths = lint_and_doc_hash_util.\
        remove_not_updated_file_paths(
            file_paths=src_docs_file_paths,
            hash_type=hash_type)
    for src_doc_file_path in src_docs_file_paths:
        markdown_txt: str = file_util.read_txt(file_path=src_doc_file_path)
        splitted_values: _SplittedVals = document_text_split_util.\
            split_markdown_document(markdown_txt=markdown_txt)
        keys: List[str] = _convert_splitted_values_to_keys(
            splitted_values=splitted_values)
        mappings: List[Dict[str, str]] = _make_mappings_from_keys(
            keys=keys, src_doc_file_path=src_doc_file_path,
            lang=lang)
        _save_mapping_data(
            mappings=mappings, src_doc_file_path=src_doc_file_path,
            lang=lang)
    lint_and_doc_hash_util.save_target_files_hash(
        file_paths=src_docs_file_paths, hash_type=hash_type)


def _get_hash_type_from_lang(*, lang: Lang) -> HashType:
    """
    Get a hash type from a specified language type.

    Parameters
    ----------
    lang : Lang
        A target translation language.

    Returns
    -------
    hash_type : HashType
        A target hash type.

    Raises
    ------
    ValueError
        If there is no implementation of a specified language
        type's branch condition.
    """
    if lang == Lang.JP:
        return HashType.TRANSLATION_MAPPING_JP
    raise ValueError(
        'There is no implementation of a specified language type\'s '
        'branch condition. Please add a necessary branch condition: '
        f'{lang}')


def _save_mapping_data(
        *, mappings: List[Dict[str, str]],
        src_doc_file_path: str,
        lang: Lang) -> None:
    """
    Save mapping data module with specified mappings data.

    Parameters
    ----------
    mappings : list of dict
        Target mappings data to save.
    src_doc_file_path : str
        A target source document's file path.
    lang : Lang
        A target translation language.
    """
    from apysc._file import file_util
    basename: str = os.path.basename(src_doc_file_path)
    module_str: str = (
        f'"""This module is for the translation mapping data '
        'of the\nfollowing document:'
        f'\n\nDocument file: {basename}'
        f'\nLanguage: {lang.value}'
        '\n"""'
        '\n\nfrom typing import Dict'
        f'\n\n{MAPPING_CONST_NAME}: Dict[str, str] = {{'
    )
    for mapping in mappings:
        key: str = list(mapping.keys())[0]
        value: str = list(mapping.values())[0]
        module_str += f"\n\n    '{key}':"
        if len(key) >= 70:
            module_str += '  # noqa'
        module_str += f"\n    '{value}',"
        if len(value) >= 70:
            module_str += '  # noqa'
    module_str += '\n\n}\n'
    module_path: str = get_mapping_module_path(
        src_doc_file_path=src_doc_file_path, lang=lang)
    file_util.save_plain_txt(txt=module_str, file_path=module_path)


def _make_mappings_from_keys(
        *, keys: List[str],
        src_doc_file_path: str,
        lang: Lang) -> List[Dict[str, str]]:
    """
    Make mapping dictionary values from specified key values.

    Parameters
    ----------
    keys : list of str
        Target dictionary key values.
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.

    Returns
    -------
    mappings : list of dict
        Created mapping dictionary values. A dictionary
        value becomes a blank string if it is a new mapping value.
    """
    already_saved_mapping: Dict[str, str] = read_mapping_data(
        src_doc_file_path=src_doc_file_path, lang=lang)
    mappings: List[Dict[str, str]] = []
    for key in keys:
        key_: str = key.replace('\\\\', '\\')
        key_ = key_.replace("\\'", "'")
        key_ = key_.replace('\\n', '\n')
        value: str = already_saved_mapping.get(key_, '')
        value = _escape_key_or_value(key_or_val=value)
        value = _set_fixed_translation_value_if_exists(
            key=key_, value=value)
        value = _set_same_value_if_code_block_mapping_is_blank(
            key=key, value=value)
        value = _convert_link_list_by_lang(
            key=key, value=value, lang=lang)
        mappings.append({key: value})
    return mappings


_LINK_PATTERN: Pattern = re.compile(
    pattern=(
        r'(.*?\[.+?\])'
        r'\((.+?\.md)\)'
        r'(?P<after_txt>.*?)'
    ),
    flags=re.MULTILINE)


def _convert_link_list_by_lang(
        *, key: str, value: str, lang: Lang) -> str:
    """
    Convert a link list value by a specified language if a key's
    value is a link list.

    Parameters
    ----------
    key : str
        A target key string (source English string).
    value : str
        A target value string.
    lang : Lang
        A target translation language.

    Returns
    -------
    value : str
        A converted value. This interface skips the
        conversion if a specified key's value is not
        a link list.
    """
    if not key.startswith('- '):
        return value
    match: Optional[Match] = _LINK_PATTERN.search(string=key)
    if match is None:
        return value
    value = ''
    while match is not None:
        prev_txt: str = match.group(1)
        doc_path: str = match.group(2)
        basename: str = os.path.basename(doc_path)
        basename = f'{lang.value}_{basename}'
        dir_path = os.path.dirname(doc_path)
        doc_path = os.path.join(dir_path, basename)
        if value != '':
            value += '\n'
        value += f'{prev_txt}({doc_path})'

        key = _LINK_PATTERN.sub(
            repl=r'\g<after_txt>',
            string=key, count=1)
        match = _LINK_PATTERN.search(string=key)
    value = _escape_key_or_value(key_or_val=value)
    return value


def _set_same_value_if_code_block_mapping_is_blank(
        *, key: str, value: str) -> str:
    """
    Set the same code-block value if a specified value
    is a blank string and a key's value is a code block.

    Parameters
    ----------
    key : str
        A target key string (source English string).
    value : str
        A target value string.

    Returns
    -------
    value : str
        A result value. If an argument value is not a blank
        string, this interface returns it directly.
        If a key's value is not a code block, this interface
        also returns an argument value directly.
    """
    if value != '':
        return value
    if not key.startswith('```'):
        return value
    return key


def _set_fixed_translation_value_if_exists(
        *, key: str, value: str) -> str:
    """
    Set a fixed translation value if its mapping setting exists.

    Parameters
    ----------
    key : str
        A target translation key.
    value : str
        A current translation value.

    Returns
    -------
    fixed_value : str
        A fixed translation value. If there is no fixed
        translation mapping setting, this interface directly
        returns an argument's value.
    """
    from apysc._lint_and_doc.fixed_translation_mapping import data_model
    fixed_value: str = data_model.get_fixed_translation_str_if_exists(
        key=key, lang=Lang.JP)
    if fixed_value == '':
        return value
    return fixed_value


def _convert_splitted_values_to_keys(
        *, splitted_values: _SplittedVals) -> List[str]:
    """
    Convert specified splitted values to dictionary's key
    strings.

    Parameters
    ----------
    splitted_values : List of Heading, BodyText and CodeBlock
        Target splitted values.

    Returns
    -------
    keys : list of str
        Converted strings.
    """
    keys: List[str] = []
    for splitted_value in splitted_values:
        is_body_text: bool = False
        key: str = ''
        if isinstance(splitted_value, Heading):
            key = splitted_value.overall_text
        if isinstance(splitted_value, BodyText):
            is_body_text = True
            key = splitted_value.text
        if isinstance(splitted_value, CodeBlock):
            key = splitted_value.overall_code_block
        key = _escape_key_or_value(key_or_val=key)
        if not is_body_text:
            keys.append(key)
        else:
            _append_body_text_keys_to_list(key=key, keys=keys)
    keys = _remove_skipping_pattern_keys_from_list(keys=keys)
    return keys


def _escape_key_or_value(*, key_or_val: str) -> str:
    """
    Escape a mapping key or value to save.

    Parameters
    ----------
    key_or_val : str
        A target key or value.

    Returns
    -------
    key_or_val : str
        An escaped key or value string.
    """
    key_or_val = key_or_val.replace('\\', '\\\\')
    key_or_val = key_or_val.replace("'", "\\'")
    key_or_val = key_or_val.replace('\n', '\\n')
    key_or_val = key_or_val.replace('\\\\n', '\\n')
    return key_or_val


def _remove_skipping_pattern_keys_from_list(
        *, keys: List[str]) -> List[str]:
    """
    Remove skipping pattern matching keys from a specified list.

    Parameters
    ----------
    keys : list of str
        A target key's list.

    Returns
    -------
    result_keys : list of str
        An after removing key's list.
    """
    result_keys: List[str] = []
    patterns: List[Pattern] = [
        *_SKIPPING_PATTERNS, *_MAPPING_UNNECESSARY_PATTERNS]
    for key in keys:
        is_pattern_matching: bool = False
        for pattern in patterns:
            match: Optional[Match] = pattern.search(string=key)
            if match is not None:
                is_pattern_matching = True
                break
        if is_pattern_matching:
            continue
        result_keys.append(key)
    return result_keys


def _append_body_text_keys_to_list(
        *, key: str, keys: List[str]) -> None:
    """
    Append document's body text keys to a specified key's list.

    Parameters
    ----------
    key : str
        A target key string. This interface splits its string
        if there are two consecutive line breaks.
    keys : list of str
        A key's list to append.
    """
    splitted_keys: List[str] = key.split('\\n\\n')
    for key_ in splitted_keys:
        keys.append(key_)


def _get_src_docs_file_paths() -> List[str]:
    """
    Get source documents file paths.

    Returns
    -------
    src_docs_file_paths : list of str
        Source documents file paths.
    """
    dir_path: str = './docs_src/source/'
    file_or_dir_names: List[str] = os.listdir(dir_path)
    src_docs_file_paths: List[str] = []
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if not os.path.isfile(file_or_dir_path):
            continue
        if not file_or_dir_path.endswith('.md'):
            continue
        if _is_translated_document(path=file_or_dir_path):
            continue
        src_docs_file_paths.append(file_or_dir_path)
    return src_docs_file_paths


def _is_translated_document(*, path: str) -> bool:
    """
    Get a boolean indicating whether a specified document path
    is a translated document or not.

    Parameters
    ----------
    path : str
        A target document path.

    Returns
    -------
    result : bool
        If a specified document path is a translated document,
        this interface returns True.
    """
    basename: str = os.path.basename(path)
    for lang in Lang:
        if basename.startswith(lang.value):
            return True
    return False
