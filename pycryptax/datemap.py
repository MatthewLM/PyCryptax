import bisect, datetime

class DateMapIterator():

    def __init__(self, dateMap, start=None, end=None):

        self._dateMap = dateMap

        self._pos = 0 if start is None else bisect.bisect_left(dateMap._dates, start)

        self._end = len(dateMap) if end is None else \
                bisect.bisect_right(dateMap._dates, end)

    def __next__(self):

        if self._pos == self._end:
            raise StopIteration

        self._pos += 1

        return self._dateMap[self._pos - 1]

class DateMapIterable():

    def __init__(self, dateMap, start, end):
        self._dateMap = dateMap
        self._start = start
        self._end = end

    def __iter__(self):
        return DateMapIterator(self._dateMap, self._start, self._end)

class DateMap():

    def __init__(self):

        self._dates = []
        self._values = []

    def range(self, start, end):
        return DateMapIterable(self, start, end)

    def _indexOf(self, date):
        return bisect.bisect_left(self._dates, date)

    def _indexHasDate(self, ind, date):
        return ind != len(self) and self._dates[ind] == date

    def __contains__(self, date):
        return self._indexHasDate(self._indexOf(date), date)

    def __getitem__(self, ind):

        if type(ind) is datetime.datetime:

            intInd = self._indexOf(ind)

            if not self._indexHasDate(intInd, ind):
                raise IndexError

            return self._values[intInd]

        return self._dates[ind], self._values[ind]

    def __len__(self):
        return len(self._dates)

    def __iter__(self):
        return DateMapIterator(self)

    def insert(self, date, value):

        ind = bisect.bisect(self._dates, date)
        self._dates.insert(ind, date)
        self._values.insert(ind, value)

        return value

