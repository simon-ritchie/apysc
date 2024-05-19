from apysc._material_design.icon.material_favorite_icon import MaterialfavoriteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfavoriteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfavoriteIcon = MaterialfavoriteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
