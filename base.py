#! python

import numpy

# dimensions are in "nanometers", although that is not what it renders initially

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


def dumpFiles(instance):
    ''' Dumps a specific instance of roundPattern into a file '''
    # open svg
    svg = instance.getCutPattern()
    # write basic round pattern into round.svg
    # convert to dxf
    # (Human to evaluate shape in browser)

if __name__ == '__main__':
    pattern = RoundPattern('t', 100)
    dumpFiles(pattern)
