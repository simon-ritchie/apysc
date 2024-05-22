from apysc._material_design.icon.material_replay_30_outlined_icon import (
    MaterialReplay30OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplay30OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplay30OutlinedIcon = MaterialReplay30OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
