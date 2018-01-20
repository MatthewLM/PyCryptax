# PyCryptax

Pycryptax calculates income and capital gains using transactions and price
data from CSV files which can include cryptoassets such as Bitcoin. Capital
gains are calculated according to section 104 holding; 30-day bed and
breakfasting; and same-day rules. Guidance is available through an [HMRC
publication
online](https://www.gov.uk/government/publications/tax-on-cryptoassets/cryptoassets-for-individuals).

To install the program you must have Python 3. You can install using pip
(remember to use `sudo` if needed):

    pip3 install pycryptax

Alternatively you can run the following command in the project's root directory:

    python3 setup.py install

After installation, the `pycryptax` command should be available and you may run
`pycryptax --help` to view an overview of the usage. See below for more details
on how to use the software.

## Disclaimer

**Do not rely on this software for accuracy. Anything provided by this software
does not constitute advice in any form. The software is provided "as is",
without warranty of any kind. Use at your own risk. See the LICENSE file for
more details.**

## Providing Data

Transaction data for income and gains need to be provided in CSV files contained
within particular directories. Prices are kept in `./prices`, capital gain/loss
trades in `./gains` and income transactions in `./income`. These directories
should be found within the present working directory or the directory provided
by the `--dir` command line option.

CSV files can be produced by any decent spreadsheet software. Spreadsheet
software can be used to manipulate exported price, exchange and wallet data into
the correct format.

Empty rows are allowed. Additional columns for comments etc. are allowed and
ignored.

Please see the `./examples` directory which contains an example of how data
should be provided.

### Price data

Inside the `./prices` directory, CSV files containing price data for asset pairs
can be provided. This price data is used to convert asset amounts into the
reporting/account currency for which the tax calculation is being done (`gbp` by
default).

Each file should be formatted as `XXX_YYY.csv` where `XXX` is the base currency,
and `YYY` is the quote currency. For example `btc_gbp.csv` would contain the GBP
prices of 1 bitcoin.

These files can be chained together to combine conversions. For example
`btc_usd.csv` and `usd_gbp.csv` would allow conversion of bitcoin to GBP by
converting to USD first. The software only allows conversions to be done through
a single chain and they can only be done from the base currency to the quoted
currency so `gbp_btc.csv` would allow conversions of GBP to bitcoin but not
bitcoin to GBP.

Each file should contain a list of daily prices for the asset pair. If a price
is not available for a specifc date, then the soonest earlier date available is
used instead.

The price csv files should use the following columns:

| Column | Description                                                         |
| ------ | ------------------------------------------------------------------- |
| DATE   | The date of the price formatted as YYYY-MM-DD                       |
| PRICE  | A decimal number of the price of the base asset in the quoted asset |

### Income data

Transactions for all revenues (positive amounts) and expenses (negative amounts)
can be provided under the `./income` directory in as many CSV files as desired.
The CSV files can be named anything as long as they end in `.csv`. Transactional
data should be provided with the following columns:

| Column | Description                                                                  |
| ------ | ---------------------------------------------------------------------------- |
| DATE   | The date of the transaction formatted as YYYY-MM-DD                          |
| ASSET  | The asset transacted, in the same format provided by the prices CSV filename |
| AMOUNT | The amount of the asset received/debited (positive) or sent/credited (negative) |
| NOTE   | A note to be provided when outputing transactions                            |

### Capital Gain/Loss data

Trades between assets, and other acquisitions or disposals can be provided in
the `./gains` directory in as many CSV files as desired. The CSV files can be
named anything as long as they end in `.csv`.

If one asset is being traded for another, then they should be provided on the
same row. Sometimes assets are acquired or disposed without a counter asset. In
this case, only the single asset should be provided and the other cells should be
empty.

If you are selling or buying an asset against the reporting currency (GBP by
default), then the amount of the reporting currency should be provided as a
corresponding buy/sell asset like any other asset would. For example if you sold
2 bitcoin for £12,000, then put `btc` as the sell asset, `gbp` as the buy asset,
`2` as the sell amount and `12000` as the buy amount.

Asset names should be in the same format as in the price CSV filenames.

Trades should be provided with the following columns:

| Column      | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| DATE        | The date of the trade, acquistion and/or disposal formatted as YYYY-MM-DD |
| SELL ASSET  | The asset being sold/sent/disposed, or empty if none                      |
| BUY ASSET   | The asset being bought/received/acquired or empty if none                 |
| SELL AMOUNT | The amount of the SELL ASSET being disposed or empty if none              |
| BUY ASSET   | The amount of the BUY ASSET being acquired or empty if none               |

## Running Calculations

Please run `pycryptax -h` for usage details.

When running a calculation you must either be in the directory containing the
`prices`, `income` and/or `gains` directories, or provide it using the `--dir`
option.

Calcuations are done for a particular period of time. The start and end dates
need to be provided in the `YYYY-MM-DD` format. For example, to calculate income
for the 2009-2010 tax year in the `./examples` directory:

    pycryptax income 2009-04-06 2010-04-05 -d ./examples

The following actions are allowed:

- **income:** Produces the revenue and expenditure for each asset and in
  total.
- **gain:** Produces the gain and loss for each asset and in total. Also
  displays the status of the section 104 holding at the end of the
calculation period.
- **txs:** Outputs in CSV format each income tax transaction with revenue and
  expenditure calculations shown in the reporting asset (GBP by default).
- **disposals:** Outputs in CSV format each disposal, including the
  calculated costs and proceeds which HMRC may ask for.

If you do not want to report calculations in GBP or have named GBP something
other than `gbp`, then the `--reportingcurrency` option can be used to specify a
different asset.

