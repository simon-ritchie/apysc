from apysc._material_design.icon.material_favorite_border_icon import (
    MaterialFavoriteBorderIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFavoriteBorderIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFavoriteBorderIcon = MaterialFavoriteBorderIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
