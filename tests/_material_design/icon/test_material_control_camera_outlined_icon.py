from apysc._material_design.icon.material_control_camera_outlined_icon import (
    MaterialControlCameraOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialControlCameraOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialControlCameraOutlinedIcon = MaterialControlCameraOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
