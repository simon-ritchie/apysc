from apysc._material_design.icon.material_library_add_check_icon import (
    MateriallibraryAddCheckIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryAddCheckIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryAddCheckIcon = MateriallibraryAddCheckIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
