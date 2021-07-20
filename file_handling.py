from pathlib import Path



# Version 1: Simple -> Usage: discouraged
# - Files might stay open if program crashes before *.close() lines
# - We do not know if the files exists or could get an error
def version1():
    in_file = open("ip_list.txt", "r")
    in_data = in_file.read()

    user_input = input("Content to write to file: ") 

    out_file = open("new_ip_list", "w")
    out_file.write(in_data + user_input)

    in_file.close()
    out_file.close()


# Version 2: A bit more advanced -> Usage: Good/OK
# - Even if program crashes files will be closed because of with block
# - We do not know if the files exists or could get an error
def version2():
    with open("ip_list.txt", "r") as in_file, open("new_ip_list", "w") as out_file:
        user_input = input("Content to write to file: ")
        out_file.write(in_file.read() + user_input)


# Version 3: Advanced -> Usage: Encouraged
# Pathlib is taking care of file handling, with blocks etc. and
# is also able to check file path if it exists/for it's type
def version3():
    in_file = Path("ip_list.txt")
    if in_file.exists() and in_file.is_file():
        out_file = Path("new_ip_list.txt")
        if not out_file.exists():
            user_input = input("Content to write to file: ")
            out_file.write_text(in_file.read_text + user_input)


# Just to for fun to keep version3 a bit shorter and to show new python features
# Requires Python3.8.2+
def version3_extra():
    # ( variable := object ) to assign a variable only if the with block
    # evaluates to True
    if (in_file := Path("ip_list.txt")).exists() and in_file.is_file():
        if not (out_file := Path("new_ip_list.txt")).exists():
            user_input = input("Content to write to file: ")
            out_file.write_text(in_file.read_text() + user_input)



if __name__ == "__main__":
    version3()