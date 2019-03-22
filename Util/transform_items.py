def lst_str_int(string, seperator):
    """
    Initialize network tables
    :parameter string and seperator
    :return list of ints
    """
    lst_strs = string.split("-")
    lst_ints = []
    for num in lst_strs:
        integer_form = int(num)
        lst_ints.append(integer_form)
    return lst_ints
