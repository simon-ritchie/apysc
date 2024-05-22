from apysc._material_design.icon.material_more_time_icon import MaterialMoreTimeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMoreTimeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMoreTimeIcon = MaterialMoreTimeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
