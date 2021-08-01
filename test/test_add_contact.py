# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Igor", middlename="Valerievich", lastname="Petrov",
                      nickname="Igo", title="Mr.", company="hisCorp",
                      address="moscow", homephone="235698", mobile="+794582145698",
                      work="256985", email="igo@mail.ru", email2="igo2@mail.ru", email3="igo3@mail.ru", address2="address2",
                      phone2="+79991112233", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




