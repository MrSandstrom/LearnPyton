def going_out(sunny, stay_in):
    if sunny == True and stay_in == False:
        return True
    else:
        return False


print(going_out(True, True))    # Sun is shining but not allowed to get out --> False
print(going_out(True, False))   # Sun is shaing but and are allowed to get out --> True
print(going_out(False, True))   # Sun do not shine --> False
print(going_out(False, False))  # Sun do not shine --> False