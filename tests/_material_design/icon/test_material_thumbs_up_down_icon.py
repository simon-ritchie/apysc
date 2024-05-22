from apysc._material_design.icon.material_thumbs_up_down_icon import (
    MaterialThumbsUpDownIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialThumbsUpDownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialThumbsUpDownIcon = MaterialThumbsUpDownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
