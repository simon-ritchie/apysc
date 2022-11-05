"""This module is for the class implementation of
the `DeletedObjectMixIn`.
"""

import inspect
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple

from typing_extensions import final

from apysc._type.revert_mixin import RevertMixIn

_EXCLUDING_TARGET_METHOD_NAMES: List[str] = [
    "_make_snapshot",
    "_revert",
    "_set_single_snapshot_val_to_dict",
    "_snapshot_exists",
    "_get_next_snapshot_name",
    "_run_all_make_snapshot_methods",
    "_run_all_revert_methods",
    "_delete_snapshot_exists_val",
    "_run_base_cls_revert_methods_recursively",
    "_run_base_cls_make_snapshot_methods_recursively",
    "_set_snapshot_exists_val",
    "_initialize_ss_exists_val_if_not_initialized",
    "_disable_each_method",
    "_disabled_method",
]


class _DisabledObjectError(Exception):
    pass


class DeletedObjectMixIn(RevertMixIn):

    __is_deleted_object: bool = False

    @property
    def _is_deleted_object(self) -> bool:
        """
        Get a boolean indicating whether this object is
        deleted object or not.

        Returns
        -------
        _is_deleted_object : bool
            A boolean indicating whether this object is
            deleted object or not.
        """
        return self.__is_deleted_object

    @_is_deleted_object.setter
    def _is_deleted_object(self, value: bool) -> None:
        """
        Set a boolean indicating whether this object is
        deleted object or not.

        Parameters
        ----------
        value : bool
            A target value to set.
        """
        self.__is_deleted_object = value
        if value:
            self._disable_each_method()

    @final
    def _disabled_method(self, *args: Any, **kwargs: Any) -> None:
        """
        The method to replace each method when this object
        becomes deleted object.

        Raises
        ------
        _DisabledObjectError
            This interface always raises an exception.
        """
        raise _DisabledObjectError(
            "This object has been deleted and cannot manipulate."
        )

    @final
    def _disable_each_method(self) -> None:
        """
        Disable each method of this instance.
        """
        method_members: List[Tuple[str, Callable]] = inspect.getmembers(
            self, predicate=inspect.ismethod
        )
        for method_name, _ in method_members:
            if method_name in _EXCLUDING_TARGET_METHOD_NAMES:
                continue
            setattr(self, method_name, self._disabled_method)

    _is_deleted_object_snapshot: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._set_single_snapshot_val_to_dict(
            dict_name="_is_deleted_object_snapshot",
            value=self.__is_deleted_object,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self.__is_deleted_object = self._is_deleted_object_snapshot[snapshot_name]
