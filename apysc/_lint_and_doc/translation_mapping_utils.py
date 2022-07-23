"""This module is for translation-mapping
utility implementations.
"""

import importlib
import os
import re
from types import ModuleType
from typing import Dict
from typing import List
from typing import Match
from typing import Optional
from typing import Pattern
from typing import Union

from apysc._lint_and_doc.docs_lang import Lang
from apysc._lint_and_doc.docstring_util import DOCSTRING_PATH_COMMENT_PATTERN
from apysc._lint_and_doc.document_text_split_util import BodyText
from apysc._lint_and_doc.document_text_split_util import CodeBlock
from apysc._lint_and_doc.document_text_split_util import Heading
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType

MAPPING_CONST_NAME: str = "MAPPING"

SKIPPING_PATTERNS: List[Pattern] = [
    re.compile(pattern=DOCSTRING_PATH_COMMENT_PATTERN),
]

_INTERFACE_SIGNATURE_PATTERN: str = r"\*\*\[Interface signature\]\*\* .*?<hr>"

_CODE_BLOCK_IFRAME_PATTERN: str = r'<iframe src=\\"static.*?index\.html\\".*?></iframe>'

MAPPING_UNNECESSARY_PATTERNS: List[Pattern] = [
    re.compile(pattern=_INTERFACE_SIGNATURE_PATTERN),
    re.compile(pattern=_CODE_BLOCK_IFRAME_PATTERN),
    re.compile(pattern=_CODE_BLOCK_IFRAME_PATTERN.replace("\\", "")),
]

_SplittedVals = List[Union[Heading, BodyText, CodeBlock]]


def read_mapping_data(*, src_doc_file_path: str, lang: Lang) -> Dict[str, str]:
    """
    Read an already saved mapping data.

    Parameters
    ----------
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.

    Returns
    -------
    already_saved_mapping : dict
        An already saved mapping data dictionary.
    """
    from apysc._file import module_util

    mapping_module_path: str = get_mapping_module_path(
        src_doc_file_path=src_doc_file_path, lang=lang
    )
    if not os.path.isfile(mapping_module_path):
        return {}
    module: ModuleType = module_util.read_target_path_module(
        module_path=mapping_module_path
    )
    importlib.reload(module)
    if not hasattr(module, MAPPING_CONST_NAME):
        return {}
    already_saved_mapping: Dict[str, str] = getattr(module, MAPPING_CONST_NAME)
    return already_saved_mapping


def get_mapping_module_path(*, src_doc_file_path: str, lang: Lang) -> str:
    """
    Get a mapping data module path.

    Parameters
    ----------
    src_doc_file_path : str
        A target source document file path.
    lang : Lang
        A target translation language.

    Returns
    -------
    mapping_module_path : str
        A mapping data module path.
    """
    basename: str = os.path.basename(src_doc_file_path)
    basename = basename.replace(".md", ".py", 1)
    mapping_module_path: str = os.path.join(
        f"./apysc/_translation/{lang.value}/",
        basename,
    )
    return mapping_module_path


def convert_splitted_values_to_keys(*, splitted_values: _SplittedVals) -> List[str]:
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
        key: str = ""
        if isinstance(splitted_value, Heading):
            key = splitted_value.overall_text
        if isinstance(splitted_value, BodyText):
            is_body_text = True
            key = splitted_value.text
        if isinstance(splitted_value, CodeBlock):
            key = splitted_value.overall_code_block
        key = escape_key_or_value(key_or_val=key)
        if not is_body_text:
            keys.append(key)
        else:
            _append_body_text_keys_to_list(key=key, keys=keys)
    return keys


def _append_body_text_keys_to_list(*, key: str, keys: List[str]) -> None:
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
    splitted_keys: List[str] = key.split("\\n\\n")
    for key_ in splitted_keys:
        if _key_is_api_docs_list(key_=key_):
            lines: List[str] = key_.split("\\n")
            keys.extend(lines)
        elif _key_is_api_docs_br_tags_list(key_=key_):
            _extend_keys_with_api_docs_br_tags_list(keys=keys, key_=key_)
        else:
            keys.append(key_)


def _extend_keys_with_api_docs_br_tags_list(*, keys: List[str], key_: str) -> None:
    """
    Extend a specified keys list with an API docs' break tags list.

    Parameters
    ----------
    keys : list of str
        A keys list to extend.
    key_ : str
        An API docs' break tags list string.
    """
    splitted_keys: List[str] = key_.split("<br> ・")
    for i, splitted_key in enumerate(splitted_keys):
        if i != 0:
            splitted_keys[i] = f"<br> ・{splitted_key}"
    keys.extend(splitted_keys)


def _key_is_api_docs_br_tags_list(*, key_: str) -> bool:
    """
    Get a boolean indicating whether a specified key's string
    is a list markdown with break tags.

    Parameters
    ----------
    key_ : str
        A target key string to check.

    Returns
    -------
    result : bool
        A boolean indicates whether a specified key's string
        is a markdown of a list with break tags or not.
    """
    if "<br> ・" in key_:
        return True
    return False


_API_DOCS_LIST_PATTERN: Pattern = re.compile(pattern=r"^- .+?\\n", flags=re.MULTILINE)


def _key_is_api_docs_list(*, key_: str) -> bool:
    """
    Get a boolean indicating whether a specified key's
    string is an API document's (parameters, returns, exceptions,
    references) list.

    Parameters
    ----------
    key_ : str
        A target key string to check.

    Returns
    -------
    result : bool
        A boolean indicates whether a specified key's string
        is a markdown of a list with break tags or not.
    """
    match: Optional[Match] = _API_DOCS_LIST_PATTERN.search(string=key_)
    if match is None:
        return False
    return True


def escape_key_or_value(*, key_or_val: str) -> str:
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
    key_or_val = remove_escaping_from_key_or_value(key_or_val=key_or_val)
    TMP_LINE_END_ESCAPE_STR: str = "___tmp_line_end___"
    key_or_val = re.sub(
        pattern=r"\\$\n",
        repl=TMP_LINE_END_ESCAPE_STR,
        string=key_or_val,
        flags=re.MULTILINE,
    )
    key_or_val = key_or_val.replace("\\", "\\\\")
    key_or_val = key_or_val.replace("'", "\\'")
    key_or_val = key_or_val.replace('"', '\\"')
    key_or_val = key_or_val.replace("\n", "\\n")
    key_or_val = key_or_val.replace("\\\\n", "\\n")
    key_or_val = re.sub(
        pattern=rf"{TMP_LINE_END_ESCAPE_STR}",
        repl=r"\\\\\\n",
        string=key_or_val,
        flags=re.MULTILINE,
    )
    return key_or_val


def remove_escaping_from_key_or_value(*, key_or_val: str) -> str:
    """
    Remove escaping characters from a specified key or value string.

    Parameters
    ----------
    key_or_val : str
        A target key or value string.

    Returns
    -------
    key_or_val : str
        A result key or value string.
    """
    key_or_val = key_or_val.replace("\\\\", "\\")
    key_or_val = key_or_val.replace("\\'", "'")
    key_or_val = key_or_val.replace('\\"', '"')
    key_or_val = key_or_val.replace("\\n", "\n")
    return key_or_val


def is_mapping_unnecessary_key(*, key: str) -> bool:
    """
    Get a boolean indicating whether a specified key
    is an unnecessary mapping pattern or not.

    Parameters
    ----------
    key : str
        A target key string to check.

    Returns
    -------
    result : bool
        This interface returns True if a specified key is
        an unnecessary mapping pattern.
    """
    for pattern in MAPPING_UNNECESSARY_PATTERNS:
        match: Optional[Match] = pattern.search(string=key)
        if match is not None:
            return True
    return False


def is_translation_skipping_key(*, key: str) -> bool:
    """
    Get a boolean indicating whether a specified
    key is a translation skipping pattern or not.

    Parameters
    ----------
    key : str
        A target key string to check.

    Returns
    -------
    result : bool
        This interface returns True if a specified key
        is a translation skipping pattern.
    """
    for pattern in SKIPPING_PATTERNS:
        match: Optional[Match] = pattern.search(string=key)
        if match is not None:
            return True
    return False


def get_translated_file_path_from_src_path(*, source_doc_path: str, lang: Lang) -> str:
    """
    Get a translated file path from a specified source
    document's file path.

    Parameters
    ----------
    source_doc_path : str
        A target document's file path.
    lang : Lang
        A target language.

    Returns
    -------
    translated_file_path : str
        A translated file path.
    """
    basename: str = os.path.basename(source_doc_path)
    basename = f"{lang.value}_{basename}"
    dir_path = os.path.dirname(source_doc_path)
    translated_file_path: str = os.path.join(dir_path, basename)
    return translated_file_path


def remove_empty_keys(*, keys: List[str]) -> List[str]:
    """
    Remove empty (or only spaces) keys (source text) from
    a specified list.

    Parameters
    ----------
    keys : list of str
        A target keys list.

    Returns
    -------
    result_keys : list of str
        A result keys list.
    """
    result_keys: List[str] = []
    for key in keys:
        if key.strip() == "":
            continue
        result_keys.append(key)
    return result_keys


def get_hash_type_from_lang(*, lang: Lang) -> HashType:
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
        "There is no implementation of a specified language type's "
        "branch condition. Please add a necessary branch condition: "
        f"{lang}"
    )
