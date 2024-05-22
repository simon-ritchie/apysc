from apysc._material_design.icon.material_fast_forward_icon import (
    MaterialFastForwardIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFastForwardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFastForwardIcon = MaterialFastForwardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
