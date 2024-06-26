from apysc._material_design.icon.material_stop_circle_outlined_icon import (
    MaterialStopCircleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStopCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStopCircleOutlinedIcon = MaterialStopCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
