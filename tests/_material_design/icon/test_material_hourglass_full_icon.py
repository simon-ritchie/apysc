from apysc._material_design.icon.material_hourglass_full_icon import (
    MaterialHourglassFullIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHourglassFullIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHourglassFullIcon = MaterialHourglassFullIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
