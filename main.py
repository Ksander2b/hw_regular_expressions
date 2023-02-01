from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def move_names():
  for value in contacts_list[1:]:
    lastname = value[0].split(' ')
    name = value[1].split(' ')
    if len(lastname) == 3:
      value[0] = lastname[0]
      value[1] = lastname[1]
      value[2] = lastname[2]
    if len(lastname) == 2:
      value[0] = lastname[0]
      value[1] = lastname[1]
    if len(name) == 2:
      value[1] = name[0]
      value[2] = name[1]


def replace_phones():
  for value in contacts_list[1:]:
    pattern = r'(\+7|8)?\s*?\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d*)[\s,]?\(?(доб.)?\s?(\d{4})?\)?'
    sub = r'+7(\2)\3-\4-\5\6\7'
    value[5] = re.sub(pattern, sub, value[5])


def duplicates_merging():
  new_list = []
  contacts_list[2].append('')
  for contact in contacts_list[1:]:
    first_name = contact[0]
    last_name = contact[1]
    for contact_2 in contacts_list:
      new_first_name = contact_2[0]
      new_last_name = contact_2[1]
      if first_name == new_first_name and last_name == new_last_name:
        if contact[2] == '':
          contact[2] = contact_2[2]
        if contact[3] == '':
          contact[3] = contact_2[3]
        if contact[4] == '':
          contact[4] = contact_2[4]
        if contact[5] == '':
          contact[5] = contact_2[5]
        if contact[6] == '':
          contact[6] = contact_2[6]
  for contact in contacts_list:
    if contact not in new_list:
      new_list.append(contact)
  return new_list


if __name__ == '__main__':
  move_names()
  replace_phones()
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(duplicates_merging())