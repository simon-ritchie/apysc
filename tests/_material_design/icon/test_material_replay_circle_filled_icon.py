from apysc._material_design.icon.material_replay_circle_filled_icon import (
    MaterialReplayCircleFilledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplayCircleFilledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplayCircleFilledIcon = MaterialReplayCircleFilledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
