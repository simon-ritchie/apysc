from apysc._material_design.icon.material_camera_enhance_icon import (
    MaterialCameraEnhanceIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCameraEnhanceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCameraEnhanceIcon = MaterialCameraEnhanceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
