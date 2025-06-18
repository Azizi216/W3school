import re

# 1. Email Extractor from Text
text = "Contact us at info@example.com or support@mydomain.org and admin@abc.net"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|net)\b'
emails = re.findall(email_pattern, text)
print("Emails:", emails)

# 2. Log File Cleaner: Extract IP and Timestamp
log = '123.45.67.89 - - [10/Oct/2022:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 2326'
log_pattern = r'(\d{1,3}(?:\.\d{1,3}){3})\s.*\[(.*?)\]'
log_matches = re.findall(log_pattern, log)
print("IP and Timestamp:", log_matches)

# 3. Validate Passwords with Regex
password = "StrongPass1"
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
is_valid_password = bool(re.fullmatch(password_pattern, password))
print("Is valid password?", is_valid_password)

# 4. Twitter Hashtag Extractor
tweet = "Loving the new #Python3.11 update! #💻 #Code_Newbie"
hashtag_pattern = r'#\w[\w\ufe0f\u200d]*'
hashtags = re.findall(hashtag_pattern, tweet)
print("Hashtags:", hashtags)

# 5. Phone Number Normalizer
phones = "Call us at +7 701 123 4567 or 87011234567 or 7-701-123-45-67."
phone_pattern = r'(?:\+?7|8)[\s-]?(\d{3})[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})'
phone_matches = re.findall(phone_pattern, phones)
normalized_phones = [f'+7 ({a}) {b}-{c}-{d}' for a, b, c, d in phone_matches]
print("Normalized Phones:", normalized_phones)

