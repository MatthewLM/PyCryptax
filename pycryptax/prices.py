import os, re
from decimal import Decimal
from pycryptax import csvdata

FILENAME_PATTERN = r"^(.+)_(.+)\.csv$"

class AssetPricesNotFound(Exception):
    def __init__(self, asset):
        self.asset = asset

class PriceNotFoundForDate(Exception):
    def __init__(self, asset, date):
        self.asset = asset
        self.date = date

class Prices():

    def __init__(self, reportAsset, dirpath):

        self._d = {}
        self._reportAsset = reportAsset

        for f in os.listdir(dirpath):

            match = re.match(FILENAME_PATTERN, f)

            if match:
                base, quoted = match.groups()
                self._d[base.lower()] = csvdata.CSVPrices(
                    dirpath + "/" + f, quoted.lower()
                )

    def get(self, asset, date):

        if asset == self._reportAsset:
            return Decimal(1)

        try:
            assetPrices = self._d[asset]
        except KeyError:
            raise AssetPricesNotFound(asset)

        try:
            return assetPrices[date] * self.get(assetPrices.quotedAsset(), date)
        except KeyError:
            raise PriceNotFoundForDate(asset, date)

    def reportAsset(self):
        return self._reportAsset

