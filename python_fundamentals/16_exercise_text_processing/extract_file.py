text_input = input().split("\\")
file_name = text_input[-1].split(".")
print(f'''File name: {file_name[0]}
File extension: {file_name[1]}''')
