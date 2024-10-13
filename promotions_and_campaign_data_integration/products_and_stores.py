from faker import Faker
import csv

faker = Faker()


def get_products():
    products = []
    for i in range(50):
        products.append(
            {
                "product_id": "pro-"+str(i),
                "product_name": faker.company()
            }
        )
    return products


def get_stores():
    stores = []
    for i in range(10):
        stores.append(
            {
                "store_id": "st-"+str(i),
                "store_name": faker.city()
            }
        )
    return stores


if __name__ == "__main__":
    path = "./promotions_and_campaign_data_integration/csv_files"

    with open(path+"/products_data.csv", 'w', newline='') as products_data:
        writer = csv.DictWriter(products_data,
                                fieldnames=[
                                    'product_id', 'product_name'
                                ]
                                )
        writer.writeheader()
        writer.writerows(get_products())

    with open(path+"/stores_data.csv", 'w', newline='') as stores_data:
        writer = csv.DictWriter(stores_data,
                                fieldnames=[
                                    "store_id", "store_name"
                                ]
                                )
        writer.writeheader()
        writer.writerows(get_stores())
