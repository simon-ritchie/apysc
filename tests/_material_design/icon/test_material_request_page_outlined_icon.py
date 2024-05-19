from apysc._material_design.icon.material_request_page_outlined_icon import (
    MaterialrequestPageOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrequestPageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrequestPageOutlinedIcon = MaterialrequestPageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
