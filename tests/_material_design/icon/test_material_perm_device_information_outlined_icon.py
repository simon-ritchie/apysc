from apysc._material_design.icon.material_perm_device_information_outlined_icon import MaterialpermDeviceInformationOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermDeviceInformationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermDeviceInformationOutlinedIcon = MaterialpermDeviceInformationOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
