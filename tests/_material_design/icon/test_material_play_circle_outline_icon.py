from apysc._material_design.icon.material_play_circle_outline_icon import (
    MaterialplayCircleOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplayCircleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplayCircleOutlineIcon = MaterialplayCircleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
