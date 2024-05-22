from apysc._material_design.icon.material_favorite_icon import MaterialFavoriteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFavoriteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFavoriteIcon = MaterialFavoriteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
