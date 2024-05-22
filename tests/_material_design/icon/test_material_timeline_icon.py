from apysc._material_design.icon.material_timeline_icon import MaterialTimelineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTimelineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTimelineIcon = MaterialTimelineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
