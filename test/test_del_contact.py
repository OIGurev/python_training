from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Nikita", middlename="Sergeevich", lastname="Rushev",
                       nickname="Nick", title="Mr.", company="unity",
                       address="moscow", home="25", mobile="none",
                       work="256985", email="nsr@mail.ru", address2="address2",
                       phone2="none", notes="notes"))
    app.contact.delete_first_contact()