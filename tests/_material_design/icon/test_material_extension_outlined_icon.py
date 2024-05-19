from apysc._material_design.icon.material_extension_outlined_icon import MaterialextensionOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialextensionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialextensionOutlinedIcon = MaterialextensionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
