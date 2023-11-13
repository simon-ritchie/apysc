"""Class implementation for the `revert`-related mix-in.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar

from typing_extensions import final

from apysc._type.revert_interface import RevertInterface

_SnapshotValue = TypeVar("_SnapshotValue")


class RevertMixIn(RevertInterface):
    _snapshot_exists_: Dict[str, bool]

    def _initialize_ss_exists_val_if_not_initialized(self) -> None:
        """
        Initialize _snapshot_exists_ value if this instance
        does not initialize it yet.
        """
        if hasattr(self, "_snapshot_exists_"):
            return
        self._snapshot_exists_ = {}

    @final
    def _run_all_make_snapshot_methods(self, *, snapshot_name: str) -> None:
        """
        Run all _make_snapshot methods. If an instance has
        multiple inheritances, and each class inherits
        RevertMixIn, each class calls the _make_snapshot
        methods.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self_type: Type = type(self)
        self._run_base_cls_make_snapshot_methods_recursively(
            class_=self_type, snapshot_name=snapshot_name
        )
        self._set_snapshot_exists_val(snapshot_name=snapshot_name)

    @final
    def _run_base_cls_make_snapshot_methods_recursively(
        self, *, class_: Type["RevertMixIn"], snapshot_name: str
    ) -> None:
        """
        Run base classes make_snapshot methods recursively.

        Parameters
        ----------
        class_ : type
            Target type.
        snapshot_name : str
            Target snapshot name.
        """
        base_classes: Tuple[Type, ...] = class_.__bases__
        for base_class in base_classes:
            if not issubclass(base_class, RevertMixIn):
                continue
            base_class._make_snapshot(self, snapshot_name=snapshot_name)
            self._run_base_cls_make_snapshot_methods_recursively(
                class_=base_class, snapshot_name=snapshot_name
            )
        class_._make_snapshot(self, snapshot_name=snapshot_name)

    @final
    def _run_all_revert_methods(self, *, snapshot_name: str) -> None:
        """
        Run all _revert methods. If an instance has multiple
        inheritances, and each class inherits RevertMixIn,
        each class calls the _revert methods.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self_type: Type = type(self)
        self._run_base_cls_revert_methods_recursively(
            class_=self_type, snapshot_name=snapshot_name
        )
        self._delete_snapshot_exists_val(snapshot_name=snapshot_name)

    @final
    def _run_base_cls_revert_methods_recursively(
        self, *, class_: Type["RevertMixIn"], snapshot_name: str
    ) -> None:
        """
        Run base classes revert methods recursively.

        Parameters
        ----------
        class_ : type
            Target type.
        snapshot_name : str
            Target snapshot name.
        """
        base_classes: Tuple[Type, ...] = class_.__bases__
        for base_class in base_classes:
            if not issubclass(base_class, RevertMixIn):
                continue
            base_class._revert(self, snapshot_name=snapshot_name)
            self._run_base_cls_revert_methods_recursively(
                class_=base_class, snapshot_name=snapshot_name
            )
        class_._revert(self, snapshot_name=snapshot_name)

    @final
    def _snapshot_exists(self, *, snapshot_name: str) -> bool:
        """
        Get a boolean value whether a snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.

        Returns
        -------
        snapshot_exists : bool
            Boolean value, whether a snapshot value exists or not.
        """
        self._initialize_ss_exists_val_if_not_initialized()
        return snapshot_name in self._snapshot_exists_

    @final
    def _set_snapshot_exists_val(self, *, snapshot_name: str) -> None:
        """
        Set a boolean value whether a snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ss_exists_val_if_not_initialized()
        self._snapshot_exists_[snapshot_name] = True

    @final
    def _delete_snapshot_exists_val(self, *, snapshot_name: str) -> None:
        """
        Delete a boolean value whether a snapshot value exists or not.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ss_exists_val_if_not_initialized()
        if snapshot_name in self._snapshot_exists_:
            del self._snapshot_exists_[snapshot_name]

    @final
    def _get_next_snapshot_name(self) -> str:
        """
        Get the next snapshot name.

        Returns
        -------
        snapshot_name : str
            Next snapshot name.
        """
        from apysc._expression import expression_variables_util
        from apysc._expression.var_names import SNAPSHOT

        snapshot_name: str = expression_variables_util.get_next_variable_name(
            type_name=SNAPSHOT
        )
        return snapshot_name

    @final
    def _set_single_snapshot_val_to_dict(
        self, *, dict_name: str, value: Any, snapshot_name: str
    ) -> None:
        """
        Set a single snapshot value to the specified
        name dictionary.

        Notes
        -----
        If a snapshot value of the same name already exists,
        this interface stops the method execution.

        Parameters
        ----------
        dict_name : str
            Target dictionary name.
        value : Any
            Target value.
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, dict_name) or getattr(self, dict_name) is None:
            setattr(self, dict_name, {})
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        target_dict: Optional[Dict[str, Any]] = getattr(self, dict_name)
        if target_dict is None:
            target_dict = {}
        target_dict[snapshot_name] = value

    @final
    def _get_snapshot_val_if_exists(
        self,
        *,
        current_value: _SnapshotValue,
        snapshot_dict: Optional[Dict[str, _SnapshotValue]],
        snapshot_name: str,
    ) -> _SnapshotValue:
        """
        Get a snapshot value from a specified dictionary if a snapshot exists.

        Parameters
        ----------
        current_value : _SnapshotValue
            A current value.
        snapshot_dict : Optional[Dict[str, _SnapshotValue]]
            A dictionary that contains a snapshot value.
        snapshot_name : str
            A target snapshot name.

        Returns
        -------
        snapshot_value : _SnapshotValue
            A snapshot value. If a snapshot value does not exist,
            this interface returns a current value.
        """
        if snapshot_dict is None:
            snapshot_dict = {}
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return current_value
        snapshot_value: _SnapshotValue = snapshot_dict[snapshot_name]
        return snapshot_value


def make_snapshots_of_each_scope_vars(
    *, locals_: Dict[str, Any], globals_: Dict[str, Any]
) -> str:
    """
    Make snapshots of each scope's variables.

    Parameters
    ----------
    locals_ : dict
        Local scope's variables.
    globals_ : dict
        Global scope's variables.

    Returns
    -------
    snapshot_name : str
        Snapshot name to be used.
    """
    variables: List[Any] = [*locals_.values(), *globals_.values()]
    snapshot_name: str = make_variables_snapshots(variables=variables)
    return snapshot_name


def make_variables_snapshots(*, variables: List[Any]) -> str:
    """
    Make snapshots of specified variables.

    Parameters
    ----------
    variables : list
        Variables to make snapshots.

    Returns
    -------
    snapshot_name : str
        Snapshot name to be used.
    """
    ended: Dict[int, bool] = {}
    snapshot_name: str = ""
    for variable in variables:
        if not isinstance(variable, RevertMixIn):
            continue
        var_id: int = id(variable)
        if var_id in ended:
            continue
        if snapshot_name == "":
            snapshot_name = variable._get_next_snapshot_name()
        variable._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        ended[var_id] = True
    return snapshot_name


def revert_each_scope_vars(
    *, snapshot_name: str, locals_: Dict[str, Any], globals_: Dict[str, Any]
) -> None:
    """
    Revert each scope's variables.

    Parameters
    ----------
    snapshot_name : str
        Snapshot name to use.
    locals_ : dict
        Local scope's variables.
    globals_ : dict
        Global scope's variables.
    """
    variables: List[Any] = [*locals_.values(), *globals_.values()]
    revert_variables(snapshot_name=snapshot_name, variables=variables)


def revert_variables(*, snapshot_name: str, variables: List[Any]) -> None:
    """
    Revert each variable.

    Parameters
    ----------
    snapshot_name : str
        Snapshot name to use.
    variables : list
        Each variable to revert.
    """
    ended: Dict[int, bool] = {}
    for variable in variables:
        if not isinstance(variable, RevertMixIn):
            continue
        var_id: int = id(variable)
        if var_id in ended:
            continue
        variable._run_all_revert_methods(snapshot_name=snapshot_name)
        ended[var_id] = True
