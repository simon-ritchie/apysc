from apysc._material_design.icon.material_dialpad_outlined_icon import MaterialdialpadOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdialpadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdialpadOutlinedIcon = MaterialdialpadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
