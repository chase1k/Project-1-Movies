"""
CSCI-140/242

A program that demonstrates custom sorting a list of dataclass objects by
several fields.

Author: RIT CS

$ python3.9 dataclass_demo.py
Before sorting:
Product(id=10, name='Snuggie', cost=19.99)
Product(id=20, name='OxiClean', cost=9.01)
Product(id=30, name='ShamWow!', cost=5.99)
Product(id=40, name='Schticky', cost=5.99)
Product(id=50, name='SlapChop', cost=19.99)
Product(id=60, name='Clapper', cost=19.99)

After sorting:
Product(id=60, name='Clapper', cost=19.99)
Product(id=50, name='SlapChop', cost=19.99)
Product(id=10, name='Snuggie', cost=19.99)
Product(id=20, name='OxiClean', cost=9.01)
Product(id=40, name='Schticky', cost=5.99)
Product(id=30, name='ShamWow!', cost=5.99)
"""


from dataclasses import dataclass
import operator


@dataclass(frozen=True)
class Product:
    """A dataclass to represent a product."""
    identifier: int
    name: str
    cost: float


def custom_sort(products: list[Product]) -> None:
    """
    A custom sort function for a list of Product's.  Here, the intention
    is to have the data sorted first in descending order by cost, and
    second in ascending order by name.

    :param products: the list of Product's to be sorted (in place)
    """
    # notice that the order of the sorts are reversed!
    # 1. sort by secondary which is names in ascending order
    products.sort(key=operator.attrgetter('name'))
    # 2. sort by primary which is cost in reverse order.
    products.sort(key=operator.attrgetter('cost'), reverse=True)


def print_products(products: list[Product]) -> None:
    """
    Displays the elements of a list of products in order.
    :param products: the list of Product's to display
    """
    for product in products:
        print(product)


def main():
    """Create and sort the products."""
    products = [Product(10, 'Snuggie', 19.99),
                Product(20, 'OxiClean', 9.01),
                Product(30, 'ShamWow!', 5.99),
                Product(40, 'Schticky', 5.99),
                Product(50, 'SlapChop', 19.99),
                Product(60, 'Clapper', 19.99)]
    print('Before sorting:')
    print_products(products)
    custom_sort(products)
    print('\nAfter sorting:')
    print_products(products)


if __name__ == '__main__':
    main()
