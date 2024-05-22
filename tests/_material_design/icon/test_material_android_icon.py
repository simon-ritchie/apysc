from apysc._material_design.icon.material_android_icon import MaterialAndroidIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAndroidIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAndroidIcon = MaterialAndroidIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
