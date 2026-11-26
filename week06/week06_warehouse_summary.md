# Week 6: Warehouse Operations Summary

Compares the 6 branches. Throughput is incoming plus outgoing units from the stock ledger (adjustments excluded).

## Branch performance (2024)
| Branch | Capacity (sqft) | Units per sqft | Throughput | Out to in % | Employees | Throughput per employee | Movements per employee |
|---|---|---|---|---|---|---|---|
| CHN001 | 41,890 | 77.21 | 620,557 | 6.42 | 81 | 7,661 | 90.00 |
| DEL001 | 45,230 | 72.71 | 600,659 | 5.13 | 92 | 6,529 | 69.27 |
| AHM001 | 34,120 | 92.47 | 587,218 | 5.14 | 63 | 9,321 | 100.63 |
| PUN001 | 38,750 | 84.03 | 579,240 | 5.19 | 74 | 7,828 | 85.23 |
| HYD001 | 36,210 | 89.62 | 562,005 | 4.69 | 57 | 9,860 | 102.25 |
| KOL001 | 29,880 | 104.55 | 542,950 | 6.59 | 49 | 11,081 | 132.80 |

Movement counts include all ledger entries, including adjustments.

## Revenue check (delivered orders, 2019 to 2024, monthly average)
| Branch | Branch table revenue | Revenue from orders | Times higher |
|---|---|---|---|
| DEL001 | 5,234,890 | 48,611,546 | 9.3 |
| PUN001 | 4,389,120 | 46,854,584 | 10.7 |
| CHN001 | 4,567,780 | 65,030,584 | 14.2 |
| HYD001 | 3,102,455 | 42,736,781 | 13.8 |
| KOL001 | 2,894,770 | 60,275,852 | 20.8 |
| AHM001 | 3,245,890 | 55,365,480 | 17.1 |

## Findings
- CHN001 handled the most units in 2024 and KOL001 the fewest.
- KOL001, the smallest warehouse, has the most units per sqft, throughput per employee and movements per employee.
- DEL001, the largest warehouse with the most employees, has the lowest throughput and movements per employee.
- In every branch and every full year from 2019 to 2024, incoming units were about 13 to 24 times outgoing units.
- Cost-to-revenue ratios from the branch table are 59.96% to 62.17%, but that revenue does not agree with order data.

## Limitations
- Units per sqft ignores product size and stacking, so it is not true space utilisation.
- Stock quantities are unverified (see Week 5).
- The data does not show employee duties, so per-employee measures do not prove productivity differences.
- 2025 is incomplete and excluded from comparisons.

## Recommendations
- Review staffing and duties at DEL001.
- Verify ledger data, then plan purchasing against demand.
- Verify and correct branch revenue data.
