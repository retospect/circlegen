from yattag import indent
from yattag import Doc
from math import pi, floor

doc, tag, text = Doc().tagtext()

class spiral:
    def __init__(self, rg, ri, ro, innerWidth=20, cutwidth=10):
        '''
        rg: radius of the glass
        ri: inner radius
        ro: outer radius
        innerWidth: width of the narrowest part of the spiral arm
        '''
        self.ri = ri
        self.ro = ro
        # number of spiral arms is determined by the width of the narrowest part of the spiral arm and the diameter of the inner circle
        circumference = 2 * pi * ri
        self.n = floor(circumference / (innerWidth+cutwidth))

    def draw(self):
        for i in range(self.n):
            angle = 360/self.n * i
            with tag('g', ('transform', 'rotate({})'.format(angle))):
                with tag('line', ('x1', 0), ('y1', self.ri), ('x2', 0), ('y2', self.ro)):
                    pass

    def glass(self):
        ''' draws the glass cutout '''
        with tag('circle', ('cx', 0), ('cy', 0), ('r', self.rg), ('fill', 'transparent'), ('stroke', 'red')):
            pass

def main():
    s = spiral(270, 100, 250, 30)
    with tag('svg', ('width', 600), ('height', 600), ('version', '1.1'), ('xmlns', 'http://www.w3.org/2000/svg'), ('fill', 'white')):
        with tag('g', ('transform', 'translate(300 300)'), ('fill', 'none'), ('stroke-width', 1), ('stroke', 'black')):
            s.draw()
            
    result = indent(doc.getvalue())
    print(result)

if __name__ == '__main__':
    main()



        
