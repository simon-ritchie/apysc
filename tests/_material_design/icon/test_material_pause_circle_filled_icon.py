from apysc._material_design.icon.material_pause_circle_filled_icon import (
    MaterialpauseCircleFilledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpauseCircleFilledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpauseCircleFilledIcon = MaterialpauseCircleFilledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
