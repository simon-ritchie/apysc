from apysc._material_design.icon.material_play_disabled_icon import MaterialplayDisabledIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplayDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplayDisabledIcon = MaterialplayDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
