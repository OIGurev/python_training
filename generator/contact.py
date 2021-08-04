import os.path
import random
import string
import jsonpickle
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits
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
    for i in range(n)
]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))