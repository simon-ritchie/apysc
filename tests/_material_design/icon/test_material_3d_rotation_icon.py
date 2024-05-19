from apysc._material_design.icon.material_3d_rotation_icon import Material3DRotationIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial3DRotationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material3DRotationIcon = Material3DRotationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
