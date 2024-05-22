from apysc._material_design.icon.material_view_array_outlined_icon import (
    MaterialViewArrayOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewArrayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewArrayOutlinedIcon = MaterialViewArrayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
