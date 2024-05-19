from apysc._material_design.icon.material_article_outlined_icon import MaterialarticleOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarticleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarticleOutlinedIcon = MaterialarticleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
