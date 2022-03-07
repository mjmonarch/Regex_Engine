# ----------------------------------------STAGE 1------------------------------------------------------
# regex, input_str = input().split('|')
# if regex == input_str or regex == '.' or not regex:
#     print("True")
# else:
#     print("False")

# ----------------------------------------STAGE 2------------------------------------------------------
def match(a, b):
    if a == '.' or a == b:
        return True
    return False


def compare(regex_, input_str_):
    if not regex_:
        return True
    if not input_str_:
        return False
    if not match(regex_[0], input_str_[0]):
        return False
    return compare(regex_[1:], input_str_[1:])


regex, input_str = input().split('|')
print(compare(regex, input_str))
