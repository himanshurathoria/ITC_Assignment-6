x = input("Enter a word : ")
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes, word is a palindrome")
else:
    print("No, word isn't a palindrome")