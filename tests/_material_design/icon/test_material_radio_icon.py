from apysc._material_design.icon.material_radio_icon import MaterialradioIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialradioIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialradioIcon = MaterialradioIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
