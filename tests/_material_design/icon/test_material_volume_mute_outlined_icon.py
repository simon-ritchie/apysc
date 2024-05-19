from apysc._material_design.icon.material_volume_mute_outlined_icon import (
    MaterialvolumeMuteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvolumeMuteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvolumeMuteOutlinedIcon = MaterialvolumeMuteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
