from apysc._material_design.icon.material_duo_outlined_icon import MaterialduoOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialduoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialduoOutlinedIcon = MaterialduoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
