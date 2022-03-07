# ----------------------------------------STAGE 1------------------------------------------------------
# regex, input_str = input().split('|')
# if regex == input_str or regex == '.' or not regex:
#     print("True")
# else:
#     print("False")

# ----------------------------------------STAGE 2------------------------------------------------------
# def match(a, b):
#     if a == '.' or a == b:
#         return True
#     return False
#
#
# def compare(regex_, input_str_):
#     if not regex_:
#         return True
#     if not input_str_:
#         return False
#     if not match(regex_[0], input_str_[0]):
#         return False
#     return compare(regex_[1:], input_str_[1:])
#
#
# regex, input_str = input().split('|')
# print(compare(regex, input_str))

# ----------------------------------------STAGE 3------------------------------------------------------
def match(a, b):
    if a == '.' or a == b:
        return True
    return False


def compare_same_length(regex_, input_str_):
    if not regex_:
        return True
    if not input_str_:
        return False
    if not match(regex_[0], input_str_[0]):
        return False
    return compare_same_length(regex_[1:], input_str_[1:])


def compare(regex_, input_str_):
    while len(input_str_) >= len(regex_):
        if compare_same_length(regex_, input_str_[0:len(regex_)]):
            return True
        else:
            return compare(regex_, input_str_[1:])
    return False


regex, input_str = input().split('|')
print(compare(regex, input_str))