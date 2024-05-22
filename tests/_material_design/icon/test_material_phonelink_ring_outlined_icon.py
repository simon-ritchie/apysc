from apysc._material_design.icon.material_phonelink_ring_outlined_icon import (
    MaterialPhonelinkRingOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhonelinkRingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhonelinkRingOutlinedIcon = MaterialPhonelinkRingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
