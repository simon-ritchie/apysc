from apysc._material_design.icon.material_play_circle_filled_icon import (
    MaterialPlayCircleFilledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlayCircleFilledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlayCircleFilledIcon = MaterialPlayCircleFilledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
