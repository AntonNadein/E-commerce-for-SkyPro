# E-commerce-for-SkyPro

## Описание:

E-commerce - это сборник домашних заданий на Python для SkyPro в которой реализуются ООП.

## Использование:
* Клонируем репозитроий *git@github.com:AntonNadein/E-commerce-for-SkyPro.git*
* Устанавливаем зависимоти **pyproject.toml**
* В директории **data** заменяем файлы на идентичного содержания и структуры.
* Запускаем функционал при помощи файлов **main.py,**


## Документация:
1. Модуль *category* класс с категорией продукта с свойствами: название (name),описание 
(description),список товаров категории (products).
2. Модуль *product* класс с категорией продукта с свойствами: название (name),описание 
(description),цена (price),количество в наличии (quantity).
3. Модуль *utils* подгружает данные по категориями и товарам из файла 
*[products.json](data%2Fproducts.json)*

## Тестирование:
Для тестироваия используйте файлы 
**[test_category.py](tests%2Ftest_category.py)
[test_product.py](tests%2Ftest_product.py)
[test_utils.py](tests%2Ftest_utils.py)**

test coverage 100%

## Лицензия:

Этот проект не имеет лицензий.