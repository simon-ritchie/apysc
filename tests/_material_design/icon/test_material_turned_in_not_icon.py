from apysc._material_design.icon.material_turned_in_not_icon import (
    MaterialTurnedInNotIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTurnedInNotIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTurnedInNotIcon = MaterialTurnedInNotIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
