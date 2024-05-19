from apysc._material_design.icon.material_work_outlined_icon import (
    MaterialworkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialworkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialworkOutlinedIcon = MaterialworkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
