from apysc._material_design.icon.material_view_carousel_icon import (
    MaterialviewCarouselIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewCarouselIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewCarouselIcon = MaterialviewCarouselIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
