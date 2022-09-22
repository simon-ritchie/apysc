"""The utilities module for each lint and doc's hash file
(used to check whether the files are updated or not).

Mainly following interfaces are defined:

- get_hash_dir_path
    - Get a specified type's hash directory path.
- get_target_file_hash_file_path
    - Get a specified file's hash file path.
- read_target_file_hash
    - Read a specified file's hashed string.
- read_saved_hash
    - Read an already-saved file's hashed string.
- save_target_file_hash
    - Save a target file's current hash.
- save_target_files_hash
    - Save target files' current hash.
- is_file_updated
    - Get a boolean value whether a specified file has been updated.
- remove_not_updated_file_paths
    - Remove not updated files from specified file paths.
- delete_target_file_hash
    - Delete a target file's hash file.
"""

import hashlib
import os
from concurrent import futures
from enum import Enum
from multiprocessing import Pool
from multiprocessing import cpu_count
from typing import List

from typing_extensions import TypedDict


class HashType(Enum):

    AUTOFLAKE = "autoflake"
    ISORT = "isort"
    DOCSTRING_SRC = "docstring_src"
    DOCSTRING_TO_MARKDOWN = "docstring_to_markdown"
    TRANSLATION_MAPPING_JP = "translation_mapping_jp"
    TRANSLATION_FIXED_MAPPING_JP = "translation_fixed_mapping_jp"
    APPLYING_TRANSLATION_MAPPING = "applying_translation_mapping"
    DOCUMENT = "document"


_HASH_PACKAGE_ROOT_PATH: str = "./.lint_and_doc_hash"


def get_hash_dir_path(*, hash_type: HashType) -> str:
    """
    Get a specified type's hash directory path.

    Parameters
    ----------
    hash_type : HashType
        Target hash type.

    Returns
    -------
    dir_path : str
        Target type's hash directory path.

    Notes
    -----
    This interface creates a returned directory path
    if it does not exist.
    """
    dir_path: str = os.path.join(_HASH_PACKAGE_ROOT_PATH, f".{hash_type.value}/")
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_target_file_hash_file_path(*, file_path: str, hash_type: HashType) -> str:
    """
    Get a specified file's hash file path.

    Parameters
    ----------
    file_path : str
        Target file path.
    hash_type : HashType
        Target hash type.

    Returns
    -------
    file_path : str
        Target hash file path.

    Notes
    -----
    This interface automatically creates a returned file's
    directory path if it does not exist.
    """
    if file_path.startswith("./"):
        file_path = file_path.replace("./", "", 1)
    dir_path: str = get_hash_dir_path(hash_type=hash_type)
    file_path_: str = os.path.join(dir_path, file_path)
    basename: str = os.path.basename(file_path_)
    if "." in basename:
        extension: str = basename.split(".")[-1]
        file_path_ = file_path_.replace(f".{extension}", "", 1)
    os.makedirs(os.path.dirname(file_path_), exist_ok=True)
    return file_path_


def read_target_file_hash(*, file_path: str) -> str:
    """
    Read a specified file's hashed string.

    Parameters
    ----------
    file_path : str
        Target file path.

    Returns
    -------
    hashed_string : str
        Hashed file string. If there is no file at
        the specified path, this interface returns
        a blank string.
    """
    from apysc._file import file_util

    if not os.path.isfile(file_path):
        return ""
    file_txt: str = file_util.read_txt(file_path=file_path)
    hashed_string: str = hashlib.sha1(file_txt.encode()).hexdigest()
    return hashed_string


def read_saved_hash(*, file_path: str, hash_type: HashType) -> str:
    """
    Read an already-saved file's hashed string.

    Parameters
    ----------
    file_path : str
        Target file path.
    hash_type : HashType
        Target hash type.

    Returns
    -------
    saved_hash : str
        An already-saved file's hash string. If there
        is no saved hash file, this interface returns
        a blank string.
    """
    from apysc._file import file_util

    file_path_: str = get_target_file_hash_file_path(
        file_path=file_path, hash_type=hash_type
    )
    if not os.path.isfile(file_path_):
        return ""
    saved_hash: str = file_util.read_txt(file_path=file_path_)
    saved_hash = saved_hash.strip()
    return saved_hash


def save_target_file_hash(*, file_path: str, hash_type: HashType) -> None:
    """
    Save a target file's current hash.

    Parameters
    ----------
    file_path : str
        Target file path.
    hash_type : HashType
        Target hash type.
    """
    from apysc._file import file_util

    hash: str = read_target_file_hash(file_path=file_path)
    if hash == "":
        return
    file_path_: str = get_target_file_hash_file_path(
        file_path=file_path, hash_type=hash_type
    )
    file_util.save_plain_txt(txt=hash, file_path=file_path_)


def save_target_files_hash(*, file_paths: List[str], hash_type: HashType) -> None:
    """
    Save target files' current hash.

    Parameters
    ----------
    file_paths : list of str
        Target file paths.
    hash_type : HashType
        Target hash type.
    """
    workers: int = max(cpu_count() - 1, 1)
    with futures.ProcessPoolExecutor(max_workers=workers) as executor:
        future_list: List[futures.Future] = []
        for file_path in file_paths:
            future = executor.submit(
                save_target_file_hash, file_path=file_path, hash_type=hash_type
            )
            future_list.append(future)
        _ = futures.as_completed(fs=future_list)


def is_file_updated(*, file_path: str, hash_type: HashType) -> bool:
    """
    Get a boolean value whether a specified file is changing or not.

    Parameters
    ----------
    file_path : str
        Target file path.
    hash_type : HashType
        Target hash type.

    Returns
    -------
    result : bool
        If a specified file is changing, this interface
        returns True.
    """
    saved_hash: str = read_saved_hash(file_path=file_path, hash_type=hash_type)
    current_hash: str = read_target_file_hash(file_path=file_path)
    if saved_hash == current_hash:
        return False
    return True


class _IsFileUpdatedArgs(TypedDict):
    file_path: str
    hash_type: HashType


def _is_file_updated_func_for_multiprocessing(args: _IsFileUpdatedArgs) -> bool:
    """
    Wrapper function of the `is_file_updated` function
    for the multiprocessing.

    Parameters
    ----------
    args : _IsFileUpdatedArgs
        Arguments dictionary to pass to the `is_file_updated`
        function.

    Returns
    -------
    result : bool
        If there is an updated file, this interface
        returns True.
    """
    result: bool = is_file_updated(
        file_path=args["file_path"], hash_type=args["hash_type"]
    )
    return result


def _create_args_list_for_multiprocessing(
    *, file_paths: List[str], hash_type: HashType
) -> List[_IsFileUpdatedArgs]:
    """
    Create an arguments list for the multiprocessing.

    Parameters
    ----------
    file_paths : list of str
        Target file paths.
    hash_type : HashType
        Target hash type.

    Returns
    -------
    args_list : list of _IsFileUpdatedArgs
        Created arguments list for the multiprocessing.
    """
    args_list: List[_IsFileUpdatedArgs] = []
    for file_path in file_paths:
        args_list.append(
            {
                "file_path": file_path,
                "hash_type": hash_type,
            }
        )
    return args_list


def remove_not_updated_file_paths(
    *, file_paths: List[str], hash_type: HashType
) -> List[str]:
    """
    Remove not updated files from specified file paths.

    Parameters
    ----------
    file_paths : list of str
        Target file paths.
    hash_type : HashType
        Target hash type.

    Returns
    -------
    sliced_file_paths : list of str
        After the slicing file paths.
    """
    workers: int = max(cpu_count() - 1, 1)
    args_list: List[_IsFileUpdatedArgs] = _create_args_list_for_multiprocessing(
        file_paths=file_paths, hash_type=hash_type
    )
    sliced_file_paths: List[str] = []
    with Pool(processes=workers) as p:
        file_updated_bool_list: List[bool] = p.map(
            func=_is_file_updated_func_for_multiprocessing,
            iterable=args_list,
        )
    file_updated: bool
    for i, file_updated in enumerate(file_updated_bool_list):
        if not file_updated:
            continue
        sliced_file_paths.append(file_paths[i])
    return sliced_file_paths


def delete_target_file_hash(*, file_path: str, hash_type: HashType) -> None:
    """
    Delete a target file's hash file.

    Parameters
    ----------
    file_path : str
        A target file path.
    hash_type : HashType
        A Target hash type.
    """
    from apysc._file import file_util

    hash_file_path: str = get_target_file_hash_file_path(
        file_path=file_path,
        hash_type=hash_type,
    )
    file_util.delete_file_if_exists(file_path=hash_file_path)
