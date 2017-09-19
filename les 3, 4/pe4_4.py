def newPassword(oldPassword, newPassword):
    containsDigit = False
    for char in newPassword:
        if char.isdigit():
            containsDigit = True
    if newPassword == oldPassword:
        return False
    elif len(newPassword) >= 6:
        return False
    elif containsDigit == False:
        return False

    return True


userOldPassword = input('Geef je oude wachtwoord op: ')
userNewPassword = input('Geef je nieuwe wachtwoord op: ')
print(newPassword(userOldPassword, userNewPassword))
