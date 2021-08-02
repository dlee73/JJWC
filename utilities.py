def file_stringify(file):
    with open(file=file, mode='r') as contents:
        temp_list = []
        for item in contents:
            try:
                temp_list.append(str(int(item)))
            except:
                pass
        print(", ".join(temp_list))

def listify_file(file):
    output_list = []
    with open(file=file, mode="r") as contents:
        for item in contents:
            try:
                output_list.append(str(int(item)))
            except:
                continue
    return output_list

def main():
    file_stringify("MannysList.txt")
    file_stringify("sample")

if __name__ == "__main__":
    main()

