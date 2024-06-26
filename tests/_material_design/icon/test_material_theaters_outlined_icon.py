from apysc._material_design.icon.material_theaters_outlined_icon import (
    MaterialTheatersOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTheatersOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTheatersOutlinedIcon = MaterialTheatersOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
