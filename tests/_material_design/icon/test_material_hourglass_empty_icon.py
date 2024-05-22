from apysc._material_design.icon.material_hourglass_empty_icon import (
    MaterialHourglassEmptyIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHourglassEmptyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHourglassEmptyIcon = MaterialHourglassEmptyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
