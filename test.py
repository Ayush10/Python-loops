a = input("Enter the sentence: ")
print(a)
vowel = 0
for i in a:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
            or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowel = vowel + 1
if vowel > 1:
    for count in range(2, vowel):
        if (vowel % count) == 0:
            print(vowel,"is not prime number")
            for table in range(1, 11):
                print(str(vowel) + "*" + str(table) + "=" + str(table * vowel))
            break
    else:
        print(vowel,"is a prime number")
else:
    print(vowel,"is not prime number")
    for table in range(1, 11):
        print(str(vowel) + "*" + str(table) + "=" + str(table * vowel))