
def check_password(password):
    score = 0

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:,.?/"

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    for character in password:
        if character.islower():
            has_lowercase = True
        elif character.isupper():
            has_uppercase = True
        elif character.isdigit():
            has_digit = True
        elif character in special_characters:
            has_special = True

    if has_lowercase:
        score += 1
    if has_uppercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    print("\n===== PASSWORD ANALYSIS =====")
    print("Length requirement:", "Passed" if len(password) >= 8 else "Not met")
    print("Lowercase letters:", "Yes" if has_lowercase else "No")
    print("Uppercase letters:", "Yes" if has_uppercase else "No")
    print("Digits:", "Yes" if has_digit else "No")
    print("Special characters:", "Yes" if has_special else "No")

    print("Strength score:", score, "/ 6")

    if score <= 2:
        print("Strength: Weak")
    elif score <= 4:
        print("Strength: Moderate")
    else:
        print("Strength: Strong")


print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter a sample password to analyze: ")

if password == "":
    print("Password cannot be empty.")
else:
    check_password(password)
  
