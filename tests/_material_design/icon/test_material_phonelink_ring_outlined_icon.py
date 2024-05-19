from apysc._material_design.icon.material_phonelink_ring_outlined_icon import MaterialphonelinkRingOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkRingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkRingOutlinedIcon = MaterialphonelinkRingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
