username=input("what is your username: ")
password=input("what is your password: ")
Pass_length=len(password)
hidden_password='*'*Pass_length
print(f"{username},your password,{hidden_password},is{Pass_length}letters long")
