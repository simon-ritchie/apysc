from apysc._material_design.icon.material_work_outline_outlined_icon import MaterialworkOutlineOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialworkOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialworkOutlineOutlinedIcon = MaterialworkOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
