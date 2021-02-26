def sleep_in(weekday, vacation):
    if (not weekday and not vacation) or (not weekday and vacation) or (weekday and vacation):
        return True
    else:
        return False

print(sleep_in(False,True))