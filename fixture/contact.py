from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        #init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_fields(contact)
        #submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_to_home_page()
        self.go_to_modify_page(index)
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        #fill phone numbers
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        #fill e-mail
        self.change_field_value("email", contact.email)
        #select birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("17")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1999")
        #fill secondary information form
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        #select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        #submit deletion
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        #confirm alert
        wd.switch_to_alert().accept()
        wd.implicitly_wait(0.1)
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    #navigation
    def go_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def go_to_modify_page(self, index):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("update")) > 1:
            wd.find_elements_by_name("selected[]")[index].click()
            wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
            wd.find_element_by_name("modifiy").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name=entry]"):
                firstname = element.find_elements_by_tag_name("td")[2].text
                lastname = element.find_elements_by_tag_name("td")[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)