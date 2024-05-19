from apysc._material_design.icon.material_hourglass_top_icon import MaterialhourglassTopIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhourglassTopIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhourglassTopIcon = MaterialhourglassTopIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
