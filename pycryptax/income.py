from decimal import Decimal
from pycryptax import util, output

class IncomeValue():

    def __init__(self, value=Decimal(0)):
        if value > 0:
            self._in = value
            self._out = Decimal(0)
        else:
            self._out = -value
            self._in = Decimal(0)

    def __iadd__(self, amount):
        self._in += amount._in
        self._out += amount._out
        return self

    def revenue(self):
        return self._in

    def expenditure(self):
        return self._out

    def total(self):
        return self._in - self._out

class IncomeTx():

    def __init__(self, asset, date, amount, price, incomeValue, note):
        self.asset = asset
        self.date = date
        self.amount = amount
        self.price = price
        self.incomeValue = incomeValue
        self.note = note

class IncomeCalculator():

    def __init__(self, incomeData, priceData, start, end):

        self._start = start
        self._end = end

        self._assetIncome = {}
        self._txs = []
        self._total = IncomeValue()

        for date, tx in incomeData.range(start, end):
            price = priceData.get(tx.asset, date)
            incomeValue = IncomeValue(tx.amount * price)
            self._txs.append(
                IncomeTx(
                    tx.asset, date, tx.amount, price, incomeValue, tx.note
                )
            )
            self._total += incomeValue
            util.addToDictKey(self._assetIncome, tx.asset, incomeValue)

    def printSummary(self):

        output.printCalculationTitle("INCOME", self._start, self._end)

        table = output.OutputTable(4)
        table.appendRow("ASSET", "REVENUE", "EXPENDITURE", "TOTAL")
        table.appendGap()

        for k, v in self._assetIncome.items():
            table.appendRow(k, v.revenue(), v.expenditure(), v.total())

        table.appendGap()
        table.appendRow(
            "TOTAL", self._total.revenue(), self._total.expenditure(), self._total.total()
        )

        table.print()

    def printTxs(self):

        print("Date,Asset,Amount,Price,Revenue,Expense,Note")

        def numFormat(n):
            return "{:.2f}".format(n) if n != 0 else ""

        for tx in self._txs:
            print("{},\"{}\",{},{},{},{},\"{}\"".format(
                util.getPrettyDate(tx.date),
                tx.asset.replace('"', '""'),
                numFormat(tx.amount),
                numFormat(tx.price),
                numFormat(tx.incomeValue.revenue()),
                numFormat(tx.incomeValue.expenditure()),
                tx.note.replace('"', '""')
            ))

