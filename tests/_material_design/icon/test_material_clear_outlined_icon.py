from apysc._material_design.icon.material_clear_outlined_icon import MaterialclearOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclearOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclearOutlinedIcon = MaterialclearOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
