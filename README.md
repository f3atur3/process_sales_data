# Итоговое задание №4

![Python Version](https://img.shields.io/badge/python-3.10-blue)
![Matplotlib Version](https://img.shields.io/badge/matplotlib-3.9-blue)

## Описание проекта

Этот проект представляет собой программу, которая позволяет анализировать данные о продажах продуктов в магазине и строит графики наглядного представления информации

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/f3atur3/process_sales_data.git
    cd process_sales_data
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Укажите путь до файла с данными:

    В файле .env укажите в переменной FILE_PATH пусть до csv файла с данными

## Использование

Запустите main.py командой:

  ```bash
  python main.py
  ```

Обратите внимание, что файл с данными должен иметь заголовок "product_name","quantity","price","date"

где product_name - это строка, quantity - целое число, price - вещественное число, date - дата в ISO формате (2024-09-13)
