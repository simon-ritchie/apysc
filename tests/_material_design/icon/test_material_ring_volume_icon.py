from apysc._material_design.icon.material_ring_volume_icon import MaterialRingVolumeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRingVolumeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRingVolumeIcon = MaterialRingVolumeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
