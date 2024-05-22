from apysc._material_design.icon.material_person_search_outlined_icon import (
    MaterialPersonSearchOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPersonSearchOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPersonSearchOutlinedIcon = MaterialPersonSearchOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
