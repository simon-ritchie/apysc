"""The mix-in class implementation for the `_initialize_locals_and_globals`
method.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final


class InitializeLocalsAndGlobalsMixIn:
    _locals: Dict[str, Any]
    _globals: Dict[str, Any]

    @final
    def _initialize_locals_and_globals(
        self,
        locals_: Optional[Dict[str, Any]],
        globals_: Optional[Dict[str, Any]],
    ) -> None:
        """
        Initialize the `locals` and `globals` attributes.

        Parameters
        ----------
        locals_ : Optional[Dict[str, Any]]
            Current scope's local variables.
        globals_ : Optional[Dict[str, Any]]
            Current scope's global variables.
        """
        if locals_ is None:
            locals_ = {}
        if globals_ is None:
            globals_ = {}
        self._locals = locals_
        self._globals = globals_
