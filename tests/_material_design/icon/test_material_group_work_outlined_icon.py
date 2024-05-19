from apysc._material_design.icon.material_group_work_outlined_icon import (
    MaterialgroupWorkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgroupWorkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgroupWorkOutlinedIcon = MaterialgroupWorkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
