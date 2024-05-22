from apysc._material_design.icon.material_perm_camera_mic_outlined_icon import (
    MaterialPermCameraMicOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermCameraMicOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermCameraMicOutlinedIcon = MaterialPermCameraMicOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
