import sys
import json


class Contact(object):
    def __init__(self, name, personal_phone, mobile_phone, additional_info):
        self.name = name
        self.personal_phone = personal_phone
        self.mobile_phone = mobile_phone
        self.additional_info = additional_info

    def set_name(self, name: str):
        self.name = name

    def set_personal_phone(self, personal_phone: str):
        self.personal_phone = personal_phone

    def set_mobile_phone(self, mobile_phone: str):
        self.mobile_phone = mobile_phone

    def set_additional_info(self, additional_info: str):
        self.additional_info = additional_info

    def get_name(self) -> str:
        return self.name

    def get_personal_phone(self) -> str:
        return self.personal_phone

    def get_mobile_phone(self) -> str:
        return self.mobile_phone

    def get_additional_info(self) -> str:
        return self.additional_info


class Phonebook:
    def __init__(self):
        self.contact_list = list()
        self.menu()

    def add(self):
        name = input("Enter name: ")
        personal_phone = input("Enter personal phone: ")
        mobile_phone = input("Enter mobile phone: ")
        additional_info = input("Enter additional information: ")
        contact = Contact(name, personal_phone, mobile_phone, additional_info)
        self.contact_list.append(contact)
        self.menu()

    def print_all(self):
        print("Contacts\n")
        for num, val in enumerate(self.contact_list):
            print("\tName: ", val.get_name())
            print("\tPersonal phone: ", val.get_personal_phone())
            print("\tMobile phone: ", val.get_mobile_phone())
            print("\tAdditional information: ", val.get_additional_info())
        self.menu()

    def exit(self):
        sys.exit(0)

    def menu(self):
        print("\nMenu\n")
        print("1-Read all\n2-Add new\n3-Export to json\n4-Import from json\n5-Exit\n")
        choice = input("Enter number: ")
        choice_menu = {'1': self.print_all,
                       '2': self.add,
                       '3': self.export_contacts,
                       '4': self.import_contacts,
                       '5': self.exit}
        if choice not in choice_menu.keys():
            print("Please enter correct number")
        else:
            choice_menu[choice]()

    def export_contacts(self):
        data = {"contacts": []}
        for contact in self.contact_list:
            data['contacts'].append({
                "name": contact.get_name(),
                "personal phone": contact.get_personal_phone(),
                "mobile phone": contact.get_mobile_phone(),
                "additional": contact.get_additional_info()
            })
        with open('contacts.json', 'w') as outfile:
            json.dump(data, outfile)
        self.menu()

    def import_contacts(self):
        with open('contacts.json') as json_file:
            data = json.load(json_file)
            self.contact_list = list()
            for contacts_list in data["contacts"]:
                name = contacts_list["name"]
                personal_phone = contacts_list["personal phone"]
                mobile_phone = contacts_list["mobile phone"]
                additional_info = contacts_list["additional"]
                contact = Contact(name, personal_phone, mobile_phone, additional_info)
                self.contact_list.append(contact)
        self.menu()


Phonebook()
