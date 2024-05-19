from apysc._material_design.icon.material_arrow_circle_up_icon import (
    MaterialarrowCircleUpIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarrowCircleUpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarrowCircleUpIcon = MaterialarrowCircleUpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
