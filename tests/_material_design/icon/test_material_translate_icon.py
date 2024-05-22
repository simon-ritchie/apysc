from apysc._material_design.icon.material_translate_icon import MaterialTranslateIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTranslateIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTranslateIcon = MaterialTranslateIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
