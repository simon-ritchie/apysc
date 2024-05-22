from apysc._material_design.icon.material_wysiwyg_outlined_icon import (
    MaterialWysiwygOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWysiwygOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWysiwygOutlinedIcon = MaterialWysiwygOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
