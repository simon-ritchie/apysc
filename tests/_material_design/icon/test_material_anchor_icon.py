from apysc._material_design.icon.material_anchor_icon import MaterialAnchorIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAnchorIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAnchorIcon = MaterialAnchorIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
