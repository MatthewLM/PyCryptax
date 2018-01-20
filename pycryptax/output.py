import string, decimal
from pycryptax import util

class OutputTable():

    def __init__(self, cols):
        self._data = []
        self._cols = cols
        self._colWidths = (0,) * cols

    def appendRow(self, *row):

        # Convert to strings

        row = tuple(
            "{:,.2f}".format(cell) if type(cell) is decimal.Decimal \
            else str(cell) \
            for cell in row
        )

        # Pad with extra cells

        self._data.append(
            row + ("",) * (self._cols - len(row))
        )

        # Calculate new width from maximum width of cell strings

        self._colWidths = tuple(
            max(last, new+2) for last, new in zip(
                self._colWidths,
                (len(cell) for cell in row)
            )
        )

    def appendGap(self):
        self._data.append(("",) * self._cols)

    def print(self):

        for row in self._data:
            for cell, width in zip(row, self._colWidths):
                padding = width-len(cell)
                print(cell, end = " " * padding)
            print()

        print()


def printCalculationTitle(title, start, end):
    print("\n{} CALCULATION {} - {}:\n".format(
        title, util.getPrettyDate(start), util.getPrettyDate(end)
    ))

