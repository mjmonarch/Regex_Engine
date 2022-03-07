# ----------------------------------------STAGE 1------------------------------------------------------
regex, input_str = input().split('|')
if regex == input_str or regex == '.' or not regex:
    print("True")
else:
    print("False")
