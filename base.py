#! python

from yattag import Doc, indent
from math import sqrt, floor

doc, tag, text = Doc().tagtext()

# dimensions are in "micrometers", although that is not what it renders initially
# We draw the pattern in 1 pixel = 1 µm, then scale it to "actual size" in svg
# SVG, according to the spec, uses 1px = 1/96 inch - https://oreillymedia.github.io/Using_SVG/guide/units.html

inch = 25400  # µm
svgDPI = 96  # dpi convention for svg

# factor to convert from 1µm = 1px to 1in = 96px
conversionFactor = svgDPI / inch


class Pattern:
    def __init__(self, label):
        self.label = label

    def glass(self):
        raise NotImplementedException

    def draw(self):
        raise NotImplementedException

    def scalebar(self):
        """draws a scalebar 100µm by 10µm"""
        with tag("g", ("transform", "translate(2300,2300)")):
            with tag(
                "rect",
                ("width", 100),
                ("height", 10),
                ("fill", "black"),
                ("stroke", "black"),
            ):
                pass

    def toFirefox(self, size=1200):
        with tag(
            "svg",
            ("width", size),
            ("height", size),
            ("version", "1.1"),
            ("xmlns", "http://www.w3.org/2000/svg"),
            ("fill", "white"),
        ):
            with tag(
                "g",
                ("transform", "scale(0.2) translate(3000,3000)"),
                ("fill", "none"),
                ("stroke-width", 1),
                ("stroke", "black"),
            ):
                self.draw()
                self.glass()
                self.scalebar()


def dumpFiles(instance):
    """Dumps a specific instance of roundPattern into a file"""
    # open svg
    svg = instance.getCutPattern()
    # write basic round pattern into round.svg
    # convert to dxf
    # (Human to evaluate shape in browser)


def drawWaferWithFlat():
    flat = 22220
    threeInches = inch * 3
    halfFlat = flat / 2
    # pythagoras for shortening. The radius^2 - halfFlat^2 = shortFromFlat^2
    shortFromFlat = round(
        threeInches / 2 - sqrt((threeInches / 2) ** 2 - halfFlat**2)
    )
    with tag("g", ("transform", "translate(0, {})".format(threeInches / 2))):
        # circle validation
        # with tag('circle', ('cx', 0), ('cy', -threeInches/2), ('r', threeInches/2)):
        #    pass
        with tag(
            "g", ("transform", "translate(0,{})".format(-shortFromFlat))
        ):  # Move middle of circle
            path = " ".join(
                (
                    "M -11110 0 ",
                    "A {} {} 0 1 1 {} 0 ".format(
                        threeInches / 2, threeInches / 2, halfFlat
                    ),
                    "Z",
                )
            )
            with tag("path", ("d", path)):
                pass


if __name__ == "__main__":
    pattern = RoundPattern("t", 100)
    dumpFiles(pattern)
