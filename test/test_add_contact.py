# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Igor", middlename="Valerievich", lastname="Petrov",
                       nickname="Igo", title="Mr.", company="hisCorp",
                       address="moscow", home="235698", mobile="+794582145698",
                       work="256985", email="igo@mail.ru", address2="address2",
                       phone2="+79991112233", notes="notes"))




