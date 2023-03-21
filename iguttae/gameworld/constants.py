from typing import cast

class Constants():
    '''
    Singleton class of constants for actors
    '''
    
    _instance:"Constants" = cast("Constants", None)
    '''
    The only instance of this class
    '''
    
    @classmethod
    def create(cls) -> "Constants":
        """
        Call this to ostensibly crate a new constants.

        Returns:
            Constants: ostensibly new Constants
        """
        if Constants._instance == None:
            Constants._instance = Constants()
        return Constants._instance

    def __init__(self):
        '''
        DON'T USE THIS. USE CREATE INSTEAD.
        
        The original constructor was private!
        '''
        
        self._prefixes:list[str] = [
            "container",
            "flag",
            "permission",
            "slot"
        ]
        '''
        Valid strings to use as prefixes for constants.
        
        TODO: Externalize this to a file.
        '''
        
        self._keyList:list[str] = [
        # ----------
        # containers
        # ----------
        #
        # whether this is a room/able to be contained in a room
        "container.room",
        # whether this is a stomach/able to be contained in a stomach
        "container.stomach",
        # whether this is storage/able to be contained in storage
        "container.storage",
        # whether this has an inventory/is able to be contained in an inventory
        "container.inventory",
        # -----
        # flags
        # -----
        #
        # whether an actor is edible
        "flag.edible",
        # whether this area is public
        "flag.public",
        # whether a passage is hidden
        "flag.hidden",
        # whether something is locked
        "flag.locked",
        # whether something operates on a timer
        "flag.timer",
        # -----------
        # permissions
        # -----------
        #
        # whether or not an actor can wait and if waiting is allowed here
        "permission.wait",
        # -----
        # slots
        # -----
        # Either this means that such equipment slots exist
        # OR
        # that such a thing can be equipped in an equipment slot
        # OR
        # that this entry represents the given equipment slot.

        # the left ring finger - or the only ring slot
        # if you're playing classic.
        "slot.ringLeftRing",

        # a one handed weapon
        "slot.weapon.onehanded",

        # a two handed weapon
        "slot.weapon.twohanded",

        # the torso armor - or the only armor slot
        # if you're playing classic.
        "slot.armor.torso"
        ]
        '''
        List of actual constants.
        
        TODO: Externalize this to a file.
        '''
        
        def exists(self, prefix:str, key:str) -> bool:
            """
            Checks whether the prefix and key even exists

            Args:
                prefix (str): prefix for key
                key (str): key itself

            Returns:
                bool: whether it even exists
            """
            # eventual return
            ret:bool = True
            
            if (not (self._prefixes.contains(prefix))):
                ret = False
            else:
                swp = prefix + "." + key
                if (not (self.keyList.contains(swp))):
                    ret = False
                    
            return ret
        
        def get(self, prefix:str, key:str) -> int:
            """
            Gives some consistent value that can be used for the key with prefix
            
            For now these are ints. Later on I might get more clever with them.

            Args:
                prefix (str): prefix for key
                key (str): key itself

            Returns:
                int: a stable value for prefix.key
            """
            
            # the impossible value returns!
            ret:int = -1
            
            if (self.exists(key, prefix)):
                ret = self._keylist.index(prefix + "." + key)
            else:
                # yeah, that qualifies as a major error
                raise ValueError("Invalid constant key asked for! : " + prefix + "." + key)
            
            return ret
        
        def intToKey(self, incoming:int) -> str:
            """
            Convert int to key string (future proofed storage)

            Args:
                incoming (int): int for const

            Returns:
                str: string
            """            
            return self._keyList[incoming]
        
        def keyToInt(self, incoming:str) -> int:
            """
            Converts key string to int (future proofed storage)

            Args:
                incoming (str): key string for const

            Returns:
                int: int
            """            
            return self._keyList.index(incoming)