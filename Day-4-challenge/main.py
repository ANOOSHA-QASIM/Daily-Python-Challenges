print("=" * 60)
print(" DAY 4 - Number to Words Converter Challenge ".center(60, "-"))
print("=" * 60)


from num2words import num2words

num = int(input("Enter a number: "))

words = num2words(num).title()

print(f"Nnumber in words: {words}")

print("=" * 60)
print(" DAY 4 - Currency Amount to Words Converter Challenge ".center(60, "-"))
print("=" * 60)


amount_str = input("Enter a number: ")

if "." in amount_str:
    rupees_sec , paisa_sec = amount_str.split(".")
else:
    rupees_sec = amount_str
    paisa_sec = "0"

paisa_sec = paisa_sec[:2].ljust(2, '0')

rupees = int(rupees_sec)
paisa = int(paisa_sec)

rupees_in_words = num2words(rupees).title()

paisa_in_words = num2words(paisa).title()


result = (f"{rupees_in_words} Rupees And {paisa_in_words} Paisa")

print(f"Currency in words: {result}")

print("=" * 60)
print("END OF CHALLENGE".center(60, "-"))
print("=" * 60)




