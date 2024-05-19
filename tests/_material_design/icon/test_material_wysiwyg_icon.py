from apysc._material_design.icon.material_wysiwyg_icon import MaterialwysiwygIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwysiwygIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwysiwygIcon = MaterialwysiwygIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
