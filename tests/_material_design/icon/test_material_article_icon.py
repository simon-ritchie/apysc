from apysc._material_design.icon.material_article_icon import MaterialArticleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialArticleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialArticleIcon = MaterialArticleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
