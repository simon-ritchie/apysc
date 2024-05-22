from apysc._material_design.icon.material_spellcheck_outlined_icon import (
    MaterialSpellcheckOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpellcheckOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpellcheckOutlinedIcon = MaterialSpellcheckOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
