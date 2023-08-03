#! python

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

# dimensions are in "nanometers", although that is not what it renders initially

class Pattern():
    def __init__(self, label):
        self.label = label
    def glass(self):
        raise NotImplementedException
    def draw(self):
        raise NotImplementedException

class RoundPattern(Pattern):
    ''' Makes a round kirigami pattern at coordinates 0,0 with the specified radius 
        the get methods should return svg strings '''
    def __init__(self, label, radius):
        self.radius = radius
        self.label = label


    def glass(self):
        ''' draws the glass cutout '''
        with tag('circle', ('cx', 0), ('cy', 0), ('r', self.rg), ('fill', 'transparent'), ('stroke', 'red')):
            pass

    def scalebar(self):
        ''' draws a scalebar 100µm by 10µm'''
        with tag('g', ('transform', 'translate(2300,2300)')):
            with tag('rect', ('width', 100), ('height', 10), ('fill', 'black'), ('stroke', 'black')):
                pass

    def toFirefox(self):
        with tag('svg', ('width', 1200), ('height', 1200), ('version', '1.1'), ('xmlns', 'http://www.w3.org/2000/svg'), ('fill', 'white')):
            with tag('g', ('transform', 'scale(0.2) translate(3000,3000)'), ('fill', 'none'), ('stroke-width', 1), ('stroke', 'black')):
                self.draw()
                self.glass()
                self.scalebar()


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
