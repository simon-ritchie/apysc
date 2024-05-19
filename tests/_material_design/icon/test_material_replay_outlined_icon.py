from apysc._material_design.icon.material_replay_outlined_icon import (
    MaterialreplayOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreplayOutlinedIcon = MaterialreplayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
