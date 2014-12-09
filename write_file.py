def write_file(filename, content):

    file = open(filename, "w")
    file.write(content)
    #file.write("\n")
    file.close()
