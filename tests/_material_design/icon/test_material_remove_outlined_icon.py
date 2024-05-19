from apysc._material_design.icon.material_remove_outlined_icon import MaterialremoveOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialremoveOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialremoveOutlinedIcon = MaterialremoveOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
