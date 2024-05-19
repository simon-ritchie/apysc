from apysc._material_design.icon.material_arrow_circle_down_outlined_icon import MaterialarrowCircleDownOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarrowCircleDownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarrowCircleDownOutlinedIcon = MaterialarrowCircleDownOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
