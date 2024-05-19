from apysc._material_design.icon.material_g_translate_icon import MaterialgTranslateIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgTranslateIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgTranslateIcon = MaterialgTranslateIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
