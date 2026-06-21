password = input("Enter your password: ")
length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_symbol = False
has_repeats = False

symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

common_passwords = ["password", "123456", "password123", "qwerty", "abc123", "letmein", "admin", "welcome"]

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if char in symbols:
        has_symbol = True

# Check for repeated characters after processing all individual characters
for i in range(len(password) - 2):
    if password[i] == password[i+1] == password[i+2]:
        has_repeats = True
        break # No need to check further if repeats are found

print("Password length:", length)
print("Has uppercase:", has_upper)
print("Has lowercase:", has_lower)
print("Has digit:", has_digit)
print("Has symbol:", has_symbol)
print("Has repeated characters:", has_repeats)

is_common = password.lower() in common_passwords

score = 0
if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1
if not has_repeats:
    score += 1

print("")

if is_common:
    print("DANGER: This is a commonly used, easily hacked password!")
elif score == 6:
    print("STRONG password!")
elif score >= 4:
    print("MODERATE password - could be better")
else:
    print("WEAK password - improve it!")
