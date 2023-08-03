#!python

from yattag import indent
from base import RoundPattern, doc, tag, text
from math import pi, floor


class Spiral(RoundPattern):
    def __init__(self, rg, ri, ro, n):
        '''
        rg: radius of the glass
        ri: inner radius
        ro: outer radius
        innerWidth: width of the narrowest part of the spiral arm
        '''
        self.rg = rg
        self.ri = ri
        self.ro = ro
        # number of spiral arms is determined by the width of the narrowest part of the spiral arm and the diameter of the inner circle
        circumference = 2 * pi * ri
        self.n = n

    def draw(self):
        for i in range(self.n):
            angle = 360/self.n * i
            with tag('g', ('transform', 'rotate({})'.format(angle))):
                with tag('line', ('x1', 0), ('y1', self.ri), ('x2', 0), ('y2', self.ro)):
                    pass


def main():
    s = Spiral(2700, 100, 2500, 20)
    s.toFirefox()
    result = indent(doc.getvalue())
    print(result)

if __name__ == '__main__':
    main()



        
