from apysc._material_design.icon.material_backspace_icon import MaterialbackspaceIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbackspaceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbackspaceIcon = MaterialbackspaceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
