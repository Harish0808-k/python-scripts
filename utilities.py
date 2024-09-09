import random
import csv
from faker import Faker

faker = Faker()


def generate_stores_data(num_of_records):
    data = []
    for _ in range(1, num_of_records + 1):
        data.append(
            [
                faker.uuid4(),  # id (assuming auto-increment for simplicity)
                faker.company(),
                faker.city(),
                faker.street_address(),
                faker.city(),
                faker.state(),
                faker.date_time_this_decade(),  # created_at
                faker.date_time_this_decade(),  # updated_at
            ]
        )
    return data


def generate_product_data(num_of_records):
    product_category_dict = {
        "Mobile": [
            "Galaxy S23 Ultra",
            "iPhone 15 Pro",
            "Pixel 8 Pro",
            "OnePlus 11",
            "Xiaomi Mi 13",
            "Sony Xperia 1 IV",
            "Samsung Galaxy Z Fold 5",
            "iPhone 14",
            "Samsung Galaxy A54",
            "Nokia X30 5G",
            "Oppo Find X6",
            "Motorola Edge 40",
            "Realme GT 3",
            "Huawei P60 Pro",
            "Asus ROG Phone 7",
            "Google Pixel 7a",
            "Samsung Galaxy Note 20",
            "Xiaomi Redmi Note 12",
            "iPhone SE (2024)",
            "Samsung Galaxy A34",
        ],
        "Accessories": [
            "Beats Studio Buds",
            "Apple AirPods Pro",
            "Samsung Galaxy Buds 2",
            "Jabra Elite 85t",
            "Sony WH-1000XM4",
            "Logitech MX Master 3S",
            "Anker Wireless Charger",
            "Apple MagSafe Charger",
            "Bose QuietComfort Earbuds",
            "Belkin BoostCharge Pro",
            "Satechi USB-C Hub",
            "OtterBox Defender Case",
            "Spigen Tough Armor Case",
            "Razer BlackWidow V3",
            "Apple Pencil (2nd Gen)",
            "Logitech StreamCam",
            "JBL Flip 6",
            "Razer Naga X",
            "Anker PowerCore 10000",
            "HyperX Alloy FPS Pro",
        ],
        "Laptop": [
            "MacBook Pro 16-inch (2024)",
            "Dell XPS 15",
            "HP Spectre x360",
            "Lenovo ThinkPad X1 Carbon",
            "Microsoft Surface Laptop 5",
            "Asus ZenBook 14",
            "Acer Predator Helios 300",
            "Razer Blade 15",
            "Apple MacBook Air M2",
            "LG Gram 17",
            "MSI GS66 Stealth",
            "HP Envy 13",
            "Dell Inspiron 14",
            "Lenovo Yoga 9i",
            "Samsung Galaxy Book3",
            "Alienware x17",
            "Huawei MateBook X Pro",
            "ASUS ROG Flow Z13",
            "Acer Swift X",
            "Microsoft Surface Book 3",
        ],
        "Tablet": [
            "iPad Pro 12.9 (2024)",
            "Samsung Galaxy Tab S9 Ultra",
            "Microsoft Surface Pro 9",
            "Lenovo Tab P12 Pro",
            "Apple iPad Air 5",
            "Samsung Galaxy Tab A8",
            "Huawei MatePad Pro",
            "Amazon Fire HD 10",
            "Xiaomi Pad 6",
            "Microsoft Surface Go 3",
            "Lenovo Yoga Tab 13",
            "Apple iPad Mini 6",
            "Samsung Galaxy Tab S8+",
            "Sony Xperia Tablet Z4",
            "Huawei MediaPad T5",
            "Amazon Fire HD 8",
            "Samsung Galaxy Tab Active4 Pro",
            "Lenovo Tab M10 Plus",
            "Apple iPad Pro 11 (2024)",
            "Microsoft Surface Pro X",
        ]
    }
    categories = list(product_category_dict.keys())
    data = []
    for _ in range(num_of_records):
        category = random.choice(categories)
        product = random.choice(list(product_category_dict[category]))

        data.append(
            [
                faker.uuid4(),  # id (assuming auto-increment for simplicity)
                product,
                category,
                faker.company(),
                random.randint(0, 100),
                round(random.uniform(500.0, 300000.0), 2),
                faker.date_time_this_year(),  # created_at
                faker.date_time_this_year(),  # updated_at
            ]
        )
    return data


def generate_sales_data(num_records, store_ids, product_ids):
    data = []
    for _ in range(num_records):
        quantity = random.randint(1, 10)
        sale_price = round(random.uniform(500.0, 300000.0), 2)
        data.append(
            [
                faker.uuid4(),  # transaction_id
                random.choice(store_ids),
                random.choice(product_ids),
                quantity,
                sale_price,
                round(quantity * sale_price, 2),
                faker.date_time_this_decade(),  # sale_date
                random.randint(1, 100),  # supervisor_id
                faker.date_time_this_decade(),  # created_at
                faker.date_time_this_decade(),  # updated_at
            ]
        )
    return data


def generate_refunds_data(num_records, store_ids, product_ids):
    data = []
    for _ in range(num_records):
        quantity_refunded = random.randint(1, 10)
        refund_amount = round(random.uniform(500.0, 300000.0), 2)
        data.append(
            [
                faker.uuid4(),  # transaction_id
                random.choice(store_ids),
                random.choice(product_ids),
                quantity_refunded,
                refund_amount,
                faker.date_time_this_year(),  # refund_date
                random.randint(1, 100),  # supervisor_id
                faker.date_time_this_year(),  # created_at
                faker.date_time_this_year(),  # updated_at
            ]
        )
    return data


def generate_supervisors_data():
    data = []
    for i in range(1, 101):
        data.append(
            [
                i,
                faker.name(),
            ]
        )
    return data


def write_csv(filename, header, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
