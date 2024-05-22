from apysc._material_design.icon.material_add_link_icon import MaterialAddLinkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddLinkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddLinkIcon = MaterialAddLinkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
