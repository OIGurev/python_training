from random import randrange
from model.contact import Contact

def test_modify_some_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="a", middlename="a", lastname="a",
                                   nickname="a", title="Mr.", company="a",
                                   address="a", homephone="25", mobile="a",
                                   work="256985", email="a@mail.ru", address2="address2",
                                   phone2="a", notes="notes"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Ivan")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_modify_some_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="b", middlename="b", lastname="b",
                                   nickname="b", title="Mr.", company="b",
                                   address="b", homephone="25", mobile="b",
                                   work="256985", email="b@mail.ru", address2="address2",
                                   phone2="b", notes="notes"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="Vasilyev")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

