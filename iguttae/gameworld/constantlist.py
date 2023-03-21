# TODO: Replace with set.
class ConstantList():
    def __init__(self):
        self._list:list[int] = []
        """Internal list of constants"""
        
    def contains(self, constant:int) -> bool:
        """
        Helper function to check if a list has a constant
        
        Args:
            constant (int): constant to check for

        Returns:
            bool: whether constant is in list
        """
        return (constant in self._list)
    
    def add(self, constant:int) -> None:
        """
        Add constant to list if it isn't already there

        Args:
            constant (int): constant to add to list
        """        
        if (not(constant in self._list)):
            self._list.append(constant)
            
    def remove(self, constant:int) -> None:
        """
        Remove constant from list if it's there

        Args:
            constant (int): constant to remove from list
        """        
        if (constant in self._list):
            self._list.remove(constant)
    
    def getIntersectionWith(self, other:"ConstantList") -> "ConstantList":
        """
        Gets the intersection of this constant list with another constant list.

        Args:
            other (ConstantList): the other list to intersect with

        Returns:
            ConstantList: ConstantList containing all common between this one 
                            and that one.
        """        
        ret:"ConstantList" = ConstantList()
        
        for entry in self._list:
            if (other.contains(entry)):
                ret.add(entry)
        
        return ret
    
    def clone(self) -> "ConstantList":
        """
        Clone this list

        Returns:
            ConstantList: a new list that is a clone of this list.
        """        
        ret:"ConstantList" = ConstantList()
        
        for entry in self._list:
            ret.add(entry)
        
        return ret