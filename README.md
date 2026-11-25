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
| `week01/` | Python scripts and profiling summary |
| `docs/` | Data dictionary, quality report, KPI summary, sprint note |

## How to run
1. Install Python and pandas (`pip install pandas`).
2. Place the 12 CSV files in a `data/` folder at the project root.
3. From inside `week01/`, run in this order:
   1. `data_profiling.py`
   2. `data_checks.py`
   3. `id_checks.py`
   4. `week1_cleaning.py` (creates `data_clean/`)
   5. `data_dictionary.py` (creates `docs/data_dictionary.csv`; descriptions were added separately in `data_dictionary_final.csv`)
   6. `kpis.py`

## Week 1 results
| KPI | Result |
|---|---|
| Total sales (delivered, excluding GST, 2019 to 2024) | 22,958,987,430 |
| Average order value | 1,273,165.17 |
| Sales orders delivered | 90.16% |
| Purchase order cancellation rate | 9.88% |
| On-time delivery rate | 84.90% |

## Data issues found
- 2,370 blank received dates, all on cancelled purchase orders
- Duplicate invoice and payment IDs (kept, with unique keys; affected invoice links flagged)
- Current stock above maximum stock in all 180 inventory rows
- Column descriptions are assumed because fields documentation was not in the download

## Documents
- [Sprint note](docs/week01_sprint_note.md)
- [Data quality report](docs/week01_data_quality_report.md)
- [KPI summary](docs/week01_kpi_summary.md)
- [Data dictionary](docs/data_dictionary_final.csv)
