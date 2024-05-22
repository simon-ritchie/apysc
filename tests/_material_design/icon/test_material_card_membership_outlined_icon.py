from apysc._material_design.icon.material_card_membership_outlined_icon import (
    MaterialCardMembershipOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCardMembershipOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCardMembershipOutlinedIcon = MaterialCardMembershipOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
