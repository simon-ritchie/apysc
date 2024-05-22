from apysc._material_design.icon.material_segment_icon import MaterialSegmentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSegmentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSegmentIcon = MaterialSegmentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
