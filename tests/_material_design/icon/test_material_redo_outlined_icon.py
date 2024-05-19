from apysc._material_design.icon.material_redo_outlined_icon import (
    MaterialredoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialredoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialredoOutlinedIcon = MaterialredoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
