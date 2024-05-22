from apysc._material_design.icon.material_card_travel_icon import MaterialCardTravelIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCardTravelIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCardTravelIcon = MaterialCardTravelIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
