from apysc._material_design.icon.material_rtt_icon import MaterialrttIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrttIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrttIcon = MaterialrttIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
