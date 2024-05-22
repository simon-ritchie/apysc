from apysc._material_design.icon.material_stay_primary_portrait_icon import (
    MaterialStayPrimaryPortraitIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStayPrimaryPortraitIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStayPrimaryPortraitIcon = MaterialStayPrimaryPortraitIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
