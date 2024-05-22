from apysc._material_design.icon.material_rtt_icon import MaterialRttIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRttIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRttIcon = MaterialRttIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
