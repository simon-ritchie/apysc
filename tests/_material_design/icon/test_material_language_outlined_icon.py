from apysc._material_design.icon.material_language_outlined_icon import (
    MaterialLanguageOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLanguageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLanguageOutlinedIcon = MaterialLanguageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
