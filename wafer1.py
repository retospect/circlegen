from yattag import indent
from yattag import Doc

from math import sqrt, floor
from base import doc, tag, text, inch, conversionFactor, drawWaferWithFlat
from spiral import Spiral

threeInches = int(inch * 3)


def getOffsets(patternSquare=7500):
    maxOffset = floor(threeInches / 2 / patternSquare)
    for y in range(-maxOffset, maxOffset + 1):
        for x in range(-maxOffset, maxOffset + 1):
            radius = threeInches / 2 - 1000  # leave a 5mm rim
            # if all the corners are inside the circle, then the square is inside the circle
            if (
                (x * patternSquare) ** 2 + (y * patternSquare) ** 2 < radius**2
                and ((x + 1) * patternSquare) ** 2 + (y * patternSquare) ** 2
                < radius**2
                and ((x + 1) * patternSquare) ** 2 + ((y + 1) * patternSquare) ** 2
                < radius**2
                and (x * patternSquare) ** 2 + ((y + 1) * patternSquare) ** 2
                < radius**2
            ):
                yield (x, y)


def makeWafer(rounds, show_wafer=False, show_glass=False, show_cuts=False):
    with tag("g", ("transform", "translate(40000 40000))")):
        if show_wafer:
            drawWaferWithFlat()
        patternSquare = 7500
        coords = getOffsets(patternSquare)
        for circular in rounds:
            x, y = next(coords)
            with tag(
                "g",
                (
                    "transform",
                    "translate({}, {})".format(x * patternSquare, y * patternSquare),
                ),
            ):
                # with tag('rect', ('x', 0), ('y', 0), ('width', patternSquare), ('height', patternSquare)):
                #    pass
                with tag(
                    "g",
                    (
                        "transform",
                        "translate({}, {})".format(
                            patternSquare / 2, patternSquare / 2
                        ),
                    ),
                ):
                    s = Spiral(2700, 100, 2500, 3)
                    with tag("g", ("stroke-width", 1)):
                        if show_glass:
                            circular.glass()
                        if show_cuts:
                            circular.draw()


def main():
    with tag(
        "svg",
        ("width", "6in"),
        ("height", "6in"),
        ("version", "1.1"),
        ("xmlns", "http://www.w3.org/2000/svg"),
    ):
        with tag("g", ("fill", "none"), ("stroke-width", 100), ("stroke", "black")):
            with tag(
                "g",
                (
                    "transform",
                    "scale({} {})".format(conversionFactor, conversionFactor),
                ),
            ):
                spirals = []
                for i in range(26):
                    spirals.append(Spiral(2700, 100, 2500, i + 1))

                with tag("g", ("transform", "translate(47000 105000)")):
                    makeWafer(spirals, show_glass=True, show_wafer=True)
                with tag("g", ("transform", "translate(105000 47000)")):
                    # Mirror it because it's going on the back!
                    with tag("g", ("transform", "scale(-1,1)")):
                        makeWafer(spirals, show_cuts=True, show_wafer=True)

    result = indent(doc.getvalue())
    print(result)


if __name__ == "__main__":
    main()
