from apysc._material_design.icon.material_bookmark_outlined_icon import MaterialbookmarkOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookmarkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookmarkOutlinedIcon = MaterialbookmarkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
