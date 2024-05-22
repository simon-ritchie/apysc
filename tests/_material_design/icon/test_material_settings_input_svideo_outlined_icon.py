from apysc._material_design.icon.material_settings_input_svideo_outlined_icon import (
    MaterialSettingsInputSvideoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsInputSvideoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsInputSvideoOutlinedIcon = (
            MaterialSettingsInputSvideoOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
