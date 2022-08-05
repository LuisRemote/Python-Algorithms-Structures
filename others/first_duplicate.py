
def firstDuplicate(array):
    set_ = set()

    for item in array:
        if item in set_:
            return item
        else:
            set_.add(item)
    return None



if __name__ == "__main__":
    array = [1, 2, 2, 3, 4, 5, 1, 3]

    print(firstDuplicate(array))
