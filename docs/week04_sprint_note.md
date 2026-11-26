# Week 4 Sprint Note

**Project:** Heavy Supplier, Inventory & Warehouse Analytics
**Participant:** Maryam Shaikh (solo)

## Sprint goal
Find which products drive sales and how they compare by value and units sold.

## Completed
- Joined product and sales order data (`week04/product_performance.py`)
- Created new columns: units_sold, sales, orders, sales_share_pct, abc_class and movement
- Classified 30 products using ABC analysis
- Grouped products as Fast, Medium or Slow by units sold
- Wrote the product performance summary

## Issues
- Units sold are very similar across products, so the movement labels have limited meaning
- Current stock above maximum stock (found earlier) will affect inventory analysis

## Next steps (Week 5)
- Analyse inventory turnover and stock health by product and branch
- Check stock levels against reorder level, safety stock and maximum stock
- Check stock ledger movements, including adjustments
