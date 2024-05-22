from apysc._material_design.icon.material_watch_later_outlined_icon import (
    MaterialWatchLaterOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWatchLaterOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWatchLaterOutlinedIcon = MaterialWatchLaterOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
