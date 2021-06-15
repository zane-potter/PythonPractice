# Checks for password input against stored password
# Password is stored in plaintext, not secure

master_password = "Password"

pass_attempt = input("What is your password?")

if (pass_attempt == master_password):
    print("Access Granted")
else:
    print("Access Denied")
