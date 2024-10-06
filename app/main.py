import logging
import sys
from os.path import abspath, dirname

sys.path.append(dirname(abspath(__file__)))

import matplotlib.pyplot as plt
import seaborn as sns
from utils import (
    FILE_PATH,
    fill_missing_dates,
    read_sales_data,
    sales_over_time,
    total_sales_per_product,
)

logging.getLogger().setLevel(logging.WARNING)


if __name__ == "__main__":
    sales = read_sales_data(FILE_PATH)
    
    sales_agg_by_product = total_sales_per_product(sales)
    sales_agg_by_date = sales_over_time(sales)
    
    most_profitable_product = max(sales_agg_by_product.items(), key=lambda x: x[1])
    most_profitable_date = max(sales_agg_by_date.items(), key=lambda x: x[1])
    
    print("Продукт, принесший наибольшую выручку: {} ({} у.е.)".format(*most_profitable_product))
    print("День, с наибольшей суммой продаж: {} ({} у.е.)".format(*most_profitable_date))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    
    data_sales_agg_by_product = sorted(sales_agg_by_product.items(), key=lambda x: x [1], reverse=True)
    
    products = [item[0] for item in data_sales_agg_by_product]
    total_price_by_product = [item[1] for item in data_sales_agg_by_product]
    
    sns.barplot(ax=ax1, x=products, y=total_price_by_product)
    ax1.set_title('Выручка по товарам')
    ax1.set_xlabel('Товар')
    ax1.set_ylabel('Выручка')
    
    data_sales_agg_by_date_without_miss = sorted(fill_missing_dates(sales_agg_by_date).items(), key=lambda x: x[0])
    
    dates = [item[0] for item in data_sales_agg_by_date_without_miss]
    total_price_by_date = [item[1] for item in data_sales_agg_by_date_without_miss]
    
    sns.barplot(ax=ax2, x=dates, y=total_price_by_date)
    ax2.set_title('Выручка по датам')
    ax2.set_xlabel('Дата')
    ax2.set_ylabel('Выручка')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()