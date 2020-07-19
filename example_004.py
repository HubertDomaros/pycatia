#! /usr/bin/python3.6

"""

    Example 4:

    Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

"""

from pycatia import catia
from pycatia.enumeration.enumeration_types import cat_work_mode_type

documents = catia.documents
documents.open(r'tests/cat_files/product_top.CATProduct')
document = catia.active_document
product = document.product()

# Change the work mode to Design Mode.
# This is useful for CATIA configurations that work with a cache otherwise
# methods on children may fail due to the document not being loaded.
product.apply_work_mode(cat_work_mode_type.index("DESIGN_MODE"))

products = product.get_products()

if len(products) == 0:
    print("Active document has no children or is not a CATProduct.")

for item in products:

    if item.is_catpart():
        print(f'This is a part: "{item}"')
        print('')

    if item.is_catproduct():
        product = item
        print(f'This is a product: "{item}"')

        if item.has_children():
            print('This product has children.')
            children = item.get_children()
            print(children)
        print('')
