import re

class RegisterNumber:
    colg_code = ""
    colg_name = ""
    year_of_joining = ""
    course_code = ""
    course_name = ""
    roll_no = ""

    def __init__(self, registernumber):
        reg_no_pattern = re.compile(r"([\d]{4})([\d]{2})([\d]{3})([\d]{3})")
        reg_no_matcher = re.search(reg_no_pattern, registernumber)
        self.colg_code = reg_no_matcher.group(1)
        self.colg_name = self.get_colg_name()
        self.year_of_joining = "20" + reg_no_matcher.group(2)
        self.course_code = reg_no_matcher.group(3)
        self.course_name = self.get_couse_name()
        self.roll_no = reg_no_matcher.group(4)

    def print_student_details(self):
        print(self.colg_code)
        print(self.colg_name)
        print(self.year_of_joining)
        print(self.course_code)
        print(self.course_name)
        print(self.roll_no)

    def get_colg_name(self):
        with open("colg_list.txt", mode="r") as colg_list_file:
            colg_list = colg_list_file.read().split("\n")
            for i in colg_list:
                if(self.colg_code in i):
                    return (i.split(",")[2])
            else:
                return None

    def get_couse_name(self):
        with open("course_list.txt", mode="r") as course_list_file:
            course_list = course_list_file.read().split("\n")
            for i in course_list:
                if(self.course_code in i):
                    return (i.split(",")[1])
            else:
                return None
