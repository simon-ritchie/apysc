from apysc._material_design.icon.material_web_icon import MaterialwebIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwebIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwebIcon = MaterialwebIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
