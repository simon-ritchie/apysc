from apysc._material_design.icon.material_gavel_outlined_icon import MaterialgavelOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgavelOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgavelOutlinedIcon = MaterialgavelOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
