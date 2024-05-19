from apysc._material_design.icon.material_person_search_icon import (
    MaterialpersonSearchIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpersonSearchIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpersonSearchIcon = MaterialpersonSearchIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
