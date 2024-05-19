from apysc._material_design.icon.material_remove_circle_icon import (
    MaterialremoveCircleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialremoveCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialremoveCircleIcon = MaterialremoveCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
