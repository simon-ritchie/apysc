from apysc._material_design.icon.material_replay_10_outlined_icon import (
    MaterialReplay10OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReplay10OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReplay10OutlinedIcon = MaterialReplay10OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
