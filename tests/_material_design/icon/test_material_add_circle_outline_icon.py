from apysc._material_design.icon.material_add_circle_outline_icon import (
    MaterialaddCircleOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddCircleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddCircleOutlineIcon = MaterialaddCircleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
