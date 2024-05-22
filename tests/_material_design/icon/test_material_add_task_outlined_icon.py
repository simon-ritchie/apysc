from apysc._material_design.icon.material_add_task_outlined_icon import (
    MaterialAddTaskOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddTaskOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddTaskOutlinedIcon = MaterialAddTaskOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
