def display_name(name):
 print("Hello, " + name)
def count_vowels(name):
 vowels = "aeiouAEIOU"
 count = 0# set count to zero
 for char in name:#uses the in operater to check if the character is a vowel
 if char in vowels:
 count += 1 # increment count by 1
 print (count)
#count is incremented by 1 everytime a vowel is found in the name because of the for loop
def display_charsleft(name, n):
 left_chars = name[:n]#slices to the left of n
 print ("Characters from left:", left_chars)
def reverse_name(name):
 reverse = name[::-1]#reverses the name
 #^ sets the value of reverse to the reverse of name.
 print(reverse)#prints the reversed name
def main(name, n):
 # calls all the functions down
 display_name(name)
 display_charsleft(name, n)
 count_vowels(name)
 reverse_name(name)
 #passes arguments to the functions.

main(input('what is your name? '),int(input('how many characters from the left')))
