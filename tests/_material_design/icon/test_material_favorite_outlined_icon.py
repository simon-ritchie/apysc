from apysc._material_design.icon.material_favorite_outlined_icon import MaterialfavoriteOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfavoriteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfavoriteOutlinedIcon = MaterialfavoriteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
