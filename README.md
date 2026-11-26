# Heavy Supplier, Inventory & Warehouse Analytics

A 12-week analytics project (CadetX virtual work experience) on supplier, product, inventory, warehouse and customer data.

**Participant:** Maryam Shaikh (solo)

## Goal
Use historical data to understand product movement, check inventory health, review warehouse and supplier performance, and support better decisions.

## Dataset
12 CSV files from the CadetX portal: branches, customers, inventory_master, invoices, payments, products, purchase_orders_header, purchase_orders_lines, sales_orders_header, sales_orders_lines, stock_ledger and suppliers.

The data files are not included in this repository.

## Folder structure
| Folder | Contents |
|---|---|
| `week01/` | Data profiling script and profiling summary |
| `week02/` | Data checks, ID validation, cleaning and data quality report |
| `week03/` | Data dictionary, first KPIs and KPI summary |
| `week04/` | Product performance, ABC classification and product summary |
| `week05/` | Inventory health, turnover, stock value and summary |
| `docs/` | Sprint notes |

## How to run
1. Install Python and pandas (`pip install pandas`).
2. Place the 12 CSV files in a `data/` folder at the project root.
3. Run each script from inside its own folder, in this order:
   1. `week01/data_profiling.py`
   2. `week02/data_checks.py`
   3. `week02/id_checks.py`
   4. `week02/week1_cleaning.py` (creates `data_clean/`)
   5. `week03/data_dictionary.py` (creates `docs/data_dictionary.csv`; descriptions were added separately in `week03/data_dictionary_final.csv`)
   6. `week03/kpis.py`
   7. `week04/product_performance.py` (creates `week04/product_performance.csv`)
   8. `week05/inventory_health.py` (creates `week05/inventory_health.csv`)

## Phase 1 results (Weeks 1–3)
| KPI | Result |
|---|---|
| Total sales (delivered, excluding GST, 2019 to 2024) | 22,958,987,430 |
| Average order value | 1,273,165.17 |
| Sales orders delivered | 90.16% |
| Purchase order cancellation rate | 9.88% |
| On-time delivery rate | 84.90% |

## Week 4 results
- 10 of 30 products (class A) generate 81.53% of sales
- Engine Block EB-600 and Transmission Assembly TA-800 generate about 36% of sales
- Units sold are similar across products, so movement labels are relative

## Week 5 results
- Current stock matches the stock ledger in 166 of 180 records
- All 180 records are above maximum stock
- Mean 2024 unit turnover is 0.0104, so stock figures are treated as a data limitation

## Data issues found
- 2,370 blank received dates, all on cancelled purchase orders
- Duplicate invoice and payment IDs (kept, with unique keys; affected invoice links flagged)
- Current stock above maximum stock in all 180 inventory rows
- Column descriptions are assumed because fields documentation was not in the download

## Documents
- [Phase 1 sprint note (Weeks 1–3)](docs/week01_sprint_note.md)
- [Week 4 sprint note](docs/week04_sprint_note.md)
- [Week 5 sprint note](docs/week05_sprint_note.md)
- [Data quality report](week02/week01_data_quality_report.md)
- [KPI summary](week03/week01_kpi_summary.md)
- [Data dictionary](week03/data_dictionary_final.csv)
- [Product performance summary](week04/week04_product_summary.md)
- [Inventory health summary](week05/week05_inventory_summary.md)
