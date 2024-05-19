from apysc._material_design.icon.material_phonelink_ring_icon import (
    MaterialphonelinkRingIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkRingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkRingIcon = MaterialphonelinkRingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
