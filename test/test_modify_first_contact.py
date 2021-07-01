from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.go_to_home_page()
    app.contact.go_to_modify_page()
    app.contact.modify_first_contact(Contact(firstname="Ivan"))
    app.session.logout()

def test_modify_first_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.go_to_home_page()
    app.contact.go_to_modify_page()
    app.contact.modify_first_contact(Contact(middlename="Petrovich"))
    app.session.logout()