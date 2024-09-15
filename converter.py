def convert(input):

    src_text = input
    if "/" in src_text:
        changed_text = src_text.replace("/", "\\")
        
    elif "\\" in src_text:
        changed_text = src_text.replace("\\", "/")

    else:
        print("no slashes in textfile")

    return changed_text