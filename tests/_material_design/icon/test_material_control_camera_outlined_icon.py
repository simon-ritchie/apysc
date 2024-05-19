from apysc._material_design.icon.material_control_camera_outlined_icon import MaterialcontrolCameraOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontrolCameraOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontrolCameraOutlinedIcon = MaterialcontrolCameraOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
