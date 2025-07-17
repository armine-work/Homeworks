# Use the re.findall() function to extract the following:
# All email addresses
# All phone numbers
# All dates
# All capitalized words
# For each task, print the result and write a comment describing the pattern you used.
import re
text = """
Hello! My name is Yana Gabrielyan. You can contact me at ygabrielyan2000@gmail.com or yana.gabrielyan@ysu.am.

My phone numbers are:
+374-91-123456
(010) 456-789
+1 (555) 987-6543

Here are some dates:
15/07/2025
2025-07-11
05.06.24

A few other names: Aram, Mariam, Davit, Emma, and their teacher Mrs. Sargsyan.

The class email is: python_course2025@gmail.com
"""

pattern = r"\w+\.?\w+\d?@\w+\.\w{2,3}"
# select a word which starts with one or more letters and has special character . and one or more letters after and can have digit
# then has character @ and one or more letters and special character . and 2 or 3 letters after
email_results = re.findall(pattern, text)
print(f"All email addresses are: ", email_results)

pattern_1 = r"\+\d{3}-\d{2}-\d+"
#select a word which starts with special character + and has 3 digits and has character - and has 2 digits
# and has character - and has one or more digits
pattern_2 = r"(?<!\+1\s)\(\d{3}\)\s\d{3}\-\d{3}"
#select a word which doesn't starts with +1 and space , has special character ( and 3 digits and special character )
# and has one space and 3 digits and - and 3 digits
pattern_3 = r"\+\d\s\(\d{3}\)\s\d{3}-\d{4}"
#select a word which starts with special character + and has 1 digit and has 1 space
# and has special character ( and 3 digits and special character ) and 1 space and 3 digits and  character - and  4 digits
phone_result_1= re.findall(pattern_1, text)
##print(f"First phone number is: ", phone_result_1)
phone_result_2 = re.findall(pattern_2, text)
##print(f"Second phone number is: ", phone_result_2)
phone_result_3 = re.findall(pattern_3, text)
##print(f"Third phone number is: ", phone_result_3)

phone_results = phone_result_1 + phone_result_2 + phone_result_3
print(f"All phone numbers are: {phone_results}")

# from ChatGPT
# pattern = r"(?:\+?\d{1,3}[-\s]?)?(?:\(\d{2,4}\)|\d{2,4})[-\s]?\d{3}[-\s]?\d{3,4}"
# result_all_phones = re.findall(pattern, text)
# print(f"All phone numbers are: {result_all_phones}")

pattern_1_1 = r"\d{2}\/\d{2}\/\d{4}"
#select a text which starts with 2 digits, has special character / , has 2 digits after, has special character / and has more 4 digits after
pattern_1_2 = r"\d{4}-\d{2}-\d{2}"
#select a text which starts with 4 digits, has character - and has 2 digits after, has character - and has more 2 digits after
pattern_1_3 = r"\d{2}\.\d{2}\.\d{2}"
#select a text which starts with 2 digits, has special character . and has 2 digit after, has special character . and has more 2 digits after
results_dates_1 = re.findall(pattern_1_1, text)
results_dates_2 = re.findall(pattern_1_2, text)
results_dates_3 = re.findall(pattern_1_3, text)
results_dates = results_dates_1 + results_dates_2 + results_dates_3
print(f"All dates are: {results_dates}")

# from ChatGPT
#pattern = r"\b\d{1,4}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}\b"
#results_dates = re.findall(pattern, text)
#print(f"All dates are: {results_dates}")

pattern = r"[A-Z]\w+"
# select words which starts only with capital letters [A-Z] and has 1 or more letters
results_capital_words = re.findall(pattern, text)
print(f"All capitalized words are: {results_capital_words}")