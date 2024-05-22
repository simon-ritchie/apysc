from apysc._material_design.icon.material_thumbs_up_down_outlined_icon import (
    MaterialThumbsUpDownOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialThumbsUpDownOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialThumbsUpDownOutlinedIcon = MaterialThumbsUpDownOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
