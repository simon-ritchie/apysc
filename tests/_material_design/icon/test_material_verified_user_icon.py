from apysc._material_design.icon.material_verified_user_icon import (
    MaterialverifiedUserIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialverifiedUserIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialverifiedUserIcon = MaterialverifiedUserIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
