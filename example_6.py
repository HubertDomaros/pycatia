#! /usr/bin/python3.6

"""

    Example 6:

    Open a catia file.

    Export catia file to igs.

    Close a catia file.

"""

from pycatia.base_interfaces import CATIAApplication

# path to file to open.
file_name = r'tests\CF_Part_1.CATPart'
new_file_name = 'new_part.CATPart'

catia = CATIAApplication()
# open document
documents = catia.documents()
documents.open(file_name)

document = catia.document()
# save document as new name.
document.save_as(new_file_name)

# to export to another support fileformat (license permitting).
new_export_file_name = r"c:\temp\new_export_part"
document.export_data(new_export_file_name, "stp")

# close document
document.close()
