"""Definition of js function expressions (e.g., common helper function).
"""

import inspect
import sys
from types import ModuleType
from typing import Any
from typing import List
from typing import Tuple

from typing_extensions import Final

# Function for deepcopy.
FUNC_COPY: Final[
    str
] = """function cpy(any_obj) {
  return JSON.parse(JSON.stringify(any_obj));
}"""

# Function to get a specified object's total x-coordinate (including
# parents coordinates).
FUNC_GET_TOTAL_X: Final[
    str
] = """function get_total_x(any_obj) {
    var total_x = 0;
    total_x += any_obj.attr("x");
    var parent = any_obj.parent();
    while (!_.isUndefined($(parent).attr("x"))) {
        total_x += parent.attr("x");
        parent = parent.parent();
    }
    return total_x;
}"""

# Function to get a specified object's total y-coordinate (including
# parents coordinates).
FUNC_GET_TOTAL_Y: Final[
    str
] = """function get_total_y(any_obj) {
    var total_y = 0;
    total_y += any_obj.attr("y");
    var parent = any_obj.parent();
    while (!_.isUndefined($(parent).attr("y"))) {
        total_y += parent.attr("y");
        parent = parent.parent();
    }
    return total_y;
}"""


def get_js_functions() -> List[str]:
    """
    Get js function expressions defined in this module.

    Returns
    -------
    js_function_strs : list of str
        js function expressions defined in this module.
        This interface returns the list of string constants
        with the `FUNC_` name prefix.
    """
    this_module: ModuleType = sys.modules[__name__]
    members: List[Tuple[str, Any]] = inspect.getmembers(this_module)
    js_function_strs: List[str] = []
    for member_name, member_val in members:
        if not isinstance(member_val, str):
            continue
        if not member_name.startswith("FUNC_"):
            continue
        js_function_strs.append(member_val)
    return js_function_strs
