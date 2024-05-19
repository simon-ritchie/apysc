from apysc._material_design.icon.material_pause_circle_outline_icon import MaterialpauseCircleOutlineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpauseCircleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpauseCircleOutlineIcon = MaterialpauseCircleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
