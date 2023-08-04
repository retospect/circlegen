from yattag import indent
from yattag import Doc
from math import sqrt, floor

from base import doc, tag, text
from spiral import Spiral


threeInches = int(25.4*1000*3)
def getOffsets(patternSquare=7500):
    maxOffset = floor(threeInches/2/patternSquare)
    for x in range(-maxOffset, maxOffset+1):
        for y in range(-maxOffset, maxOffset+1):
            radius = threeInches/2-1000 # leave a 5mm rim
            # if all the corners are inside the circle, then the square is inside the circle
            if (x*patternSquare)**2 + (y*patternSquare)**2 < radius**2 and \
                ((x+1)*patternSquare)**2 + (y*patternSquare)**2 < radius**2 and \
                ((x+1)*patternSquare)**2 + ((y+1)*patternSquare)**2 < radius**2 and \
                (x*patternSquare)**2 + ((y+1)*patternSquare)**2 < radius**2:
                yield (x,y)

def main():
    with tag('svg', ('width', 80000), ('height', 80000), ('version', '1.1'), ('xmlns', 'http://www.w3.org/2000/svg')):
        with tag('g', ('transform', 'translate(40000 40000)'), ('fill', 'none'), ('stroke-width', 100), ('stroke', 'black')):
            flat = 22220
            halfFlat = flat/2
            # pythagoras for shortening. The radius^2 - halfFlat^2 = shortFromFlat^2
            shortFromFlat = round(threeInches/2-sqrt((threeInches/2)**2 - halfFlat**2))
            with tag('g', ('transform', 'translate(0, {})'.format(threeInches/2))):
                # circle validation
                # with tag('circle', ('cx', 0), ('cy', -threeInches/2), ('r', threeInches/2)):
                #    pass
                with tag('g', ('transform', 'translate(0,{})'.format(-shortFromFlat))): # Move middle of circle
                    path = ' '.join( ("M -11110 0 ",
                                "A {} {} 0 1 1 {} 0 ".format(threeInches/2, threeInches/2, halfFlat),
                                "Z"))
                    with tag('path', ('d', path)):
                        pass
            patternSquare = 7500
            for (x,y) in getOffsets(patternSquare):
                with tag('g', ('transform', 'translate({}, {})'.format(x*patternSquare, y*patternSquare))):
                    #with tag('rect', ('x', 0), ('y', 0), ('width', patternSquare), ('height', patternSquare)):
                    #    pass
                    with tag('g', ('transform', 'translate({}, {})'.format(patternSquare/2, patternSquare/2))):
                        s = Spiral(2700,100,2500,3)
                        with tag('g', ('stroke-width', 1)):
                            s.draw()
                        with tag('g', ('stroke', 'red')):
                            s.glass()

    result = indent(doc.getvalue())
    print(result)

if __name__ == '__main__':
    main()



        
