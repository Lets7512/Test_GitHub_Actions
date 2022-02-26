import re,glob

def get_function_name():
    pattern = re.compile(r'def ([A-Za-z_]+)')
    for txt in glob.glob('*.txt'):
        print("Filename: ",txt)
        with open(txt,'r') as f:
            content = f.read()
            functions = re.findall(pattern,content)
            print("Function names: ",functions)


if __name__ == "__main__":
    get_function_name()