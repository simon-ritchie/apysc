from apysc._material_design.icon.material_contactless_icon import MaterialcontactlessIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactlessIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactlessIcon = MaterialcontactlessIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
