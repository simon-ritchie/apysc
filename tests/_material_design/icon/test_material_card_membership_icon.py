from apysc._material_design.icon.material_card_membership_icon import MaterialcardMembershipIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcardMembershipIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcardMembershipIcon = MaterialcardMembershipIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
