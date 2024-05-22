from apysc._material_design.icon.material_wysiwyg_icon import MaterialWysiwygIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWysiwygIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWysiwygIcon = MaterialWysiwygIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
