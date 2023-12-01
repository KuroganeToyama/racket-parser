import argparse
import csv
import os
import re
import sys
sys.path.append("Path to rkt_aprser_restrictions.py")
from rkt_parser_restrictions import *

pattern = r"Regex for files you don't want the script to care about"
dest = "Directory for output csv"

# Parse file and extract the function body of func
def rkt_parser(file, func):
    target = f"(define ({func}"

    func_collector = ""
    line_count = 0

    with open(file, "r") as f:
        for line in f:
            line_count += 1

            if line.startswith(target):
                func_collector += line
                open_brackets = line.count('(')
                close_brackets = line.count(')')

                try:
                    while open_brackets != close_brackets:
                        line = next(f)
                        line_count += 1
                        func_collector += line
                        open_brackets += line.count('(')
                        close_brackets += line.count(')')

                        if open_brackets == close_brackets:
                            return func_collector
                except StopIteration:
                    pass      
            else:
                continue

# Generate CSV to check for various purposes
def spotcheck(assn_dir, file, func, csvf):
    submission = "Path to student submissions directory"
    csv_path = dest + csvf
    timestamp = "Unix time to make sure you grab the right files"

    with open(csv_path, "w") as f:
        student_counter = 0

        writer = csv.writer(f)
        # headers = ["userid", "code", "result"] # result column for commentary
        headers = ["userid", "code"]
        writer.writerow(headers)

        students = os.listdir(submission)
        students = sorted(students, reverse = False)
        
        for student in students:
            if (re.match(pattern, student) is None):
                student_dir = f"{submission}{student}/"
                if (file in os.listdir(student_dir)):
                    student_file = student_dir + file
                    mod_time = os.path.getmtime(student_file)
                    if (mod_time > timestamp):
                        student_counter += 1
                        code = rkt_parser(student_file, func)
                        # result is the return value of calling the functions for custom restrictions
                        # row = [student, code, result]
                        row = [student, code]
                        writer.writerow(row)

        print(f"Total: {student_counter}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Spotcheck student submissions")
    parser.add_argument("args_file", type = str, help = "Arguments File")

    args = parser.parse_args()
    args_file = args.args_file

    args_file_path = dest + args_file
    arg_list = []
    with open(args_file_path, "r") as f:
        for line in f:
            arg_list.append(line.strip())

    assn_dir, file, func, csvf = arg_list
    spotcheck(assn_dir, file, func, csvf)