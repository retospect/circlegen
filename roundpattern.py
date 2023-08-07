#! python

from yattag import indent
from base import doc, tag, text, Pattern


class RoundPattern(Pattern):
    """Makes a round kirigami pattern at coordinates 0,0 with the specified radius
    the get methods should return svg strings"""

    def __init__(self, label, radius):
        self.radius = radius
        self.label = label

    def glass(self):
        """draws the glass cutout"""
        with tag(
            "circle",
            ("cx", 0),
            ("cy", 0),
            ("r", self.rg),
            ("fill", "transparent"),
            ("stroke", "red"),
        ):
            pass

    def toFirefox(self):
        with tag(
            "svg",
            ("width", 1200),
            ("height", 1200),
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


def main():
    pass


if __name__ == "__main__":
    main()
