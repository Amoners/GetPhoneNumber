#! /usr/bin/python
import re
import os 
import sys

def download_files(number_prefix, filename):
    wget_cmd = " wget http://www.51hao.cc/mobile/hangzhou_" + number_prefix + ".html"
    os.system(wget_cmd)
    convert_cmd = "iconv -f cp936 -t utf-8 hangzhou_" + number_prefix + ".html > " + filename
    os.system(convert_cmd)
    
    
def get_phone_prefix():
    pattern_mob_list = re.compile('135\d{4}')
    f = open("./utf_8_a")
    result = pattern_mob_list.findall(f.read())
    f.close()
    return result

def get_phone(number_prefix, filename):
    match_string = number_prefix + "\d{4}"
    print(match_string)
    print(">>>>>")
    pattern_mob = re.compile(match_string)
    f = open(filename)
    result = pattern_mob.findall(f.read())
    f.close()
    return result
    

if __name__ == "__main__":
    #phone_list = get_phone_prefix()
    if len(sys.argv) < 2:
        print("ERROR: Please specify number in command")
        exit()
    number_prefix = sys.argv[1]
    filename = "utf_8_" + number_prefix
    download_files(number_prefix, filename)
    phone_number = get_phone(number_prefix, filename)
    #new_file = "./number/" + number_prefix 
    new_file = "./specify/" + number_prefix 
    with open(new_file,'w') as f:
        for number in phone_number:
            f.write(number + "\n")
    """
    for number_prefix in phone_list:
        filename = "utf_8_" + number_prefix
        download_files(number_prefix, filename)
        phone_number = get_phone(number_prefix, filename)
        new_file = "./number/" + number_prefix 
        with open(new_file,'w') as f:
            for number in phone_number:
                f.write(number + "\n")
    """
