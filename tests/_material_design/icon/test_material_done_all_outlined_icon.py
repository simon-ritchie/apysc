from apysc._material_design.icon.material_done_all_outlined_icon import (
    MaterialDoneAllOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDoneAllOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDoneAllOutlinedIcon = MaterialDoneAllOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
