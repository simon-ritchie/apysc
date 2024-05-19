from apysc._material_design.icon.material_watch_later_icon import MaterialwatchLaterIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwatchLaterIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwatchLaterIcon = MaterialwatchLaterIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
