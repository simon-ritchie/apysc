from apysc._material_design.icon.material_view_headline_icon import MaterialviewHeadlineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewHeadlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewHeadlineIcon = MaterialviewHeadlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
