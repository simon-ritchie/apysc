from apysc._material_design.icon.material_perm_camera_mic_icon import (
    MaterialpermCameraMicIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermCameraMicIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermCameraMicIcon = MaterialpermCameraMicIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
