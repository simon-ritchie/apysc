from apysc._material_design.icon.material_query_builder_outlined_icon import (
    MaterialQueryBuilderOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQueryBuilderOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQueryBuilderOutlinedIcon = MaterialQueryBuilderOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
