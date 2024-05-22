from apysc._material_design.icon.material_view_carousel_icon import (
    MaterialViewCarouselIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewCarouselIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewCarouselIcon = MaterialViewCarouselIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
