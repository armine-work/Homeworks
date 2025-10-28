# տնային 1՝ տրված ստրինգում գտնել 12-րդ դարից մինչև 18-րդ դարի բոլոր տարեթվերը։
# լուծել rexeg-ով ու python-ով

import re
# text = str(input("Enter any strings with digits: "))

text = "990, 1100,1101. )1200-1300) 1399! 1800, 1374_1453, {1555--1820}; 1660:1789, 1801? ((1100-1799 1100th 1500s 1222 1333's "
pattern = r"1[1-7]\d{2}"
years = re.findall(pattern, text)
print(f"\nFound years via regex:", years)

############################################################ for loop
# Remove punctuation that may be stuck to numbers
for character in ",.;:/'?!-_><()[]|}{sth":
    text = text.replace(character, " ")

# Split long text into words
words = text.split()

years = []

for word in words:
    if word.isdigit() and len(word) == 4:
        year = int(word)
        if 1100 <= year <= 1799:
            years.append(word)

print("\nFound years for_loop: ", years)

################################################## homework 2 #########################################
# տնային 2՝ տրված ա ստրինգ , պետք ա իրա sorted ֆունկցիայի միջոցով սորտավորել՝ ու տպել սորտեդ ստրինգ

new_text = "In 1134, the king built a fortress. By 1492, explorers reached new lands."
print(f"original text: {new_text}")
# if you need, you can remove punctuation marks from the text
for character in ",.;:/'?!-_><()[]|}{":
    new_text = new_text.replace(character, " ")

spilt_words = new_text.split()

sort_words = sorted(spilt_words)

join_words = " ".join(sort_words)

print(f"sorted string: {join_words} ")
