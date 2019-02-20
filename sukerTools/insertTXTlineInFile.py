with open("40-libinput.conf", 'r+') as f:
    contents = f.readlines()
    for index, line in enumerate(contents):
        if "Identifier" in line and "touchscreen" in line and "TransformationMatrix" not in contents[index + 1] :
            contents.insert(index + 1, '\tOption "TransformationMatrix" "1 0 0 0 -1 1 0 0 1"\n')
            break
    f.seek(0)
    f.writelines(contents)
