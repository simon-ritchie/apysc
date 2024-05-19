from apysc._material_design.icon.material_replay_circle_filled_icon import (
    MaterialreplayCircleFilledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplayCircleFilledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreplayCircleFilledIcon = MaterialreplayCircleFilledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
