# Smart Store Seabaugh

## Smart Sales Starter Files
Starter files to initialize the Smart Sales project.

---

## Project Setup Guide

### Setup for All Platforms
Run all commands from a terminal in the root project folder.

#### Step 1A - Create a Local Project Virtual Environment
    python3 -m venv .venv

#### Step 1B - Activate the Virtual Environment

- Mac/Linux:
    source .venv/bin/activate

- Windows:
    .venv\Scripts\activate

#### Step 1C - Install Required Packages
    python3 -m pip install --upgrade -r requirements.txt

#### Step 1D - Optional: Verify Virtual Environment Setup
    python3 -m datafun_venv_checker.venv_checker

#### Step 1E - Run the Initial Project Script
    python3 scripts/data_prep.py

---

## Database Schema & Design Choices

This project uses a **star schema** for organizing the SQLite sales data warehouse. The **fact table** (`sale`) records transactions, and the **dimension tables** (`customer`, `product`) provide lookup and filtering capabilities.

### Schema Overview

#### 🧾 customer Table

| Column             | Type     | Description                                 |
|--------------------|----------|---------------------------------------------|
| customer_id        | INTEGER  | Primary key                                 |
| name               | TEXT     | Full name of the customer                   |
| region             | TEXT     | Geographic region                           |
| join_date          | TEXT     | Date the customer joined                    |
| loyalty_points     | REAL     | Loyalty point balance                       |
| preferred_contact  | TEXT     | Preferred contact method                    |

#### 📦 product Table

| Column             | Type     | Description                                 |
|--------------------|----------|---------------------------------------------|
| product_id         | INTEGER  | Primary key                                 |
| product_name       | TEXT     | Name of the product                         |
| category           | TEXT     | Product category                            |
| unit_price         | REAL     | Price per unit                              |
| stock_quantity     | INTEGER  | Available stock                             |
| supplier           | TEXT     | Supplier name                               |

#### 💰 sale Table *(Fact Table)*

| Column             | Type     | Description                                 |
|--------------------|----------|---------------------------------------------|
| sale_id            | INTEGER  | Primary key                                 |
| customer_id        | INTEGER  | Foreign key → customer.customer_id          |
| product_id         | INTEGER  | Foreign key → product.product_id            |
| store_id           | INTEGER  | Store where the sale occurred               |
| campaign_id        | INTEGER  | Marketing campaign identifier               |
| sale_amount        | REAL     | Total sale amount                           |
| sale_date          | TEXT     | Date of the sale                            |
| discount_percent   | REAL     | Discount applied                            |
| payment_type       | TEXT     | Method of payment                           |

---
## Visualizations and SQL Queries
### 💡 Key Queries:
- **Top Customers:**
  ```sql
  SELECT c.name, SUM(s.amount) AS total_spent
  FROM sale s
  JOIN customer c ON s.customer_id = c.customer_id
  GROUP BY c.name
  ORDER BY total_spent DESC

### Visuals
![Dashboard](C:\Users\clayt\Documents\smart-store-seabaugh\images\dashboard.png)
![Schema](C:\Users\clayt\Documents\smart-store-seabaugh\images\schema.png)
![Chart from Query](C:\Users\clayt\Documents\smart-store-seabaugh\images\querychart.png)
![Query](C:\Users\clayt\Documents\smart-store-seabaugh\images\query.png)




## Git Workflow

After making changes, use the following commands to commit and push updates to GitHub:

    # git add .
    # git commit -m "Update README with schema"
    # git push

Modify the commit message to describe your changes appropriately.

---

## Markdown Preview

To preview this `README.md` file in VS Code:
- Open the file.
- Press `Ctrl + Shift + V` (Windows/Linux) or `Cmd + Shift + V` (Mac).
- Or click the "Open Preview" button in the top-right corner.

---

## Need Help?

For issues or troubleshooting, reach out via discussion forums or the project repository.

Happy coding! 🚀
