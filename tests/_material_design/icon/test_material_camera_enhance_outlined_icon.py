from apysc._material_design.icon.material_camera_enhance_outlined_icon import (
    MaterialCameraEnhanceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCameraEnhanceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCameraEnhanceOutlinedIcon = MaterialCameraEnhanceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
