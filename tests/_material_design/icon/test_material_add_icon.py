from apysc._material_design.icon.material_add_icon import MaterialaddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddIcon = MaterialaddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
