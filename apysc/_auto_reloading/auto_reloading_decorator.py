# mypy: disable-error-code=type-var

"""The decorator implementation for the auto-reloading.
"""

import functools
import os
import time
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import TypeVar

# pyright: reportInvalidTypeVarUse=false
_Callable = TypeVar("_Callable", bound=Callable)


def set_auto_reloading(
    *,
    checking_dir_paths: List[str],
    max_checking_num: Optional[int] = None,
) -> _Callable:
    """
    Set an auto-reloading setting as a decorator.

    Notes
    -----
    Currently, this setting checks only `.py` files.

    Parameters
    ----------
    checking_dir_paths : List[str]
        Directory paths to check for file changes.
    max_checking_num : Optional[int], optional
        Maximum checking attempts number.
        Mainly this interface uses this setting for the testing.

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.
    """

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:
            result: Any = callable_(*args, **kwargs)
            last_executed_time: datetime = datetime.now()
            time.sleep(1.0)

            checking_count: int = 0
            while True:
                if max_checking_num is not None and checking_count >= max_checking_num:
                    break
                if not _are_files_updated(
                    last_executed_time=last_executed_time,
                    checking_dir_paths=checking_dir_paths,
                ):
                    time.sleep(1.0)
                    checking_count += 1
                    continue
                try:
                    result = callable_(*args, **kwargs)
                    last_executed_time = datetime.now()
                    time.sleep(1.0)
                except Exception:
                    pass
                finally:
                    checking_count += 1
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def _are_files_updated(
    *,
    last_executed_time: datetime,
    checking_dir_paths: List[str],
) -> bool:
    """
    Get a boolean, whether files are updated or not.

    Parameters
    ----------
    last_executed_time : datetime
        A last execution time.
    checking_dir_paths : List[str]
        Directory paths to check for file changes.

    Returns
    -------
    result : bool
        If any updated files exist, this interface returns True.
    """
    timedelta_: timedelta = timedelta(seconds=1)
    for dire_path in checking_dir_paths:
        file_or_dir_names: List[str] = os.listdir(dire_path)
        for file_or_dir_name in file_or_dir_names:
            file_or_dir_path: str = os.path.join(dire_path, file_or_dir_name)
            if os.path.isdir(file_or_dir_path):
                result: bool = _are_files_updated(
                    last_executed_time=last_executed_time,
                    checking_dir_paths=[file_or_dir_path],
                )
                if result:
                    return True
                continue

            if not file_or_dir_path.endswith(".py"):
                continue

            last_modified: datetime = datetime.fromtimestamp(
                os.stat(file_or_dir_path).st_mtime,
            )
            if last_modified >= last_executed_time - timedelta_:
                return True
    return False
