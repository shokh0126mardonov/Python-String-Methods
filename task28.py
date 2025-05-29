text = input("Izoh matnini kiriting: ")
lower_text = text.lower()
has_bad = "bad" in lower_text
replace_text = lower_text.replace("bad", "")
print(has_bad,replace_text)
