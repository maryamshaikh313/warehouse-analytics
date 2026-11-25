# Week 1: Data Quality Report

## 1. Overview
12 CSV tables were profiled. No fully duplicated rows were found.

## 2. Findings

| Issue | Result | Action |
|---|---|---|
| Missing `received_date` in purchase_orders_header | 2,370 of 24,000 rows, all Cancelled orders | Kept as blank (expected) |
| Date columns stored as text | All converted, 0 failures | Converted to date type |
| Duplicate `invoice_id` | 197 repeats, 393 rows affected (about 2.2%) | Added `invoice_key` and `ambiguous_id` flag |
| Duplicate `payment_id` | 202 repeats | Added `payment_key`; no rows deleted |
| Payments linked to a duplicated `invoice_id` | 417 of 19,257 rows (about 2.2%) | Flagged as `ambiguous_invoice` |
| `current_stock` above `max_stock` | All 180 inventory rows | Not changed; reported as a limitation |
| Duplicate `so_id`, `po_id`, `movement_id` | None found | No action |

## 3. How flagged rows are handled
No records were deleted. When joining invoices with payments, rows with an ambiguous invoice ID are excluded, because a payment cannot be matched to one invoice with certainty:

```python
safe_pay = pay[pay["ambiguous_invoice"] == False]
safe_inv = inv[inv["ambiguous_id"] == False]
```

## 4. Limitations
- Total IN quantity in the stock ledger (20,397,795) is about 18 times total OUT quantity (1,124,832). This likely explains the high stock levels, so overstock and turnover results should be read with caution.
- The only product-branch checked in detail (P001, DEL001) had a final ledger balance matching `current_stock` (115,928). Other combinations were not checked.
- Field documentation was not used, so column meanings are assumed from names and data.
