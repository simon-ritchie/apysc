from apysc._material_design.icon.material_account_circle_icon import (
    MaterialAccountCircleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccountCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccountCircleIcon = MaterialAccountCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
