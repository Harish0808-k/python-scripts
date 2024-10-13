"""
This script generates fake data for promotions and saves it into CSV files.

Promotions Data (CSV):
----------------------
Columns:
========
1. promotion_id: Unique identifier for each promotion.
2. product_id: Identifier for the product that is being promoted.
3. promotion_type: Type of promotion (e.g., "discount", "buy one, get one free").
4. start_date: Start date of the promotion (YYYY-MM-DD).
5. end_date: End date of the promotion (YYYY-MM-DD).
6. discount_amount: Discount percentage or flat amount applied during the promotion.
"""
import csv
from faker import Faker

faker = Faker()


async def generate_promotions_data(no_of_rows):
    promotion_id_prefix = "pm-diwali"
    promotions_data = []

    for row_number in range(no_of_rows):
        row = [
            promotion_id_prefix+str(row_number),

        ]
