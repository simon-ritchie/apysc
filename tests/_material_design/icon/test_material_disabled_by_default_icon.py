from apysc._material_design.icon.material_disabled_by_default_icon import (
    MaterialDisabledByDefaultIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDisabledByDefaultIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDisabledByDefaultIcon = MaterialDisabledByDefaultIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
