from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random

def test_del_contact_from_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="tt", middlename="ttt", lastname="tttt", nickname="testnick",
                                   title="testtitle", company="tc",
                                   homephone="123456", mobile="89111111111", work="2-12-12",
                                   email="test@test.ru", email2="test2@test.ru", email3="test3@test.ru",
                                   address="ta", phone2="13",
                                   notes="tn"))
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    edit_contact = random.choice(contacts)
    del_group_from_contact = random.choice(groups)
    if len(orm.get_contacts_in_group(del_group_from_contact)) == 0:
        app.contact.add_contact_to_group_by_id(edit_contact.id, del_group_from_contact.id)
    app.contact.delete_contact_from_group_by_id(edit_contact.id, del_group_from_contact.id)
    new_contacts = orm.get_contact_list()
    list_contacts_not_in_group = orm.get_contacts_not_in_group(del_group_from_contact)
    assert new_contacts == list_contacts_not_in_group

def test_add_contact_to_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="aa", middlename="aaa", lastname="aaaa", nickname="testnicka",
                                   title="testtitlea", company="tca",
                                   homephone="123432", mobile="89121111111", work="2-32-32",
                                   email="test@test3.ru", email2="test2@test3.ru", email3="test3@test3.ru",
                                   address="taa", phone2="132",
                                   notes="tna"))
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    edit_contact = random.choice(contacts)
    add_group_for_contact = random.choice(groups)
    app.contact.add_contact_to_group_by_id(edit_contact.id, add_group_for_contact.id)
    list_contacts_in_group = orm.get_contacts_in_group(add_group_for_contact)
    assert edit_contact in list_contacts_in_group