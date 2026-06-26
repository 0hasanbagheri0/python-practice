"""
Data Generator Script / اسکریپت تولید داده‌های ساختگی
----------------------------------------------------
Generates fake data for testing and demonstration
تولید داده‌های ساختگی برای تست و نمایش

Features / ویژگی‌ها:
- Generate random user data / تولید داده‌های تصادفی کاربران
- Generate random product data / تولید داده‌های تصادفی محصولات
- Generate random sales data / تولید داده‌های تصادفی فروش
- Export to CSV and JSON / خروجی به CSV و JSON
- Customizable data types / انواع داده قابل تنظیم
"""

import random
import pandas as pd
from datetime import datetime, timedelta
import json
import argparse
from pathlib import Path

class DataGenerator:
    """
    Data generator class / کلاس تولید داده
    """
    
    # Sample data / داده‌های نمونه
    FIRST_NAMES = [
        'Hasan', 'Ali', 'Mohammad', 'Sara', 'Maryam', 'Zahra',
        'Reza', 'Amir', 'Neda', 'Leila', 'Hossein', 'Ahmad',
        'Fatemeh', 'Mehdi', 'Mina', 'Saeed', 'Maryam', 'Morteza'
    ]
    
    LAST_NAMES = [
        'Bagheri', 'Ahmadi', 'Mohammadi', 'Karimi', 'Rezaei',
        'Rahimi', 'Hashemi', 'Hosseini', 'Mousavi', 'Naderi',
        'Gholami', 'Moradi', 'Zare', 'Sadeghi', 'Ebrahimi'
    ]
    
    CITIES = [
        'Tehran', 'Mashhad', 'Isfahan', 'Shiraz', 'Tabriz',
        'Ahvaz', 'Kerman', 'Rasht', 'Kermanshah', 'Qom'
    ]
    
    PRODUCTS = [
        'Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Keyboard',
        'Mouse', 'Monitor', 'Printer', 'Camera', 'Smart Watch',
        'Speaker', 'Drone', 'VR Headset', 'Power Bank', 'USB Drive'
    ]
    
    COMPANIES = [
        'TechCorp', 'DataSystems', 'CloudNet', 'AI Solutions',
        'ByteWorks', 'CodeForge', 'DataStream', 'PixelTech',
        'Quantum', 'LogicWare', 'CyberCore', 'NanoTech'
    ]
    
    def __init__(self, seed=42):
        """
        Initialize data generator / مقداردهی اولیه تولید داده
        """
        random.seed(seed)
    
    def generate_phone(self):
        """
        Generate random phone number / تولید شماره تلفن تصادفی
        """
        return f"09{random.randint(10, 99)}{random.randint(1000000, 9999999)}"
    
    def generate_email(self, first_name, last_name):
        """
        Generate email from name / تولید ایمیل از نام
        """
        domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'company.com', 'email.com']
        return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
    
    def generate_date(self, start_date, end_date):
        """
        Generate random date / تولید تاریخ تصادفی
        """
        time_between = end_date - start_date
        days_between = time_between.days
        random_days = random.randrange(days_between)
        return start_date + timedelta(days=random_days)
    
    def generate_users(self, count=100):
        """
        Generate random user data / تولید داده‌های تصادفی کاربران
        """
        users = []
        for _ in range(count):
            first_name = random.choice(self.FIRST_NAMES)
            last_name = random.choice(self.LAST_NAMES)
            age = random.randint(18, 65)
            
            user = {
                'first_name': first_name,
                'last_name': last_name,
                'age': age,
                'email': self.generate_email(first_name, last_name),
                'phone': self.generate_phone(),
                'city': random.choice(self.CITIES),
                'is_active': random.choice([True, False]),
                'score': round(random.uniform(0, 100), 2),
                'registered_date': self.generate_date(
                    datetime(2020, 1, 1),
                    datetime(2026, 1, 1)
                )
            }
            users.append(user)
        
        return users
    
    def generate_products(self, count=50):
        """
        Generate random product data / تولید داده‌های تصادفی محصولات
        """
        products = []
        used_names = set()
        
        for _ in range(count):
            # Ensure unique product names / اطمینان از نام‌های یکتا
            name = random.choice(self.PRODUCTS)
            while name in used_names:
                name = f"{random.choice(self.PRODUCTS)} {random.randint(1, 99)}"
            used_names.add(name)
            
            product = {
                'id': f"P{random.randint(10000, 99999)}",
                'name': name,
                'category': random.choice(['Electronics', 'Clothing', 'Books', 'Food', 'Software']),
                'price': round(random.uniform(5, 1000), 2),
                'stock': random.randint(0, 500),
                'weight': round(random.uniform(0.1, 20), 2),
                'rating': round(random.uniform(1, 5), 1),
                'in_stock': random.choice([True, False]),
                'created_date': self.generate_date(
                    datetime(2022, 1, 1),
                    datetime(2026, 1, 1)
                )
            }
            products.append(product)
        
        return products
    
    def generate_sales(self, users, products, count=200):
        """
        Generate random sales data / تولید داده‌های تصادفی فروش
        """
        sales = []
        
        for _ in range(count):
            user = random.choice(users)
            product = random.choice(products)
            quantity = random.randint(1, 10)
            
            sale = {
                'sale_id': f"S{random.randint(100000, 999999)}",
                'user_id': users.index(user) + 1,
                'user_name': f"{user['first_name']} {user['last_name']}",
                'product_id': product['id'],
                'product_name': product['name'],
                'quantity': quantity,
                'unit_price': product['price'],
                'total_price': round(product['price'] * quantity, 2),
                'sale_date': self.generate_date(
                    datetime(2024, 1, 1),
                    datetime(2026, 6, 1)
                ),
                'payment_method': random.choice(['Cash', 'Credit Card', 'Online', 'Crypto']),
                'status': random.choice(['Completed', 'Pending', 'Cancelled'])
            }
            sales.append(sale)
        
        return sales
    
    def generate_all_data(self, user_count=100, product_count=50, sale_count=200):
        """
        Generate all data types / تولید همه انواع داده
        """
        print("🔄 Generating data...")
        
        users = self.generate_users(user_count)
        print(f"✓ Generated {len(users)} users")
        
        products = self.generate_products(product_count)
        print(f"✓ Generated {len(products)} products")
        
        sales = self.generate_sales(users, products, sale_count)
        print(f"✓ Generated {len(sales)} sales")
        
        return {
            'users': users,
            'products': products,
            'sales': sales
        }
    
    def save_to_csv(self, data, directory='generated_data'):
        """
        Save data to CSV files / ذخیره داده در فایل‌های CSV
        """
        directory = Path(directory)
        directory.mkdir(exist_ok=True)
        
        for name, records in data.items():
            df = pd.DataFrame(records)
            filepath = directory / f"{name}.csv"
            df.to_csv(filepath, index=False)
            print(f"✓ Saved {name} to {filepath}")
    
    def save_to_json(self, data, directory='generated_data'):
        """
        Save data to JSON files / ذخیره داده در فایل‌های JSON
        """
        directory = Path(directory)
        directory.mkdir(exist_ok=True)
        
        for name, records in data.items():
            filepath = directory / f"{name}.json"
            
            # Convert datetime objects to strings / تبدیل datetime به رشته
            def json_serial(obj):
                if isinstance(obj, datetime):
                    return obj.isoformat()
                raise TypeError(f"Type {type(obj)} not serializable")
            
            with open(filepath, 'w') as f:
                json.dump(records, f, indent=2, default=json_serial)
            
            print(f"✓ Saved {name} to {filepath}")
    
    def generate_summary(self, data):
        """
        Generate summary of generated data / تولید خلاصه داده‌های تولید شده
        """
        print("\n" + "=" * 60)
        print("DATA SUMMARY / خلاصه داده‌ها")
        print("=" * 60)
        
        for name, records in data.items():
            print(f"\n📊 {name.upper()}:")
            print(f"  Count: {len(records)}")
            
            if records:
                first_record = records[0]
                print(f"  Sample record:")
                for key, value in first_record.items():
                    print(f"    {key}: {value}")


def main():
    """
    Command line interface / رابط خط فرمان
    """
    parser = argparse.ArgumentParser(
        description='Generate fake data for testing'
    )
    parser.add_argument(
        '--users',
        type=int,
        default=100,
        help='Number of users to generate (default: 100)'
    )
    parser.add_argument(
        '--products',
        type=int,
        default=50,
        help='Number of products to generate (default: 50)'
    )
    parser.add_argument(
        '--sales',
        type=int,
        default=200,
        help='Number of sales to generate (default: 200)'
    )
    parser.add_argument(
        '--format',
        choices=['csv', 'json', 'both'],
        default='both',
        help='Output format (default: both)'
    )
    parser.add_argument(
        '--output',
        default='generated_data',
        help='Output directory (default: generated_data)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )
    
    args = parser.parse_args()
    
    # Create generator / ایجاد تولیدکننده
    generator = DataGenerator(seed=args.seed)
    
    # Generate data / تولید داده
    data = generator.generate_all_data(
        user_count=args.users,
        product_count=args.products,
        sale_count=args.sales
    )
    
    # Generate summary / تولید خلاصه
    generator.generate_summary(data)
    
    # Save data / ذخیره داده
    print("\n💾 Saving data...")
    
    if args.format in ['csv', 'both']:
        generator.save_to_csv(data, args.output)
    
    if args.format in ['json', 'both']:
        generator.save_to_json(data, args.output)
    
    print(f"\n✅ All data saved to: {args.output}/")


if __name__ == "__main__":
    main()

# === Example Usage / مثال استفاده ===
print("\n" + "=" * 60)
print("DATA GENERATOR - EXAMPLES / مثال‌ها")
print("=" * 60)

print("""
📊 How to use / نحوه استفاده:

1. Generate default data (100 users, 50 products, 200 sales):
   python data_generator.py

2. Generate with custom counts:
   python data_generator.py --users 200 --products 100 --sales 500

3. Generate only CSV files:
   python data_generator.py --format csv

4. Generate only JSON files:
   python data_generator.py --format json

5. Custom output directory:
   python data_generator.py --output my_data

6. Set random seed for reproducibility:
   python data_generator.py --seed 123

Generated data includes:
- Users: Personal info, contact details, registration dates
- Products: Product details, prices, stock levels
- Sales: Purchase records linking users and products
""")
