from apysc._material_design.icon.material_work_off_outlined_icon import (
    MaterialworkOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialworkOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialworkOffOutlinedIcon = MaterialworkOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
