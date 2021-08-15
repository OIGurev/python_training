from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def check_empty_filling(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

def test_delete_contact_from_group(app, db):
    check_empty_filling(app, db)
    contact_to_add = db.get_contacts_not_in_groups()[0]
    group = db.get_group_list()
    random_group = random.randint(1, len(group))
    random_group_id = group[random_group - 1].id

    contacts_before_delete = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))

    if contacts_before_delete == 0:
        app.contact.add_contact_to_group_by_id(contact_to_add, random_group)
    else:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group_by_id(contact.id, random_group=random_group)
        app.contact.delete_contact_from_group_by_id(group_id=random_group_id, orm=orm)
        contacts_after_delete = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))
        assert contacts_before_delete - 1 == contacts_after_delete

def test_add_contact_to_group(app, db):
    check_empty_filling(app, db)
    contact_to_add = db.get_contacts_not_in_groups()[0]
    group = db.get_group_list()[0].id
    app.contact.add_contact_to_group_by_id(contact_to_add, group)
    new_contacts_not_in_groups = db.get_contacts_not_in_groups()
    assert contact_to_add not in new_contacts_not_in_groups

