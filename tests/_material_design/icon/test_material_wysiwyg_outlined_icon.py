from apysc._material_design.icon.material_wysiwyg_outlined_icon import (
    MaterialwysiwygOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwysiwygOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwysiwygOutlinedIcon = MaterialwysiwygOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
