from apysc._material_design.icon.material_block_outlined_icon import (
    MaterialBlockOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBlockOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBlockOutlinedIcon = MaterialBlockOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
