#! /usr/bin/python3.6

from pycatia.base_interfaces import CATIAApplication
from tests.source_files import cat_part_measurable

catia = CATIAApplication()


def test_application():
    assert 'CATIAApplication' in catia.__repr__()


def test_refresh():
    documents = catia.documents()
    documents.open(cat_part_measurable)
    document = catia.document()

    catia.refresh_display(state=False)
    assert catia.refresh_display() is False

    catia.refresh_display(state=True)
    assert catia.refresh_display() is True

    document.close()


def test_visible():
    documents = catia.documents()
    documents.open(cat_part_measurable)
    document = catia.document()

    catia.visible(state=False)
    assert catia.visible() is False

    catia.visible(state=True)
    assert catia.visible() is True

    document.close()
