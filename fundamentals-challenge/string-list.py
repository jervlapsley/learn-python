palindrome = input("Check if your word is a palindrome! \nEnter a word: ")
palindromeChecker = palindrome[::-1]

if palindrome == palindromeChecker:
    print(f"Your word '{palindrome}' is a palindrome!")
else:
    print("Nope, try again!")



    