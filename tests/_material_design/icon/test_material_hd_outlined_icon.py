from apysc._material_design.icon.material_hd_outlined_icon import MaterialhdOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhdOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhdOutlinedIcon = MaterialhdOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
