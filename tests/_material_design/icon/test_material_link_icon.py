from apysc._material_design.icon.material_link_icon import MaterialLinkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLinkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLinkIcon = MaterialLinkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
