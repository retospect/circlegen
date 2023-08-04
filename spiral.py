#! python
from yattag import indent
from base import RoundPattern, doc, tag, text
from math import pi, floor
from svg.path import Path, Move, Line, Arc, CubicBezier, QuadraticBezier, Close

def arc(x, y, r, start, end):
    return Arc(r, r, 0, False, False, start, end)

class Spiral(RoundPattern):
    def __init__(self, rg, ri, ro, n, cw=10):
        '''
        rg: radius of the glass
        ri: inner radius
        ro: outer radius
        innerWidth: width of the narrowest part of the spiral arm
        n: number of spiral arms
        cw: cut width
        '''
        self.rg = rg
        self.ri = ri
        self.ro = ro
        self.mr = (ri+ro)/2
        self.cw = cw
        # number of spiral arms is determined by the width of the narrowest part of the spiral arm and the diameter of the inner circle
        circumference = 2 * pi * ri
        self.n = n 

    def draw(self):
        for i in range(self.n):
            angle = 360/self.n * i
            with tag('g', ('transform', 'rotate({})'.format(angle))):
                # uses svg.path to draw a spiral
                cw = self.cw
                ch = int(cw/2)
                ri = self.ri
                ro = self.ro

                path = ' '.join( ("M {} {} ".format(ri, -ch),
                            "A {} {} 0 0 1 {} {} ".format(1,1, 0, ro+ch),
                            "L {} {} ".format(0, ro-ch), 
                            "A {} {} 180 1 0 {} {} ".format(1,1, ri, ch),
                            "Z"))
                with tag('path', ('d', path)):
                    pass


def main():
    s = Spiral(2700, 100, 2500, 6)
    s.toFirefox()
    result = indent(doc.getvalue())
    print(result)

if __name__ == '__main__':
    main()



        
