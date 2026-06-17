# Elite Team Cybersecurity Project: Basic Password Strength Checker
import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for numbers
    if not re.search(r"\d", password):
        return "Medium: Add numbers to make your password stronger."
        
    # Check for special characters
    if not re.search(r"[ !@#$%^&*(),.?\":{}|<>_]", password):
        return "Medium: Add special characters (like @, #, or $) to enhance security."
        
    return "Strong: Excellent security architecture!"

# Test the function
user_input = input("Enter a password to test its security configuration: ")
print(check_password_strength(user_input))
