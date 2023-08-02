#! python

import numpy

class RoundPattern():
    ''' Makes a round kirigami pattern at coordinates 0,0 with the specified radius 
        the get methods should return svg strings '''
    def __init__(self, label, radius):
        self.radius = radius
        self.label = label

    def getGlassCircle(self)
        ''' Returns a circle with the specified radius '''
        # This should be implemented here
        throw NotImplementedError

    def getGlassPattern(self):
        ''' Returns the pattern for the glass '''
        # This should be implemented in the subclass
        throw NotImplementedError
