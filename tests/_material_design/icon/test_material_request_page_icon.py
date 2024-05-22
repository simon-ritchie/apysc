from apysc._material_design.icon.material_request_page_icon import (
    MaterialRequestPageIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRequestPageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRequestPageIcon = MaterialRequestPageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
