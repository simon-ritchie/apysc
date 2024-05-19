from apysc._material_design.icon.material_add_link_icon import MaterialaddLinkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddLinkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddLinkIcon = MaterialaddLinkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
