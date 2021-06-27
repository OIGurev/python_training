def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.go_to_modify_page()
    app.group.modify_group()
    app.session.logout()