"""Definition of js function expressions (e.g., common helper function).
"""

import inspect
import sys
from types import ModuleType
from typing import Any
from typing import List
from typing import Tuple

from typing_extensions import Final

FUNC_COPY: Final[str] = """function cpy(any_obj) {
  return JSON.parse(JSON.stringify(any_obj));
}"""


def get_js_functions() -> List[str]:
    """
    Get js function expressions that defined in this module.

    Returns
    -------
    js_function_strs : list of str
        js function expressions that defined in this module.
        String constants that have `FUNC_` name prefix will be
        appended in.
    """
    this_module: ModuleType = sys.modules[__name__]
    members: List[Tuple[str, Any]] = inspect.getmembers(this_module)
    js_function_strs: List[str] = []
    for member_name, member_val in members:
        if not isinstance(member_val, str):
            continue
        if not member_name.startswith('FUNC_'):
            continue
        js_function_strs.append(member_val)
    return js_function_strs
