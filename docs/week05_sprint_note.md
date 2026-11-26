# Week 5 Sprint Note

**Project:** Heavy Supplier, Inventory & Warehouse Analytics
**Participant:** Maryam Shaikh (solo)

## Sprint goal
Check the reliability and health of inventory by product and branch.

## Completed
- Compared current stock with the stock ledger (`week05/inventory_health.py`)
- Checked ledger consistency and adjustment direction
- Assigned a stock status to all 180 records
- Calculated 2024 unit turnover, days of stock and stock value
- Wrote the inventory health summary

## Issues
- All records are above maximum stock
- 14 records do not match the ledger
- Turnover and days of stock are unrealistic, so they are reported as a data limitation

## Next steps (Week 6)
- Analyse warehouse capacity and throughput by branch
- Convert warehouse capacity from text to a number
- Compare branch performance
