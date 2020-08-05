#! /usr/bin/python3.6

from pycatia import catia
from tests.source_files import cat_part_measurable


def test_application():
    caa = catia()
    assert 'Application(name="CNEXT")' in caa.__repr__()


def test_refresh():
    caa = catia()
    documents = caa.documents
    documents.open(cat_part_measurable)
    document = caa.active_document

    caa.refresh_display = False
    assert caa.refresh_display is False

    caa.refresh_display = True
    assert caa.refresh_display is True

    document.close()


def test_visible():
    caa = catia()
    documents = caa.documents
    documents.open(cat_part_measurable)
    document = caa.active_document

    caa.visible = False
    assert caa.visible is False

    caa.visible = True
    assert caa.visible is True

    document.close()
