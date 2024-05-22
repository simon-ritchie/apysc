from apysc._material_design.icon.material_play_for_work_outlined_icon import (
    MaterialPlayForWorkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlayForWorkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlayForWorkOutlinedIcon = MaterialPlayForWorkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
