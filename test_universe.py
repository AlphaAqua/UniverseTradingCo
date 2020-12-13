from universe import *

class TestClass:
    def test_creation(self):
        myShip = ClassShip(42, 5)
        myBase = ClassShip(10, 11)
        assert myShip.x() == 42
        assert myShip.y() == 5
        assert myBase.x() == 10
        assert myBase.y() == 11

