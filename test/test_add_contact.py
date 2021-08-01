# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits + string.punctuation + " "*5
    return "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))

def random_email(prefix, maxlen1, maxlen2, maxlen3):
    symbols1 = string.digits + string.ascii_letters + "_"
    symbols2 = string.digits + string.ascii_letters
    symbols3 = string.ascii_letters
    return prefix + "".join(random.choice(symbols1) for i in range(random.randrange(maxlen1))) + "@" + "".join(random.choice(symbols2) for i in range(random.randrange(maxlen2))) + "." + "".join(random.choice(symbols3) for i in range(random.randrange(maxlen3)))

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    homephone="", mobile="", work="", email="", email2="", email3="", address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), homephone=random_phone(10), mobile=random_phone(10), work=random_phone(10),
            email=random_email("email", 10, 5, 3), email2=random_email("email2", 10, 5, 3), email3=random_email("email3", 10, 5, 3),
            address2=random_string("address2", 10), phone2=random_phone(10), notes=random_string("notes", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




