# mypy: disable-error-code=type-var

"""The decorator implementation for the auto reloading.
"""

import functools
from typing import Any, List, Optional
from typing import Callable
from typing import Dict
from typing import TypeVar
from datetime import datetime
import time
import os

# pyright: reportInvalidTypeVarUse=false
_Callable = TypeVar("_Callable", bound=Callable)


def set_auto_reloading(*, checking_dir_paths: List[str]) -> _Callable:
    """
    Set an auto-reloading setting as a decorator.

    Parameters
    ----------
    checking_dir_paths : List[str]
        Directory paths to check for files' changes.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            result: Any = callable_(*args, **kwargs)
            last_checked_time: datetime = datetime.now()

            while True:
                if not _are_files_updated(
                    last_checked_time=last_checked_time,
                    checking_dir_paths=checking_dir_paths,
                ):
                    time.sleep(0.5)
                    continue
                try:
                    result: Any = callable_(*args, **kwargs)
                except:
                    continue
    pass


def _are_files_updated(
    *,
    last_checked_time: datetime,
    checking_dir_paths: List[str],
) -> bool:
    """
    Get a boolean, whether files are updated or not.

    Parameters
    ----------
    last_checked_time : datetime
        A last checked time.
    checking_dir_paths : List[str]
        Directory paths to check for files' changes.

    Returns
    -------
    result : bool
        If any updated files exist, this interface returns True.
    """
    for dire_path in checking_dir_paths:
        file_or_dir_names: List[str] = os.listdir(dire_path)
        for file_or_dir_name in file_or_dir_names:
            file_or_dir_path: str = os.path.join(dire_path, file_or_dir_name)
            if os.path.isdir(file_or_dir_path):
                result: bool = _are_files_updated(
                    last_checked_time=last_checked_time,
                    checking_dir_paths=[file_or_dir_path],
                )
                if result:
                    return True
                continue

            last_modified: datetime = datetime.fromtimestamp(
                os.stat(file_or_dir_path).st_mtime,
            )
            if last_modified > last_checked_time:
                return True
    return False
