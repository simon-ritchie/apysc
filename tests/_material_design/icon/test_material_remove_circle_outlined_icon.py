from apysc._material_design.icon.material_remove_circle_outlined_icon import MaterialremoveCircleOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialremoveCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialremoveCircleOutlinedIcon = MaterialremoveCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
