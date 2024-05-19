from apysc._material_design.icon.material_more_time_icon import MaterialmoreTimeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmoreTimeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmoreTimeIcon = MaterialmoreTimeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
