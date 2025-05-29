text = input("emailni kiriting>>")
start_swidth = not text.startswith('@')
endswith = text.endswith(".com") 
result = start_swidth and endswith
print(result)