from apysc._material_design.icon.material_delete_forever_outlined_icon import (
    MaterialdeleteForeverOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdeleteForeverOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdeleteForeverOutlinedIcon = MaterialdeleteForeverOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
