from apysc._material_design.icon.material_shuffle_outlined_icon import (
    MaterialshuffleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshuffleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshuffleOutlinedIcon = MaterialshuffleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
