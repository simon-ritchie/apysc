from apysc._material_design.icon.material_hd_icon import MaterialhdIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhdIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhdIcon = MaterialhdIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
