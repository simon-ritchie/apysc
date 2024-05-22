from apysc._material_design.icon.material_view_carousel_outlined_icon import (
    MaterialViewCarouselOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewCarouselOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewCarouselOutlinedIcon = MaterialViewCarouselOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
