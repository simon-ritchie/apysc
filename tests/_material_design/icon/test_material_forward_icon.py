from apysc._material_design.icon.material_forward_icon import MaterialforwardIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforwardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialforwardIcon = MaterialforwardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
