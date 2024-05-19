from apysc._material_design.icon.material_arrow_circle_up_outlined_icon import MaterialarrowCircleUpOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarrowCircleUpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarrowCircleUpOutlinedIcon = MaterialarrowCircleUpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
