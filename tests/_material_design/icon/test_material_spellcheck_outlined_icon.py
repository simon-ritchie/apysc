from apysc._material_design.icon.material_spellcheck_outlined_icon import (
    MaterialspellcheckOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialspellcheckOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialspellcheckOutlinedIcon = MaterialspellcheckOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
