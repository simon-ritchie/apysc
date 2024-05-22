from apysc._material_design.icon.material_skip_next_icon import MaterialSkipNextIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSkipNextIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSkipNextIcon = MaterialSkipNextIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
