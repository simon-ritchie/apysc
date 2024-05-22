from apysc._material_design.icon.material_volume_off_outlined_icon import (
    MaterialVolumeOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVolumeOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVolumeOffOutlinedIcon = MaterialVolumeOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
