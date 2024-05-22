from apysc._material_design.icon.material_gif_outlined_icon import (
    MaterialGifOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGifOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGifOutlinedIcon = MaterialGifOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
