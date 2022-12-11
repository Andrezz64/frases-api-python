
def getData(position):
    with open("LocalStorege.txt", "r", encoding="utf8") as f:
        local = f.readlines()


    local = [x.rstrip('\n') for x in local]
    return local[position]

