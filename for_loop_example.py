# Check prime and print multiplication tables
# Taking user input
# text = input("Enter any string to check prime: ")
# Given text
text = "The quick brown fox jumps over the lazy dog eee."

# Converting the text to lowercase as strings are case sensitive
lower_cased_text = text.lower()

# Declaring a string that contains all vowels.
vowels = "aeiou"

# Initialization a count variable that counts vowels
count = 0

# Instantiating an empty list to store not prime elements
container = []

# Initializing a boolean for prime condition
is_prime = False

# Loop to iterate the text string
# for n in lower_cased_text:
#     if lower_cased_text == 'a' or 'e' or 'i' or 'o' or 'u':
#         count += 1
for n in text:
    if n in vowels:
        count += 1

print(count)

# Checking prime if the count is greater than 1 because 1 is not considered
# as a prime number
if count > 1:
    for i in range(2, count):
        if count % i == 0:
            is_prime = False
            container.append(i)
            print(container)
        else:
            is_prime = True
else:
    is_prime = False
    container.append(count)

print(is_prime)
# Generating multiplication tables for the given list items
print("The multiplication tables of the non-prime elements are: ")

if is_prime == False:
    for j in container:
        for k in range(1, 11):
            print("{0} x {1} = {2}".format(container[j], k, container[j] * k))
else:
    print("The number {0} is prime so no further calculations required.".format(count))
