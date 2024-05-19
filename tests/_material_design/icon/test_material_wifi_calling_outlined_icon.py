from apysc._material_design.icon.material_wifi_calling_outlined_icon import MaterialwifiCallingOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwifiCallingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwifiCallingOutlinedIcon = MaterialwifiCallingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
