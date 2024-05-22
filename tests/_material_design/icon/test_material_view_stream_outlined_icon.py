from apysc._material_design.icon.material_view_stream_outlined_icon import (
    MaterialViewStreamOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewStreamOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewStreamOutlinedIcon = MaterialViewStreamOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
