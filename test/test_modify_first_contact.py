from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="a", middlename="a", lastname="a",
                                   nickname="a", title="Mr.", company="a",
                                   address="a", home="25", mobile="a",
                                   work="256985", email="a@mail.ru", address2="address2",
                                   phone2="a", notes="notes"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Ivan"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="b", middlename="b", lastname="b",
                                   nickname="b", title="Mr.", company="b",
                                   address="b", home="25", mobile="b",
                                   work="256985", email="b@mail.ru", address2="address2",
                                   phone2="b", notes="notes"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="Petrovich"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)