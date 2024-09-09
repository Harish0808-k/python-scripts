from utilities import (
    generate_product_data,
    generate_refunds_data,
    generate_sales_data,
    generate_stores_data,
    generate_supervisors_data,
    write_csv,
)


def main():
    num_records = 20000

    # Generate and write data for stores
    stores_data = generate_stores_data(num_records)
    write_csv(
        "stores.csv",
        [
            "id",
            "name",
            "region",
            "address",
            "city",
            "state",
            "created_at",
            "updated_at",
        ],
        stores_data,
    )

    # Generate and write data for products
    products_data = generate_product_data(num_records)
    write_csv(
        "products.csv",
        [
            "id",
            "name",
            "category",
            "brand",
            "stock",
            "price",
            "created_at",
            "updated_at",
        ],
        products_data,
    )

    # Generate and write data for sales
    store_ids = [store_record[0] for store_record in stores_data]
    product_ids = [product_record[0] for product_record in products_data]
    sales_data = generate_sales_data(num_records, store_ids, product_ids)
    write_csv(
        "sales.csv",
        [
            "transaction_id",
            "store_id",
            "product_id",
            "quantity",
            "sale_price",
            "total_amount",
            "sale_date",
            "supervisor_id",
            "created_at",
            "updated_at",
        ],
        sales_data,
    )

    # Generate and write data for refunds
    refunds_data = generate_refunds_data(num_records, store_ids, product_ids)
    write_csv(
        "refunds.csv",
        [
            "transaction_id",
            "store_id",
            "product_id",
            "quantity_refunded",
            "refund_amount",
            "refund_date",
            "supervisor_id",
            "created_at",
            "updated_at",
        ],
        refunds_data,
    )

    supervisors_data = generate_supervisors_data()
    write_csv(
        "supervisors.csv",
        [
            "id",
            "name",
        ],
        supervisors_data,
    )


if __name__ == "__main__":
    main()
