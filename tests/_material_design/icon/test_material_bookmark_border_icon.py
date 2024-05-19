from apysc._material_design.icon.material_bookmark_border_icon import MaterialbookmarkBorderIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookmarkBorderIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookmarkBorderIcon = MaterialbookmarkBorderIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
