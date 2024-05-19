from apysc._material_design.icon.material_camera_enhance_outlined_icon import MaterialcameraEnhanceOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcameraEnhanceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcameraEnhanceOutlinedIcon = MaterialcameraEnhanceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
