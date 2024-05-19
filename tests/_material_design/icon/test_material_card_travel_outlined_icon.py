from apysc._material_design.icon.material_card_travel_outlined_icon import (
    MaterialcardTravelOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcardTravelOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcardTravelOutlinedIcon = MaterialcardTravelOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
