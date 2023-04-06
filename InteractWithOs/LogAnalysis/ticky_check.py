#!/usr/bin/env python3

import re
import operator
import csv

class ErrorAndInfo:
    def __init__(self) -> None:
        self.errorcount = 0
        self.infocount = 0

error_count_dic = {}
user_statistics = {}

def find_error_count_dic(line):
    re_result = re.search(r'ticky: ERROR ([\w ]*)', line)
    if re_result is not None:
        dic_key = re_result[1]
        if dic_key in error_count_dic:
            error_count_dic[dic_key] += 1
        else:
            error_count_dic[dic_key] = 1

def find_user_error_statistics(re_error_result):
    if re_error_result is not None:
        error_dic_key = re_error_result[1]
        if error_dic_key in user_statistics:
            user_statistics[error_dic_key].errorcount += 1
        else:
            error_and_info = ErrorAndInfo()
            error_and_info.errorcount = 1
            user_statistics[error_dic_key] = error_and_info

def find_user_info_statistics(re_info_result):
    if re_info_result is not None:
        info_dic_key = re_info_result[1]
        if info_dic_key in user_statistics:
            user_statistics[info_dic_key].infocount += 1
        else:
            error_and_info = ErrorAndInfo()
            error_and_info.infocount = 1
            user_statistics[info_dic_key] = error_and_info

def find_user_statistics(line):
    re_info_result = re.search(r'ticky: INFO .*\(([\w]*)\)', line)
    re_error_result = re.search(r'ticky: ERROR .*\(([\w]*)\)', line)
    find_user_error_statistics(re_error_result)
    find_user_info_statistics(re_info_result)

def genenrate_csv_error_count_file():
    with open('errorcount.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Error', 'Count'])
        for key, value in sorted(error_count_dic.items(), key=operator.itemgetter(1), reverse=True):
            csvwriter.writerow([key, value])

def generate_csv_user_statistics_file():
    with open('user_statistics.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username', 'INFO', 'ERROR'])
        for key, value in sorted(user_statistics.items()):
            csvwriter.writerow([key, value.infocount, value.errorcount])

def generate_csv_files():
    genenrate_csv_error_count_file()
    generate_csv_user_statistics_file()

with open('syslog.log', 'r') as logs:
    for line in logs.readlines():
        find_error_count_dic(line)
        find_user_statistics(line)
    generate_csv_files()

print('error_count_dic: {}'.format(sorted(error_count_dic.items(), key=operator.itemgetter(1), reverse=True)))
print('user_statistics_error: {}'.format(sorted(user_statistics.items())))
