from apysc._material_design.icon.material_find_replace_icon import MaterialfindReplaceIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfindReplaceIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfindReplaceIcon = MaterialfindReplaceIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
