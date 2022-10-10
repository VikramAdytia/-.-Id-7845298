elements1 = ["xxxxxx", "yyy", "z", "22", "xy"]


def elements_shorter_4_in_list(elements):

    element_shorter_4 = []

    for element in elements:
        if len(element) < 4:
            element_shorter_4.append(element)

    print(element_shorter_4)


elements_shorter_4_in_list(elements1)
