from apysc._material_design.icon.material_g_translate_outlined_icon import (
    MaterialGTranslateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGTranslateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGTranslateOutlinedIcon = MaterialGTranslateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
