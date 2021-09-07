from random import randint

from retrying import retry

import apysc as ap
from apysc._type.attr_linking_interface import AttrLinkingInterface


class TestAttrLinkingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_attr_linking_stack(self) -> None:
        interface: AttrLinkingInterface = AttrLinkingInterface()
        interface._initialize_attr_linking_stack()
        assert interface._attr_linking_stack == []
        interface._attr_linking_stack.append(ap.Int(10))
        interface._initialize_attr_linking_stack()
        assert interface._attr_linking_stack == [ap.Int(10)]
