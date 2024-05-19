from apysc._material_design.icon.material_add_circle_outlined_icon import MaterialaddCircleOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddCircleOutlinedIcon = MaterialaddCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
