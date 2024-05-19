from apysc._material_design.icon.material_person_search_outlined_icon import MaterialpersonSearchOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpersonSearchOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpersonSearchOutlinedIcon = MaterialpersonSearchOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
