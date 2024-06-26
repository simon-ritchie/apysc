from apysc._material_design.icon.material_translate_outlined_icon import (
    MaterialTranslateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTranslateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTranslateOutlinedIcon = MaterialTranslateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
