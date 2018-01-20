# Calculation Examples

The capital gains example is included with the `./gains/exampleTrades.csv` file,
and the income example is included with the `./income/exampleIncome.csv` file.
Multiple CSV files can be given in the `./gains/` and `./income/` directories.
Prices are found within `./prices` for the example `foo` and `bar` assets.

The income for the 2009 to 2010 (Apr 6 to Apr 5) tax year should equate to a
profit of 55. The 2010 to 2011 tax year should equate to a loss of 22.5.

## Capital Gains Calculation Walkthrough

On the 1st of January 2010, a total of 800 foo coins are purchased for a total
of £1,600 with the following transactions:

1. 200 for £550
2. 400 for £750
3. 200 at a market price of £1.5

The transactions are considered as one, ie. 800 coins for £1,600 @ £2.

On the same day, a disposal is made of 300 coins for £700. This presents a gain
of £100.  The remaining 500 coins for £1,000 are added to a section 104 holding.

On the 1st of February 150 coins are purchased for £450 at £3.  On the 1st of
February 50 coins are disposed for £200 at £4.  On the 2nd of January 300 coins
are disposed for £450 at £1.5

Firstly the disposal on the 1st of Feb is matched against the acquisition. A
gain of £50 is made on 50 coins, leaving 100 coins purchased at £3. Next the
disposal on the 2nd of Jan is matched to the acquisition on the 1st of Feb due
to it being within 30 days afterwards. This matches 100 coins at a cost of £3,
sold at £1.5, leaving a loss of £150, and 200 coins remaining. These 200 coins
are matched against the section 104 holding at a cost of £2, leaving a loss of
£100. The holding is reduced to 300 coins for £600.

On the 2nd of February a total of 300 coins are purchased for £1200 at £4.

The section 104 holding is increased to 600 coins for £1,800. This is outside
the 30 day period of the disposal made in January, so it does not get matched.

On the 1st of April 300 coins are disposed for £1,200 at £4.  On the 1st of
April 100 coins are purchased for £300 at £3.  On the 1st of May 600 coins are
purchased for £3,000 at £5.  On the 1st of May 200 coins are disposed for £1,200
at £6.

Firstly 100 coins disposed in April are matched against the coins purchased on
the same day, at a £100 gain. The 200 coins disposed in May are matched against
the same-day purchase for a £200 gain. The remaining 200 coins disposed in April
are matched against the remaining 400 purchased in May, leaving a loss of £200.
Of the coins purchased in May, 200 are added to the holding with £1,000. The new
holding equals 800 coins and £2,800.

On the 1st of July 250 coins are disposed for £2,500 at £10.  On the 1st of July
50 coins are purchased for £600 at £12.  On the 2nd of July 200 coins are
purchased for £800 at £4.  On the 2nd of July 100 coins are disposed for £1,100
at £11.  On the 3rd of July 300 coins are purchased for £1,800 at £6.

The disposal is matched against all three acquisitions but the same-day disposal
on the 2nd must be matched first, and the most recent purchases are matched
first.

1. The disposal on the 2nd is matched to 100 coins on the same day, leaving a
   gain of £700 and 100 purchased coins remaining on the 2nd.
2. The 50 coins purchased on the 1st is matched to the coins disposed on that
   day, leaving a £100 loss, and a £200 disposal remaining.
3. The remaining 100 coins from the 2nd are matched to the remaining 200 on the
   1st for a £600 gain, leaving 100 coins from the 1st.
4. The remaining 100 coins is matched to the 300 coins on the 3rd for a gain of
   £400.
5. This leaves 200 remaining on the 3rd, increasing the holding to 1,000 coins
   and £4,000.

On the 1st of September 100 coins are disposed for £1,000 at £10 On the 2nd of
September 300 coins are disposed for £1,800 at £6 On the 3rd of September 50
coins are purchased for £200 at £4 On the 4th of September 150 coins are
purchased for £300 at £2

The acquisitions are matched against the earlier disposal on the 1st. 50 from
the 3rd are matched at £4 for a £300 gain. 50 from the 4th are matched for a
gain of £400. Then the remaining 100 from the 4th is matched to the disposal on
the 2nd, for a gain of £400. The remaining 200 on the 2nd are matched against
the holding at a cost of £4, leaving a gain of £400. The holding is reduced to
800 coins and £3,200.

300 coins are sold on the 5th of September for £1,000, making a loss of £200.
This is done in three transactions:

1. 100 coins for £300
2. 150 coins for £500
3. 50 coins at a market price of £4

The final holding is at 500 coins and £2,000.

The total gain throughout 2010 is £2,900. However, in the UK the tax year starts
on the 6th of April. The 09/10 tax year would have a loss of £200 and the 10/11
tax year would have a gain of £3,100.
