#file  -- interface.py --
def clear_window():
    return(250*"\n")

def name():
    while True:
        name = input("Wat is je naam?")
        if name == "":
            print("Je hebt geen naam opgegeven!")
            continue
        else:
            return name


