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
# def match(a, b):
#     if a == '.' or a == b:
#         return True
#     return False
#
#
# def compare_same_length(regex_, input_str_):
#     if not regex_:
#         return True
#     if not input_str_:
#         return False
#     if not match(regex_[0], input_str_[0]):
#         return False
#     return compare_same_length(regex_[1:], input_str_[1:])
#
#
# def compare(regex_, input_str_):
#     while len(input_str_) >= len(regex_):
#         if compare_same_length(regex_, input_str_[0:len(regex_)]):
#             return True
#         else:
#             return compare(regex_, input_str_[1:])
#     return False
#
#
# regex, input_str = input().split('|')
# print(compare(regex, input_str))

# ----------------------------------------STAGE 4------------------------------------------------------
# def match(a, b):
#     if a == '.' or a == b:
#         return True
#     return False
#
#
# def compare_same_length(regex_, input_str_):
#     if not regex_:
#         return True
#     if not input_str_:
#         return False
#     if not match(regex_[0], input_str_[0]):
#         return False
#     return compare_same_length(regex_[1:], input_str_[1:])
#
#
# def compare_simple(regex_, input_str_):
#     while len(input_str_) >= len(regex_):
#         if compare_same_length(regex_, input_str_[0:len(regex_)]):
#             return True
#         else:
#             return compare_simple(regex_, input_str_[1:])
#     return False
#
#
# def compare_complex(regex_, input_str_):
#     if not regex_:
#         return True
#     if regex_[0] == '^':
#         if regex_[-1] == '$':
#             if len(input_str_) != len(regex_) - 2:
#                 return False
#             else:
#                 return compare_same_length(regex_[1:len(regex_) - 1], input_str_)
#         else:
#             if len(input_str_) < len(regex_) - 1:
#                 return False
#             else:
#                 return compare_same_length(regex_[1:], input_str_[:len(regex_)])
#     elif regex_[-1] == '$':
#         if len(input_str_) < len(regex_) - 1:
#             return False
#         else:
#             return compare_same_length(regex_[:len(regex_) - 1],
#                                        input_str_[len(input_str_) - (len(regex_) - 1):])
#     else:
#         return compare_simple(regex_, input_str_)
#
#
# if __name__ == '__main__':
#     regex, input_str = input().split('|')
#     print(compare_complex(regex, input_str))

# ----------------------------------------STAGE 5------------------------------------------------------
METACHARACTERS = ['?', '*', '+', '$']


def match(a, b):
    if a == '.' or a == b:
        return True
    return False


def compare(regex_, input_str_, i, j, iterate):
    # check for an empty regex
    if len(regex_) == 0:
        return True

    # check corner case for '^'
    if i == 0 and regex_[i] == '^':
        return compare(regex_, input_str_, i + 1, j, False)

    # check if regex is over
    if i >= len(regex_):
        return True

    # check if input string is over
    if j >= len(input_str_):
        return False

    # check if regex is about to finish (next item in regex doesn't exist)
    if i + 1 == len(regex_):
        if match(regex_[i], input_str_[j]):
            return True
        if regex_[i] == '$':
            if j == len(input_str_) - 1:
                return True
            else:
                return False
        if not iterate:
            return False
        return compare(regex_, input_str_, 0, j + 1, True)

    # check if regex is not about to finish (next item in regex exist)
    else:
        # check if i-element in regex is ordinal character
        if regex_[i + 1] not in METACHARACTERS:
            if match(regex_[i], input_str_[j]):
                return compare(regex_, input_str_, i + 1, j + 1, iterate)
            else:
                if iterate:
                    return compare(regex_, input_str_, 0, j + 1, True)
                else:
                    return False
        # check if (i + 1)-element in regex is '?'
        elif regex_[i + 1] == '?':
            if match(regex_[i], input_str_[j]):
                return compare(regex_, input_str_, i + 2, j + 1, iterate)
            else:
                return compare(regex_, input_str_, i + 2, j, iterate)
        # check if (i + 1)-element in regex is '*'
        elif regex_[i + 1] == '*':
            if match(regex_[i], input_str_[j]):
                try:
                    while match(regex_[i], input_str_[j + 1]):
                        # check if current symbol in input string matches the element after * in the regex
                        if i + 2 <= len(regex_) - 1 and match(regex_[i + 2], input_str_[j + 1]):
                            break
                        j += 1
                except IndexError:
                    if i >= len(regex_) - 3 and j >= len(input_str_) - 1:
                        return True
                    else:
                        return False
                return compare(regex_, input_str_, i + 2, j + 1, iterate)
            else:
                return compare(regex_, input_str_, i + 2, j, iterate)
        # check if (i + 1)-element in regex is '+'
        elif regex_[i + 1] == '+':
            if match(regex_[i], input_str_[j]):
                try:
                    while match(regex_[i], input_str_[j + 1]):
                        # check if current symbol in input string matches the element after * in the regex
                        if i + 2 <= len(regex_) - 1 and match(regex_[i + 2], input_str_[j + 1]):
                            break
                        j += 1
                except IndexError:
                    if i >= len(regex_) - 3 and j >= len(input_str_) - 1:
                        return True
                    else:
                        return False
                return compare(regex_, input_str_, i + 2, j + 1, iterate)
            else:
                if iterate:
                    return compare(regex_, input_str_, 0, j, True)
                else:
                    return False
        # check if (i + 1)-element in regex is '$'
        elif regex_[i + 1] == '$':
            if match(regex_[i], input_str_[j]) and j == len(input_str_) - 1:
                return True
            else:
                return compare(regex_, input_str_, 0, j + 1, iterate)


if __name__ == '__main__':
    regex, input_str = input().split('|')
    print(compare(regex, input_str, 0, 0, True))
