from apysc._material_design.icon.material_room_outlined_icon import MaterialroomOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialroomOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialroomOutlinedIcon = MaterialroomOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
