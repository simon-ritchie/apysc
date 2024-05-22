from apysc._material_design.icon.material_not_accessible_icon import (
    MaterialNotAccessibleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNotAccessibleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNotAccessibleIcon = MaterialNotAccessibleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
