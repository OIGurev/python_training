from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.go_to_home_page()
    app.contact.go_to_modify_page()
    #передаем в метод объект указывая все его доступные аргументы (а не только firstname) чтобы исключить конфликт
    app.contact.modify_first_contact(Contact(firstname="Ivan", middlename="", lastname="",
                       nickname="", title="", company="",
                       address="", home="", mobile="",
                       work="", email="", address2="",
                       phone2="", notes=""))
    app.session.logout()