from apysc._material_design.icon.material_backspace_icon import MaterialBackspaceIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBackspaceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBackspaceIcon = MaterialBackspaceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
