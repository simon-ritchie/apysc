from apysc._material_design.icon.material_favorite_outlined_icon import (
    MaterialFavoriteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFavoriteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFavoriteOutlinedIcon = MaterialFavoriteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
