# Copyright 2019 Matthew Mitchell

import argparse, sys
from contextlib import contextmanager
from pycryptax import csvdata, prices, income, gains, util

GAINS_DIR = "/gains"
INCOME_DIR = "/income"
PRICES_DIR = "/prices"
ERR_NOTICE = """

Please read the README.md and see the ./examples directory for an example \
working directory
"""

BEFORE_MSG = """
Do not rely on this software for accuracy. Anything provided by this software
does not constitute advice in any form. The software is provided "as is",
without warranty of any kind. Please see the LICENSE and README.md files."""

AFTER_MSG = """\
Thank you for using PyCryptax. If you found this program useful, please consider
giving a small donation to one of the following crypto addresses:

  Bitcoin : 1Fj5hKbEfb2ndBgBsyErT5WJv7jyaSSZKW
 Ethereum : 0xdE77869FF85084e0020061ac9bf858f1722e8448
 Litecoin : MRuio1MGdDPmh5Wxk5nApDyraP9qKSdy6D
 Peercoin : PPJLqRggLFEPkSTt1AhytJWUxsBSLNA7E9
   Monero : 848JNJDYRF9ZBXb3FAKkcMWYXbppcv8MaM3YYw4cCt1E7RKwCtUUaCbjUDjgkuxZYgFu5qCNfW5KJddrFz1hpCZR8cS2jCD
"""

def fail(message):
    print("\n" + message + ERR_NOTICE, file=sys.stderr)
    sys.exit(1)

@contextmanager
def csvErrorHandler(what, directory, reportAsset):

    try:
        yield
    except FileNotFoundError:
        fail(
            "You need to provide {} in the {} directory".format(what, directory)
        )
    except csvdata.CSVNotOpenable as e:
        fail("Cannot open CSV file {}".format(str(e)))
    except csvdata.CSVKeyError as e:
        fail("Missing column(s) for {}".format(e.filename))
    except csvdata.CSVDateError as e:
        fail(
"Incorrect date \"{}\" in {} on line {}. An example date is 2020-01-05"
            .format(e.date, e.filename, e.line)
        )
    except csvdata.CSVNumberError as e:
        fail(
"A non numeric value found in {} on line {} where a number is expected"
            .format(e.filename, e.line)
        )
    except prices.AssetPricesNotFound as e:
        fail("""\
Cannot find a {1} price for {0}. Please provide a {0}_{1}.csv file in the \
prices directory""".format(e.asset, reportAsset))
    except prices.PriceNotFoundForDate as e:
        fail(
            "Cannot find a {} price for {}"
            .format(e.asset, util.getPrettyDate(e.date))
        )

def main():

    # Arguments

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""\
Calculate UK Income and Capital Gain for Tax. Uses Section 104 holding rules and
30-day bed and breakfasting rules. Automatically converts asset amounts into a
specified reporting asset given price data.\
        """,
        epilog="""\
Use the 'income' command to produce a summary of revenue and
expenses.

Use the 'txs' command to output income calculations for each
transaction to CSV, containing the original asset amount, the price
and the reporting asset amount.

Use the 'gain' command to produce a summary of asset gains and
losses, and a summary of current section 104 holdings.

Use the 'disposals' command to output a list of asset disposal
information to CSV.
        """
    )

    parser.add_argument(
        "action", choices=["income", "txs", "gain", "disposals"]
    )
    parser.add_argument("start", type=str, help="Starting date of calculation")
    parser.add_argument("end", type=str, help="End date of calculation")
    parser.add_argument(
        "--reportingcurrency", "-c", type=str, default="gbp",
        help="The reporting currency (default \"gbp\") to present calculations"
    )
    parser.add_argument(
        "--dir", "-d", type=str, default="./",
        help="The root directory of the CSV data (default \"./\")"
    )

    args = parser.parse_args()

    reportAsset = args.reportingcurrency
    action = args.action
    rootDir = args.dir
    start = util.dateFromString(args.start)
    end = util.dateFromString(args.end)

    # Load price data
    with csvErrorHandler("prices", rootDir + PRICES_DIR, reportAsset):
        priceData = prices.Prices(reportAsset, rootDir + PRICES_DIR)

    def getCGCalc(**kwargs):
        with csvErrorHandler(
            "capital gains information", rootDir + GAINS_DIR, reportAsset
        ):
            return gains.CapitalGainCalculator(
                csvdata.CSVGains(rootDir + GAINS_DIR), priceData, start, end,
                **kwargs
            )

    def getIncomeCalc():
        with csvErrorHandler("income information", rootDir + INCOME_DIR, reportAsset):
            return income.IncomeCalculator(
                csvdata.CSVIncome(rootDir + INCOME_DIR), priceData, start, end
            )

    if action == "income":
        print(BEFORE_MSG)
        getIncomeCalc().printSummary()
        print(AFTER_MSG)
    elif action == "txs":
        getIncomeCalc().printTxs()
    elif action == "gain":
        print(BEFORE_MSG)
        getCGCalc(summary=True).printSummary()
        print(AFTER_MSG)
    elif action == "disposals":
        getCGCalc(disposals=True).printDisposals()

if __name__ == '__main__':
    main()

