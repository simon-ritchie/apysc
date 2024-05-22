from apysc._material_design.icon.material_play_arrow_icon import MaterialPlayArrowIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlayArrowIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlayArrowIcon = MaterialPlayArrowIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
