from apysc._material_design.icon.material_shuffle_outlined_icon import (
    MaterialShuffleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialShuffleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialShuffleOutlinedIcon = MaterialShuffleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
