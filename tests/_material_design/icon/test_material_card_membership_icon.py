from apysc._material_design.icon.material_card_membership_icon import (
    MaterialCardMembershipIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCardMembershipIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCardMembershipIcon = MaterialCardMembershipIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
