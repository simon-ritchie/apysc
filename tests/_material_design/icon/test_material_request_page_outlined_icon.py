from apysc._material_design.icon.material_request_page_outlined_icon import (
    MaterialRequestPageOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRequestPageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRequestPageOutlinedIcon = MaterialRequestPageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
