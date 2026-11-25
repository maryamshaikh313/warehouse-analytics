# Week 1 Sprint Note

**Project:** Heavy Supplier, Inventory & Warehouse Analytics
**Participant:** Maryam Shaikh (solo)

## Sprint goal
Understand the dataset, check and clean it, document it, and calculate the first KPIs.

## Completed
- Profiled all 12 tables (`data_profiling.py`)
- Checked missing values, stock levels and IDs (`data_checks.py`, `id_checks.py`)
- Converted date columns, added unique keys and ambiguity flags (`week1_cleaning.py`)
- Created the data dictionary for 138 columns, with assumed descriptions (`data_dictionary_final.csv`)
- Wrote the data quality report
- Calculated first KPIs (`kpis.py`)

## Blockers and issues
- Fields documentation was not in the dataset download, so column meanings are assumed
- Duplicate invoice and payment IDs
- Current stock is above maximum stock in all 180 inventory rows

## Next steps (Week 2)
- Verify the assumed column descriptions and customer summary columns
- Check product-wise and branch-wise performance
- Investigate cancellations and late deliveries
- Check that sales order line totals match header totals
- Start a Power BI dashboard
