from apysc._material_design.icon.material_spellcheck_icon import MaterialSpellcheckIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpellcheckIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpellcheckIcon = MaterialSpellcheckIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
