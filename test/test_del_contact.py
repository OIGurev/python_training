

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.go_to_home_page()
    app.contact.delete_first_contact()
    app.session.logout()