from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="a", middlename="a", lastname="a",
                                   nickname="a", title="Mr.", company="a",
                                   address="a", home="25", mobile="a",
                                   work="256985", email="a@mail.ru", address2="address2",
                                   phone2="a", notes="notes"))
    app.contact.modify_first_contact(Contact(firstname="Ivan"))

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="b", middlename="b", lastname="b",
                                   nickname="b", title="Mr.", company="b",
                                   address="b", home="25", mobile="b",
                                   work="256985", email="b@mail.ru", address2="address2",
                                   phone2="b", notes="notes"))
    app.contact.modify_first_contact(Contact(middlename="Petrovich"))