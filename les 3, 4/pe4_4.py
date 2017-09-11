def newPassword(oldPassword, newPassword):
    if newPassword != oldPassword:
        if len(newPassword) >= 6:
            for char in newPassword:
                if char.isdigit():
                    return True
    return False

userOldPassword = input('Geef je oude wachtwoord op: ')
userNewPassword = input('Geef je nieuwe wachtwoord op: ')
print(newPassword(userOldPassword, userNewPassword))
