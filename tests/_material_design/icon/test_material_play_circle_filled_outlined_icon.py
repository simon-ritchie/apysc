from apysc._material_design.icon.material_play_circle_filled_outlined_icon import MaterialplayCircleFilledOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplayCircleFilledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplayCircleFilledOutlinedIcon = MaterialplayCircleFilledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
