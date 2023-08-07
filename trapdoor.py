#! python

from yattag import indent
from base import doc, tag, text, Pattern


class TrapdoorPattern(Pattern):
    """Makes a round kirigami pattern at coordinates 0,0 with the specified radius
    the get methods should return svg strings"""

    def __init__(
        self,
        label,
        leftObject,
        rightObject,
        border,
    ):
        self.label = label

    def glass(self):
        """draws the glass cutout"""
        pass


def main():
    pass


if __name__ == "__main__":
    main()
