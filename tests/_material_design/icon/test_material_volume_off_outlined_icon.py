from apysc._material_design.icon.material_volume_off_outlined_icon import (
    MaterialvolumeOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeOffOutlinedIcon = MaterialvolumeOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
