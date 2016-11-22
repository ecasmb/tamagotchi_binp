#file  -- interface.py --
def clear_window():
    return(250*"\n")

def printer(type, boo):
    if type is 1:
        return "boo"
    if type is 2:
        return boo

def name():
    while True:
        name = input("Wat is je naam?")
        if name == "":
            print("Je hebt geen naam opgegeven!")
            continue
        else:
            return name