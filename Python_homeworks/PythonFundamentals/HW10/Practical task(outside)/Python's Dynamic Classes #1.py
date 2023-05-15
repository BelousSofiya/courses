def class_name_changer(cls,new_name):
    import re
    word = re.findall(r'[A-Z]+[a-zA-z0-9]*', new_name)
    if len(word) == 1 and word[0] == new_name:
        cls.__name__ = new_name
    else:
        raise Exception("Exception")


