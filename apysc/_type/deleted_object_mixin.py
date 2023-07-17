"""This module is for the class implementation of
the `DeletedObjectMixIn`.
"""

import inspect
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from typing_extensions import final

from apysc._type.revert_mixin import RevertMixIn


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

        Notes
        -----
        This method disables only public methods (this method skips
        methods which starts with the single underscore character).
        """
        method_members: List[Tuple[str, Callable]] = inspect.getmembers(
            self, predicate=inspect.ismethod
        )
        for method_name, _ in method_members:
            if method_name.startswith("_") and not method_name.startswith("__"):
                continue
            setattr(self, method_name, self._disabled_method)

    _is_deleted_object_snapshot: Optional[Dict[str, bool]] = None

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
        self.__is_deleted_object = self._get_snapshot_val_if_exists(
            current_value=self.__is_deleted_object,
            snapshot_dict=self._is_deleted_object_snapshot,
            snapshot_name=snapshot_name,
        )
