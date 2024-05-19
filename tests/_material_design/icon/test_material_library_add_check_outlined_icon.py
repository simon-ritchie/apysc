from apysc._material_design.icon.material_library_add_check_outlined_icon import (
    MateriallibraryAddCheckOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryAddCheckOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryAddCheckOutlinedIcon = (
            MateriallibraryAddCheckOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
