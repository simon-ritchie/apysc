from apysc._material_design.icon.material_card_membership_outlined_icon import (
    MaterialcardMembershipOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcardMembershipOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcardMembershipOutlinedIcon = MaterialcardMembershipOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
