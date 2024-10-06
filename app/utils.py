import csv
import logging
import os
import sys
from collections import defaultdict, namedtuple
from datetime import date, timedelta
from typing import NamedTuple
from pprint import pformat

from dotenv import load_dotenv

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
load_dotenv()

FILE_PATH = os.getenv('FILE_PATH')


TypeSale = NamedTuple(
    "Sale",
    [
        ('product_name', str),
        ('quantity', int),
        ('price', float),
        ('date', date)
    ]
)

Sale = namedtuple("Sale", ["product_name", "quantity", "price", "date"])


def read_sales_data(file_path: str) -> list[TypeSale]:
    '''Функция принимает путь к файлу и возвращает список продаж.
    Продажи в свою очередь являются словарями с ключами
    product_name, quantity, price, date (название, количество, цена, дата)'''
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл с именем \"{file_path}\" не обнаружен. Проверьте корректность пути к нему в .env")
    sales = list()
    with open(file_path, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sales.append(
                Sale(
                    product_name=row["product_name"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"]),
                    date=date.fromisoformat(row["date"])
                )
            )
    return sales

def total_sales_per_product(sales_data: list[TypeSale]) -> dict[str, float]:
    '''Функция принимает список продаж и возвращает словарь,
    где ключ - название продукта, а значение - общая сумма продаж этого продукта'''
    
    sales_agg = defaultdict(float)
    for sale in sales_data:
        sales_agg[sale.product_name] += sale.price * sale.quantity
    return dict(sales_agg)

def sales_over_time(sales_data: list[TypeSale]) -> dict[str, float]:
    '''Функция принимает список продаж и возвращает словарь,
    где ключ - дата, а значение общая сумма продаж за эту дату'''
    
    sales_agg = defaultdict(float)
    for sale in sales_data:
        sales_agg[sale.date] += sale.price * sale.quantity
    return dict(sales_agg)

def generate_dates(start_date: date, end_date: date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date = current_date + timedelta(days=1)
        
def fill_missing_dates(data_dict: dict) -> dict:
    dates = sorted(set(data_dict.keys()))
    
    start_date = min(dates)
    end_date = max(dates)
    
    all_dates = list(generate_dates(start_date, end_date))
    
    filled_data = {}
    for d in all_dates:
        filled_data[d] = data_dict.get(d, 0)
    
    return filled_data


if __name__ == "__main__":
    logging.debug("Запуск функции read_sales_data...")
    logging.debug(read_sales_data.__doc__)
    sales = read_sales_data(FILE_PATH)
    logging.debug(pformat(sales))
    
    logging.debug("Запуск функции total_sales_per_product...")
    logging.debug(total_sales_per_product.__doc__)
    sales_agg_by_product = total_sales_per_product(sales)
    logging.debug(pformat(sales_agg_by_product))
    
    logging.debug("Запуск функции sales_over_time...")
    logging.debug(sales_over_time.__doc__)
    sales_agg_by_date = sales_over_time(sales)
    logging.debug(pformat(sales_agg_by_date))