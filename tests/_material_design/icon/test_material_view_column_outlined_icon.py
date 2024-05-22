from apysc._material_design.icon.material_view_column_outlined_icon import (
    MaterialViewColumnOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewColumnOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewColumnOutlinedIcon = MaterialViewColumnOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
