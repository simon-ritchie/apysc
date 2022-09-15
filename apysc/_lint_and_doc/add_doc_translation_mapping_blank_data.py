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
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_CONST_NAME
from apysc._lint_and_doc.translation_mapping_utils import MAPPING_UNNECESSARY_PATTERNS
from apysc._lint_and_doc.translation_mapping_utils import SKIPPING_PATTERNS
from apysc._lint_and_doc.translation_mapping_utils import (
    convert_splitted_values_to_keys,
)
from apysc._lint_and_doc.translation_mapping_utils import escape_key_or_value
from apysc._lint_and_doc.translation_mapping_utils import get_hash_type_from_lang
from apysc._lint_and_doc.translation_mapping_utils import get_mapping_module_path
from apysc._lint_and_doc.translation_mapping_utils import (
    get_translated_file_path_from_src_path,
)
from apysc._lint_and_doc.translation_mapping_utils import read_mapping_data
from apysc._lint_and_doc.translation_mapping_utils import remove_empty_keys
from apysc._lint_and_doc.translation_mapping_utils import (
    remove_escaping_from_key_or_value,
)

_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]

_NO_MAPPING_FIXED_STRINGS: List[str] = [
    "</details>",
    "<hr>",
    "- ValueError: ",
    "- Exception: ",
    "---",
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
    from apysc._lint_and_doc.fixed_translation_mapping import data_model

    is_fixed_mapping_updated: bool = data_model.is_fixed_mapping_updated(lang=lang)

    src_docs_file_paths: List[str] = _get_src_docs_file_paths()
    hash_type: HashType = get_hash_type_from_lang(lang=lang)
    if not is_fixed_mapping_updated:
        src_docs_file_paths = lint_and_doc_hash_util.remove_not_updated_file_paths(
            file_paths=src_docs_file_paths, hash_type=hash_type
        )
    for src_doc_file_path in src_docs_file_paths:
        markdown_txt: str = file_util.read_txt(file_path=src_doc_file_path)
        splitted_values: _SplittedVals = (
            document_text_split_util.split_markdown_document(markdown_txt=markdown_txt)
        )
        keys: List[str] = convert_splitted_values_to_keys(
            splitted_values=splitted_values
        )
        keys = remove_empty_keys(keys=keys)
        keys = _remove_skipping_pattern_keys_from_list(keys=keys)
        mappings: List[Dict[str, str]] = _make_mappings_from_keys(
            keys=keys, src_doc_file_path=src_doc_file_path, lang=lang
        )
        _save_mapping_data(
            mappings=mappings, src_doc_file_path=src_doc_file_path, lang=lang
        )
    lint_and_doc_hash_util.save_target_files_hash(
        file_paths=src_docs_file_paths, hash_type=hash_type
    )
    data_model.save_fixed_mapping_hash(lang=lang)


def _save_mapping_data(
    *, mappings: List[Dict[str, str]], src_doc_file_path: str, lang: Lang
) -> None:
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
        "of the\nfollowing document:"
        f"\n\nDocument file: {basename}"
        f"\nLanguage: {lang.value}"
        '\n"""'
        "\n\nfrom typing import Dict"
        f"\n\n{MAPPING_CONST_NAME}: Dict[str, str] = {{"
    )
    for mapping in mappings:
        module_str += "\n    "
        module_str += "#" * 50
        key: str = list(mapping.keys())[0]
        value: str = list(mapping.values())[0]
        line: str = f'    "{key}": "{value}",'
        if len(line) >= 88:
            line += "  # noqa"
        module_str += f"\n{line}"
    module_str += "\n}\n"
    module_path: str = get_mapping_module_path(
        src_doc_file_path=src_doc_file_path, lang=lang
    )
    file_util.save_plain_txt(txt=module_str, file_path=module_path)


def _make_mappings_from_keys(
    *, keys: List[str], src_doc_file_path: str, lang: Lang
) -> List[Dict[str, str]]:
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
        src_doc_file_path=src_doc_file_path, lang=lang
    )
    mappings: List[Dict[str, str]] = []
    for key in keys:
        key_: str = remove_escaping_from_key_or_value(key_or_val=key)
        value: str = already_saved_mapping.get(key_, "")
        value = escape_key_or_value(key_or_val=value)
        value = _set_fixed_translation_value_if_exists(key=key_, value=value)
        value = _set_same_value_if_code_block_mapping_is_blank(key=key, value=value)
        value = _set_translated_file_names_to_toc_code_block(lang=lang, value=value)
        value = _convert_link_list_by_lang(key=key, value=value, lang=lang)
        value = _set_same_value_if_api_params_or_returns_list(key=key, value=value)
        value = _set_same_value_if_key_is_no_mapping_fixed_string(key=key, value=value)
        value = _set_same_value_if_key_is_image_link(key=key, value=value)
        key = escape_key_or_value(key_or_val=key)
        value = escape_key_or_value(key_or_val=value)
        mappings.append({key: value})
    return mappings


def _set_translated_file_names_to_toc_code_block(*, lang: Lang, value: str) -> str:
    """
    Set translated file names to a specified mapping value
    if a value is the table of contents' code block.

    Parameters
    ----------
    lang : Lang
        A target language setting.
    value : str
        A mapping value.

    Returns
    -------
    value : str
        A result mapping value.
    """
    if not value.startswith("```{toctree}"):
        return value
    value = remove_escaping_from_key_or_value(key_or_val=value)
    lines: List[str] = value.splitlines()
    result_lines: List[str] = []
    for line in lines:
        match: Optional[Match] = re.match(
            pattern=r"^[a-z_0-9]+$",
            string=line,
        )
        if match is None:
            result_lines.append(line)
            continue
        if line.startswith(f"{lang.value}_"):
            result_lines.append(line)
            continue
        result_lines.append(f"{lang.value}_{line}")
    value = "\n".join(result_lines)
    return value


_BLANK_ALT_IMAGE_LINK_PATTERN: Pattern = re.compile(pattern=r"^\!\[\]\(.+?\)$")


def _set_same_value_if_key_is_image_link(*, key: str, value: str) -> str:
    """
    Set the same key as a value if a specified key is an
    image link string with an alternative blank text.

    Parameters
    ----------
    key : str
        A target key string.
    value : str
        A target value.

    Returns
    -------
    value : str
        This interface returns the same value if a specified
        key is an image link string with an alternative blank
        text. Otherwise, it returns a value argument directly.
    """
    match: Optional[Match] = _BLANK_ALT_IMAGE_LINK_PATTERN.match(string=key)
    if match is None:
        return value
    return key


_API_DOC_PARAMS_OR_RETURNS_NAME_PATTERN: Pattern = re.compile(
    pattern=r"^\- \`.+?\`\: .*$"
)


def _set_same_value_if_key_is_no_mapping_fixed_string(*, key: str, value: str) -> str:
    """
    Set the same key as a value if a specified key is a
    no-mapping fixed string.

    Parameters
    ----------
    key : str
        A target key string.
    value : str
        A target value.

    Returns
    -------
    value : str
        This interface returns a key's value if a specified
        key is a no-mapping fixed string. Otherwise, this
        interface returns a specified value directly.
    """
    for no_mapping_fixed_string in _NO_MAPPING_FIXED_STRINGS:
        if key == no_mapping_fixed_string:
            return key
    return value


def _set_same_value_if_api_params_or_returns_list(*, key: str, value: str) -> str:
    """
    Set the same key as a value if a specified key string
    is an API's parameters or returns list's line.

    Parameters
    ----------
    key : str
        A target key string.
    value : str
        A target value.

    Returns
    -------
    value : str
        This interface returns a key's value if a specified
        key string is an API's parameters or returns line.
        Otherwise, this interface returns a specified value directly.
    """
    match: Optional[Match] = _API_DOC_PARAMS_OR_RETURNS_NAME_PATTERN.match(string=key)
    if match is None:
        return value
    return key


_LINK_PATTERN: Pattern = re.compile(
    pattern=(r"(.*?\[.+?\])" r"\((.+?\.(md|html))\)" r"(?P<after_txt>.*?)"),
    flags=re.MULTILINE,
)


def _convert_link_list_by_lang(*, key: str, value: str, lang: Lang) -> str:
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
    if not key.startswith("- "):
        return value
    match: Optional[Match] = _LINK_PATTERN.search(string=key)
    if match is None:
        return value
    value = ""
    while match is not None:
        prev_txt: str = match.group(1)
        doc_path: str = match.group(2)
        doc_path = get_translated_file_path_from_src_path(
            source_doc_path=doc_path, lang=lang
        )
        if value != "":
            value += "\n"
        value += f"{prev_txt}({doc_path})"

        key = _LINK_PATTERN.sub(repl=r"\g<after_txt>", string=key, count=1)
        match = _LINK_PATTERN.search(string=key)
    value = _replace_link_text_by_fixed_mapping(value=value, lang=lang)
    value = _replace_link_en_dir_with_target_lang(value=value, lang=lang)
    value = escape_key_or_value(key_or_val=value)
    return value


def _replace_link_en_dir_with_target_lang(*, value: str, lang: Lang) -> str:
    """
    Replace a link's `/en/` directory path with a specified language directory path.

    Parameters
    ----------
    value : str
        A target markdown string value to replace.
    lang : Lang
        A target translation language.

    Returns
    -------
    value : str
        Replaced markdown string.
    """
    value = re.sub(
        pattern=r"\/en\/",
        repl=rf"/{lang.value}/",
        string=value,
    )
    return value


def _replace_link_text_by_fixed_mapping(*, value: str, lang: Lang) -> str:
    """
    Replace each link text if there are fixed translation-mapping
    settings.

    Parameters
    ----------
    value : str
        A link text.
    lang : Lang
        A target translation language.

    Returns
    -------
    value : str
        A replaced link text. This interface returns a blank string
        if there is no translation mapping.
    """
    from apysc._lint_and_doc.fixed_translation_mapping import data_model

    link_texts: List[str] = _extract_link_texts(value=value)
    for link_text in link_texts:
        translation_str: str = data_model.get_fixed_translation_str_if_exists(
            key=link_text, lang=lang
        )
        if translation_str == "":
            return ""
        value = value.replace(f"[{link_text}](", f"[{translation_str}](")
    return value


_LinkTextPattern: Pattern = re.compile(
    pattern=r".*?\[(.+?)\]\(.+?\.(md|html)\)", flags=re.MULTILINE
)


def _extract_link_texts(*, value: str) -> List[str]:
    """
    Extract link texts from a specified value string.

    Parameters
    ----------
    value : str
        A target value string.

    Returns
    -------
    link_texts : list of str
        Extracted link texts.
    """
    link_texts: List[str] = []
    match: Optional[Match] = _LinkTextPattern.search(string=value)
    while match is not None:
        link_text: str = match.group(1)
        link_texts.append(link_text)
        value = _LinkTextPattern.sub(repl="", string=value, count=1)
        match = _LinkTextPattern.search(string=value)
    return link_texts


def _set_same_value_if_code_block_mapping_is_blank(*, key: str, value: str) -> str:
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
    if value != "":
        return value
    if not key.startswith("```"):
        return value
    return key


def _set_fixed_translation_value_if_exists(*, key: str, value: str) -> str:
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
        key=key, lang=Lang.JP
    )
    if fixed_value == "":
        return value
    return fixed_value


def _remove_skipping_pattern_keys_from_list(*, keys: List[str]) -> List[str]:
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
    patterns: List[Pattern] = [*SKIPPING_PATTERNS, *MAPPING_UNNECESSARY_PATTERNS]
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


def _get_src_docs_file_paths() -> List[str]:
    """
    Get source documents file paths.

    Returns
    -------
    src_docs_file_paths : list of str
        Source documents file paths.
    """
    dir_path: str = "./docs_src/source/"
    file_or_dir_names: List[str] = os.listdir(dir_path)
    src_docs_file_paths: List[str] = []
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(dir_path, file_or_dir_name)
        if not os.path.isfile(file_or_dir_path):
            continue
        if not file_or_dir_path.endswith(".md"):
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
