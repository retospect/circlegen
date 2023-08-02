#! python

import base

class SpiralPattern(RoundPattern):
    ''' Makes a round kirigami pattern at coordinates 0,0 with the specified radius 
        the get methods should return svg strings '''
    def __init__(self, label, radius, innerRadius, armAngle, nrSpirals, widthOfCut):
        '''
        radius: the radius of the outer circle
        innerRadius: the radius of the inner circle, where the spiral ends
        armAngle: the angle of the spiral arms, how far around it goes
        nrSpirals: the number of spiral arms
        widthOfCut: the width of the cut that separates the spirals
        '''
        super().__init__(label, radius);
        self.innerRadius = innerRadius
        self.armAngle = armAngle
        self.nrSpirals = nrSpirals
        self.widthOfCut = widthOfCut
        self.armLength = self.radius - self.innerRadius
        self.armWidth = self.armLength * math.tan(self.armAngle)


    def getCutPattern(self):
        ''' Returns the pattern for the glass '''
        # This should be implemented in the subclass
        throw NotImplementedError



if __name__ == '__main__':
    pattern = SpiralPattern('t', 100)
    dumpFiles(pattern)
