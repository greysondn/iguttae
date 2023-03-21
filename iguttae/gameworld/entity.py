from constantlist import ConstantList
from constants import Constants

from typing import cast

class Entity():
    """
    Base class for all world entities in Iguttae
    """
    def __init__(self):
        self.containableIn:ConstantList = ConstantList()
        """
        The types of containers this is containable in
        """
        
        self.consts:Constants = Constants.create()
        """
        Access point for constants
        """
        
        self.aliases:list[str] = []
        """
        Aliases for this object - as in things it answers to
        """
        
        self.isUnique:bool = False
        """
        Whether this is unique or not. Mostly matters for items, honestly.
        """
        
        self.index:int = cast(int, None)
        """
        Index, for indexed actors. This is considered undefined for arbitrary
        actors, but some - like rooms and transitions - are actually indexed.
        """
        
        self.isPlayer:bool = False
        """
        Whether or not this is the player
        """
        
        self.cloneCount:int = 0
        """
        Spawn count. Again, mostly matters for items.
        """
        
        self.isClone:bool = False
        """
        Whether this is a clone or not. Don't clone clones brah.
        """
        
        self.name:str = "ERROR: NO NAME"
        """
        Name of this actor
        """

    def __lt__(self, other:"Entity") -> bool:
        """
        Compare actors based on indexes. Compatible with most sorts in Python.

        Args:
            other (Entity): Another entity

        Returns:
            bool: self < other
        """
        return (self.index < other.index)
    
    def addAlias(self, alias:str) -> None:
        self.aliases.append(alias)
        
    def answersTo(self, alias:str) -> bool:
        ret:bool = False
        
        for entry in self.aliases:
            if (entry.lower() == alias.lower()):
                ret = True
                
        return ret
    
    def canClone(self) -> bool:
        """Whether or not we can clone this

        Returns:
            bool: true if we can, false if we can't
        """
        
        # generally, we can
        ret:bool = True
        
        # However, if it's unique and one is spawned already, we can't
        if (self.isUnique):
            if (self.cloneCount >= 1):
                ret = False
        
        # shouldn't be cloning clones, either
        if (self.isClone):
            ret = False
        
        # end
        return ret
    
    def clone(self) -> "Entity":
        """
        As in this is just a prototype with frills. Make sure you canClone()
        first. This won't try to stop you if you fail to check for yourself!

        Returns:
            Entity: a clone of this entity.
        """
        ret:"Entity" = Entity()
        
        # containableIn
        ret.containableIn = self.containableIn.clone()
        
        # clone count
        self.cloneCount = self.cloneCount + 1
        ret.cloneCount = self.cloneCount
        
        # index
        ret.index = self.index
        
        # isClone = we aren't but ret is
        ret.isClone = True
        
        # name
        ret.name = self.name

        # unique
        ret.isUnique = self.isUnique
        
        # aliases
        ret.aliases = self.aliases.copy() # that's a shallow copy!
        
        # return
        return ret
    
    