username = input("Usernameni kiriting: ")

replace = username.replace("-", "")

# Tekshiruv: faqat harflar va raqamlar bo‘lishi kerak
is_alnum = replace.isalnum()

print(is_alnum)
