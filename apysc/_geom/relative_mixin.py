"""Mix-in class implementation for the relative value.
"""

from typing import Dict

from typing_extensions import final

from apysc._type.boolean import Boolean
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos


class RelativeMixIn(VariableNameSuffixAttrMixIn, RevertMixIn, VariableNameSuffixMixIn):

    _relative: Boolean

    @final
    def _initialize_relative_if_not_initialized(self) -> None:
        """
        Initialize the _relative attribute if this instance
        does not initialize it yet.
        """
        if hasattr(self, "_relative"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="relative")
        self._relative = Boolean(
            False,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @property
    def relative(self) -> Boolean:
        """
        Get a boolean value indicating whether a path data
        is relative or not.

        Returns
        -------
        relative : Boolean
            A boolean value indicating whether path data
            is relative or not.

        Examples
        --------
        >>> import apysc as ap
        >>> line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=50, relative=False)
        >>> line_to.relative = ap.Boolean(True)
        >>> line_to.relative
        Boolean(True)
        """
        self._initialize_relative_if_not_initialized()
        return self._relative._copy()

    @relative.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    def relative(self, value: Boolean) -> None:
        """
        Set a boolean value indicating whether path a path data
        is relative or not.

        Parameters
        ----------
        value : Boolean
            A boolean value indicating whether path data
            is relative or not.
        """
        self._initialize_relative_if_not_initialized()
        self._relative.value = value

    _relative_snapshots: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_relative_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_relative_snapshots",
            value=self._relative._value,
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
        self._initialize_relative_if_not_initialized()
        self._relative._value = self._relative_snapshots[snapshot_name]
