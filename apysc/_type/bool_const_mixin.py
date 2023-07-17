"""The mix-in class implementation for the True and False constants classes.
"""

from typing import Union

from typing_extensions import Literal
from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.int import Int


class BoolConstMixIn:
    _value: bool

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_value_attr_with_value_arg(self, *, value: bool) -> None:
        """
        Set a `_value` attribute with a specified value argument.

        Notes
        -----
        This method's implementation does nothing (overridden as a blank method).

        Parameters
        ----------
        value : bool
            A boolean value.
        """

    @final
    def _set_value_and_skip_expression_appending(
        self, *, value: Union[bool, Literal[0, 1], Int, "Boolean"]
    ) -> None:
        """
        Update value attribute and skip expression appending.

        Notes
        -----
        This method's implementation does nothing (overridden as a blank method).

        Parameters
        ----------
        value : Boolean or Int or bool or int
            Any boolean value to set.
        """

    @final
    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Notes
        -----
        This method's implementation does nothing (overridden as a blank method).

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    @final
    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Notes
        -----
        This method's implementation does nothing (overridden as a blank method).

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    @property
    @add_debug_info_setting(module_name=__name__)
    def value(self) -> Union[bool, Literal[0, 1], Int, "Boolean"]:
        """
        Get a current boolean value.

        Returns
        -------
        value : bool
            Current boolean value.

        References
        ----------
        - apysc fundamental data classes value interface
            - https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> bool_val: ap.Boolean = ap.Boolean(True)
        >>> bool_val.value = False
        >>> bool_val.value
        False

        >>> bool_val.value = ap.Boolean(True)
        >>> bool_val.value
        True
        """
        return self._value

    @value.setter
    def value(self, value: Union[bool, Literal[0, 1], Int, "Boolean"]) -> None:
        """
        Set boolean value.

        Notes
        -----
        This interface is disabled and raise an exception if called.

        Parameters
        ----------
        value : Union[bool, Literal[0, 1], Int, &quot;Boolean&quot;]
            Any boolean value to set.

        Raises
        ------
        TypeError
            If this interface is called.
        """
        raise TypeError(
            "The `True` or `False` value is constant and cannot be changed."
        )
