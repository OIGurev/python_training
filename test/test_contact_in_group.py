from model.contact import Contact
from model.group import Group
import random
import allure


def test_del_contact_from_group(app, orm):
    with allure.step('Given a non-empty contact list'):
        # создаем контакт если их нет
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="tt", middlename="ttt", lastname="tttt", nickname="testnick",
                                       title="testtitle", company="tc",
                                       homephone="123456", mobile="89111111111", work="2-12-12",
                                       email="test@test.ru", email2="test2@test.ru", email3="test3@test.ru",
                                       address="ta", phone2="13",
                                       notes="tn"))
        # сохраняем в переменную полученный список контактов
        contacts = orm.get_contact_list()
    with allure.step('Given a non-empty group list'):
        # создаем группу если их нет
        if app.group.count() == 0:
            app.group.create(Group(name='Test'))
        # сохраняем в переменную полученный список контактов
        groups = orm.get_group_list()
    with allure.step('Given a random contact from the list'):
        # выбираем случайный контакт который будем удалять из группы
        edit_contact = random.choice(contacts)
    with allure.step('Given a random group from the list'):
        # выбираем случайную группу из которой будем удалять контакт
        del_group_from_contact = random.choice(groups)
    # сохраняем список контактов входящих в группу
    list_contacts_in_group = orm.get_contacts_in_group(del_group_from_contact)
    # если выбранный контакт не входит в группу, то добавляем его туда
    if edit_contact not in list_contacts_in_group:
        app.contact.add_contact_to_group_by_id(edit_contact.id, del_group_from_contact.id)
    with allure.step('When I delete contact %s in group %s from the list' % (edit_contact, del_group_from_contact)):
        # удаляем выбранный контакт из выбранной группы
        app.contact.delete_contact_from_group_by_id(edit_contact.id, del_group_from_contact.id)
    with allure.step('Then the edited contact will not be in the contact list of the selected group'):
        # получаем список контактов, не входящих в выбранную группу
        list_contacts_not_in_group = orm.get_contacts_not_in_group(del_group_from_contact)
        # проверяем что удаленный контакт находится в списке контактов не входящих в выбранную группу
        assert edit_contact in list_contacts_not_in_group

def test_add_contact_to_group(app, orm):
    with allure.step('Given a non-empty contact list'):
        # создаем контакт если их нет
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="aa", middlename="aaa", lastname="aaaa", nickname="testnicka",
                                       title="testtitlea", company="tca",
                                       homephone="123432", mobile="89121111111", work="2-32-32",
                                       email="test@test3.ru", email2="test2@test3.ru", email3="test3@test3.ru",
                                       address="taa", phone2="132",
                                       notes="tna"))
        # получаем список контактов
        contacts = orm.get_contact_list()
    with allure.step('Given a non-empty group list'):
        # создаем группу если их нет
        if app.group.count() == 0:
            app.group.create(Group(name='Test'))
        # получаем список групп
        groups = orm.get_group_list()
    #if orm.all_contacts_in_all_groups(groups):
    #    app.group.create(Group(name='Test'))
    with allure.step('Given a random contact from the list'):
        edit_contact = random.choice(contacts)
    with allure.step('Given a random group from the list'):
        add_group_to_contact = random.choice(groups)
        # сохраняем список контактов входящих в группу
        list_contacts_in_group = orm.get_contacts_in_group(add_group_to_contact)
        # если выбранный контакт входит в группу, то даляем его оттуда
        if edit_contact in list_contacts_in_group:
            app.contact.delete_contact_from_group_by_id(edit_contact.id, add_group_to_contact.id)
    with allure.step('When I add contact %s in group %s from the list' % (edit_contact, add_group_to_contact)):
        # добавляем контакт в группу
        app.contact.add_contact_to_group_by_id(edit_contact.id, add_group_to_contact.id)
    with allure.step('Then the edited contact will be in the contact list of the selected group'):
        list_contacts_in_group = orm.get_contacts_in_group(add_group_to_contact)
        # проверяем что контакт находится в списке контактов входящих в группу
        assert edit_contact in list_contacts_in_group

