def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.go_to_modify_page()
    app.contact.modify_contact()
    app.session.logout()