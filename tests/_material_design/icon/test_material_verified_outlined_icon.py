from apysc._material_design.icon.material_verified_outlined_icon import MaterialverifiedOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialverifiedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialverifiedOutlinedIcon = MaterialverifiedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
