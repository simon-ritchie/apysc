from apysc._material_design.icon.material_volume_mute_outlined_icon import (
    MaterialVolumeMuteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVolumeMuteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVolumeMuteOutlinedIcon = MaterialVolumeMuteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
