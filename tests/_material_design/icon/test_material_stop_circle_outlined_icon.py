from apysc._material_design.icon.material_stop_circle_outlined_icon import (
    MaterialstopCircleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstopCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstopCircleOutlinedIcon = MaterialstopCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
