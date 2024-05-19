from apysc._material_design.icon.material_article_icon import MaterialarticleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialarticleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialarticleIcon = MaterialarticleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
