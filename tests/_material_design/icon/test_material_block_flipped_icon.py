from apysc._material_design.icon.material_block_flipped_icon import (
    MaterialBlockFlippedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBlockFlippedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBlockFlippedIcon = MaterialBlockFlippedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
