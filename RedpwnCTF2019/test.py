import base64

check_string = "flag"
file_name = "tempfile.txt"
base64_string = ""

with open(file_name, "r") as in_file:
    base64_string = in_file.read()

while True:
        if "flag" not in str(base64_string):
            base64_string = base64.b64decode(base64_string)
        else:
            print(base64_string)
            break
