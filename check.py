import sys
import re
import json

if len(sys.argv) != 3:
    print("Usage: python script.py <filename>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, 'r') as f:
    lines = f.readlines()

# rest of the script here...
re_replace = re.compile(r'^\d+(?:,\d+)?c\d+(?:,\d+)?$')
re_delete = re.compile(r'^\d+(?:,\d+)?d\d+(?:,\d+)?$')
re_add = re.compile(r'^\d+a\d+(?:,\d+)?$')

key_for_replacing = ""
key_for_deleting = ""
key_for_adding = ""

differences = {}
for line in lines:
    old_file_line = re.search(r'^<.*', line)
    new_file_line = re.search(r'^>.*', line)

    if re_replace.match(line):
        key_for_deleting = ""
        key_for_adding = ""
        key_for_replacing = line.strip()
        differences[key_for_replacing] = dict()
        differences[key_for_replacing]['old_file_line'] = []
        differences[key_for_replacing]['new_file_line'] = []
    elif re_delete.match(line):
        key_for_replacing = ""
        key_for_adding = ""
        key_for_deleting = line.strip()
        differences[key_for_deleting] = dict()
        differences[key_for_deleting]['deleted_line'] = []
    elif re_add.match(line):
        key_for_replacing = ""
        key_for_deleting = ""
        key_for_adding = line.strip()
        differences[key_for_adding] = dict()
        differences[key_for_adding]['new_file_line'] = []
    elif old_file_line and key_for_replacing:
        first_file_string = old_file_line.group()[2:]
        differences[key_for_replacing]['old_file_line'].append(first_file_string)
    elif new_file_line and key_for_replacing:
        second_file_string = new_file_line.group()[2:]
        differences[key_for_replacing]['new_file_line'].append(second_file_string)
    elif old_file_line and key_for_deleting:
        deleted_string = old_file_line.group()[2:]
        differences[key_for_deleting]['deleted_line'].append(deleted_string)
    elif new_file_line and key_for_adding:
        added_string = new_file_line.group()[2:]
        differences[key_for_adding]['new_file_line'].append(added_string)

result = {'differences': differences}

with open(output_filename, 'w') as f:
    json.dump(result, f, indent=4)

        if num > max_num:
            max_num = num
    return max_num
