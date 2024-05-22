from apysc._material_design.icon.material_thumb_down_off_alt_icon import (
    MaterialThumbDownOffAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialThumbDownOffAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialThumbDownOffAltIcon = MaterialThumbDownOffAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
