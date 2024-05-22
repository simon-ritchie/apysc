from apysc._material_design.icon.material_play_circle_outline_icon import (
    MaterialPlayCircleOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlayCircleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlayCircleOutlineIcon = MaterialPlayCircleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
