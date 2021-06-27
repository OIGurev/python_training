# -*- coding: utf-8 -*-
import pytest


from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Igor", middlename="Valerievich", lastname="Petrov",
                       nickname="Igo", title="Mr.", company="hisCorp",
                       address="moscow", home="235698", mobile="+794582145698",
                       work="256985", email="igo@mail.ru", address2="address2",
                       phone2="+79991112233", notes="notes"))
    app.session.logout()




