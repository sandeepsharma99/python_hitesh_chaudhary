# Password trength Checker :  Check if a password is "Weak","Strong", "Medium" .Criteria: <6char(Weak), 6-10char (Medium), >10(Strong).

Password = "gsdfjgksdjfkdsbmcxztask "
print(len(Password))

if len(Password) <6:
    print("Weak Password")
elif len(Password) <= 10:
    print("Strong password")
elif len(Password) > 10:
    print("Strong Password")


