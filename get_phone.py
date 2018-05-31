#! /usr/bin/python
import re
import os 
import sys

def download_files(number_prefix, filename):
    #Download web page from 51hao.cc
    wget_cmd = " wget http://www.51hao.cc/mobile/hangzhou_" + number_prefix + ".html"
    os.system(wget_cmd)
    convert_cmd = "iconv -f cp936 -t utf-8 hangzhou_" + number_prefix + ".html > " + filename
    os.system(convert_cmd)
    
    
def get_phone_prefix():
    #get phone prefix, download file from 51hao.cc
    pattern_mob_list = re.compile('135\d{4}')
    f = open("./utf_8_a")
    result = pattern_mob_list.findall(f.read())
    f.close()
    return result

def get_phone(number_prefix, filename):
    #get phone number from download file
    match_string = number_prefix + "\d{4}"
    print(match_string)
    print(">>>>>")
    pattern_mob = re.compile(match_string)
    f = open(filename)
    result = pattern_mob.findall(f.read())
    f.close()
    return result
    

if __name__ == "__main__":
    #specied phone prefix in command line to download
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
    #if you specied list of phone prefix then use below method
    """
    phone_list = get_phone_prefix()
    for number_prefix in phone_list:
        filename = "utf_8_" + number_prefix
        download_files(number_prefix, filename)
        phone_number = get_phone(number_prefix, filename)
        new_file = "./number/" + number_prefix 
        with open(new_file,'w') as f:
            for number in phone_number:
                f.write(number + "\n")
    """
