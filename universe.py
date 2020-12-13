import numpy as np

class Singleton:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Universe(Singleton):
    """This class contains all the physical property of UniverseObject and allow quick computation using array instead of loops."""
    instance = None
    positions = None
    directions = None
    speeds = None
    fuels = None
    fuels_consumption = None
    targets = None
    distances_to_target = None

    def __init__(self):
        Singleton.__init__(self)

    def __first_object(self, x, y, direction=0, speed=0, fuel=0, fuel_consumption=0):
        self.positions = np.array([[x, y]])
        self.directions = np.array([direction])
        self.speeds = np.array([speed])
        self.fuels =  np.array([fuel])
        self.fuels_consumption =  np.array([fuel_consumption])

    def add_object(self, x, y, direction=0, speed=0, fuel=0, fuel_consumption=0):
        """Add an object in the universe"""
        if self.positions is None:
            self.__first_object(x, y, direction, speed, fuel, fuel_consumption)
            return 0
        self.positions = np.append(self.positions, [[x, y]], axis=0)
        self.directions = np.append(self.directions, [direction], axis=0)
        self.speeds = np.append(self.speeds, [speed], axis=0)
        self.fuels = np.append(self.fuels, [fuel], axis=0)
        self.fuels_consumption = np.append(self.fuels_consumption, [fuel_consumption], axis=0)
        return len(self.positions) - 1


class ClassUniverseObject:
    """This is the class used to represent any physical object in the universe"""
    def __init__(self, x, y):
        self.id = -1
        self.id = Universe().add_object(x, y)
    
    def x(self):
        return Universe().positions[self.id, 0]
    def y(self):
        return Universe().positions[self.id, 1]
    def position(self):
        return Universe().positions[self.id]


class ClassShip(ClassUniverseObject):
    """This is the class used to represent a ship in the universe."""
    def __init__(self, x, y):
        super().__init__(x, y)

    def fuel(self):
        return Universe().fuels[self.id]
    def fuel_consumption(self):
        return Universe().fuels_consumption[self.id]


if __name__ == "__main__":
    myUniverse = Universe
    myShip = ClassShip(42, 5)
    myBase = ClassShip(10, 10)
    print(myShip.x())

