from apysc._material_design.icon.material_volume_down_outlined_icon import (
    MaterialvolumeDownOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeDownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeDownOutlinedIcon = MaterialvolumeDownOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
