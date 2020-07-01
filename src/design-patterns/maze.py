# "enum", or enumeration, allows names to be directly assigned
# to numbers underneath the hood.
from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError('Abstract Base Class method')
    
class Direction(Enum):
    North = 0
    East  = 1
    South = 2
    West  = 3
    
class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)
        
    def GetSide(self, Direction):
        return self._sides[Direction]
    
    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite
        
    def Enter(self):
        print('    You have entered room: ' + str(self._roomNumber))
        
class Wall(MapSite):
    def Enter(self):
        print('    * You just ran into a Wall...')    

class Door(MapSite):
    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False
        
    # Figures out what Room is on the other side of the Door.
    def OtherSideFrom(self, Room):
        print('\tDoor obj: This door is a side of Room: {}'.format(Room._roomNumber))
        if 1 == Room._roomNumber: 
            other_room = self._room2
        else: 
            other_room = self._room1        
        return other_room
        
    def Enter(self):
        if self._isOpen: print('    **** You have passed through this door...')
        else: print('    ** This door needs to be opened before you can pass through it...')

class Maze():
    def __init__(self):
        # Dictionary to hold room_number, room_obj <key, value> pairs
        self._rooms = {}
    
    def AddRoom(self, room):
        # Use roomNumber as lookup value to retrieve room object
        self._rooms[room._roomNumber] = room    
    
    def RoomNo(self, room_number):
        return self._rooms[room_number]
    
class MazeGame():
    def CreateMaze(self):
        aMaze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        # Doors require two rooms as arguments.
        theDoor = Door(r1, r2)
        
        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)
        
        r1.SetSide(Direction.North.value, Wall())
        r1.SetSide(Direction.East.value, theDoor)
        r1.SetSide(Direction.South.value, Wall())
        r1.SetSide(Direction.West.value, Wall())
        
        r2.SetSide(Direction(0).value, Wall())
        r2.SetSide(Direction(1).value, Wall())
        r2.SetSide(Direction(2).value, Wall())
        r2.SetSide(Direction(3).value, theDoor)
        
        return aMaze
