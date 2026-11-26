# Week 5: Inventory Health Summary

Covers 180 product-branch records (30 products, 6 branches). Turnover and days of stock use units and 2024 outgoing movements. The currency is not stated in the data.

## Record checks
| Check | Result |
|---|---|
| Current stock matches final ledger balance | 166 of 180 |
| Records that do not match | 14 (13 lower, 1 higher; largest difference 515 units) |
| Ledger balance changes equal to movement quantity | 100% |
| Adjustments that added stock | 1,219 |
| Adjustments that removed stock | 1,222 |

## Stock health (2024)
| Measure | Result |
|---|---|
| Records above maximum stock (Overstock) | 180 of 180 |
| Unit turnover (2024 OUT units / average ledger balance), mean | 0.0104 |
| Days of stock (current stock / average daily OUT), mean | 39,877 (about 109 years) |
| Stock value at unit cost | 281,292,677,410 |

## Stock value by branch
| Branch | Stock value |
|---|---|
| CHN001 | 47,798,163,500 |
| PUN001 | 47,728,085,910 |
| DEL001 | 47,709,094,440 |
| HYD001 | 47,224,691,630 |
| AHM001 | 46,129,795,000 |
| KOL001 | 44,702,846,930 |

## Top 5 products by stock value
| Product | Stock value |
|---|---|
| Engine Block EB-600 | 60,411,676,500 |
| Transmission Assembly TA-800 | 45,323,915,500 |
| Boom Cylinder BC-400 | 22,449,965,200 |
| Track Chain TC-45 | 20,763,665,000 |
| Swing Motor SWM-350 | 19,414,168,800 |

## Findings
- The ledger is internally consistent, but current stock differs from the final ledger balance in 14 records. The cause is unknown.
- Stock levels are unrealistically high compared with sales. Turnover, days of stock and stock value should not be used for decisions until the data is verified.
- Engine Block EB-600 holds about 21% of the recorded stock value.

## Limitations
- Average stock is the mean of ledger balances at movement records, not a time-weighted average.
- Stock value uses the unit cost in the products table.

## Recommendations
- Verify stock quantities with the data provider or a physical count.
- Investigate the 14 mismatched records.
