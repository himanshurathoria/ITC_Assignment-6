def ispangram(string):
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in alph :
        if i not in string.lower():
            return False
    return True
string = input("\nEnter a string : ")
print(ispangram(string))