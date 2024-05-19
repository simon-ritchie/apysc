from apysc._material_design.icon.material_favorite_border_outlined_icon import MaterialfavoriteBorderOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfavoriteBorderOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfavoriteBorderOutlinedIcon = MaterialfavoriteBorderOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
