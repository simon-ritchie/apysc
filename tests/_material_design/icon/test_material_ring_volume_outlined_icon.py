from apysc._material_design.icon.material_ring_volume_outlined_icon import MaterialringVolumeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialringVolumeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialringVolumeOutlinedIcon = MaterialringVolumeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
