from apysc._material_design.icon.material_group_work_outlined_icon import (
    MaterialGroupWorkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGroupWorkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGroupWorkOutlinedIcon = MaterialGroupWorkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
