from apysc._material_design.icon.material_card_travel_outlined_icon import (
    MaterialCardTravelOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCardTravelOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCardTravelOutlinedIcon = MaterialCardTravelOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
