from apysc._material_design.icon.material_app_blocking_icon import (
    MaterialAppBlockingIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAppBlockingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAppBlockingIcon = MaterialAppBlockingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
