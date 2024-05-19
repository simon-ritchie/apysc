from apysc._material_design.icon.material_language_outlined_icon import MateriallanguageOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallanguageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallanguageOutlinedIcon = MateriallanguageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
