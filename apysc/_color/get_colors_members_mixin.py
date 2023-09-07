"""The mix-in class for the `get_colors_members` method.
"""

from typing import List
from typing import Tuple

from apysc._color.color import Color
from apysc._html.debug_mode import add_debug_info_setting


class GetColorsMenmbersMixIn:
    @classmethod
    @add_debug_info_setting(module_name=__name__)
    def get_colors_members(cls) -> List[Tuple[str, Color]]:
        """
        Get colors' members of this instance.

        Returns
        -------
        members : List[Tuple[str, Color]]
            A colors' members of this instance.
            A tuple's first element is a constant name,
            and second is a color instance.
        """
        members: List[Tuple[str, Color]] = []
        for member_name, member_value in cls.__dict__.items():
            if not isinstance(member_value, Color):
                continue
            members.append((member_name, member_value))
        return members
