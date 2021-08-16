import re

from model.contact import Contact

def test_info_on_home_page_and_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    list_contacts_from_home_page = list(
        map(lambda i: (i.id, i.firstname, i.lastname, i.all_phones_from_home_page, i.all_emails_from_home_page,
                       i.address), contacts_from_home_page))
    list_contacts_from_db = list(
        map(lambda i: (i.id, i.firstname, i.lastname, merge_phones_like_on_home_page(i),
                       merge_emails_like_on_home_page(i), i.address), contacts_from_db))
    assert sorted(list_contacts_from_home_page, key=lambda i: i[0]) == sorted(list_contacts_from_db, key=lambda i: i[0])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))