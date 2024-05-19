from apysc._material_design.icon.material_send_outlined_icon import MaterialsendOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsendOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsendOutlinedIcon = MaterialsendOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
