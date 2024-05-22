from apysc._material_design.icon.material_control_camera_icon import (
    MaterialControlCameraIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialControlCameraIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialControlCameraIcon = MaterialControlCameraIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
