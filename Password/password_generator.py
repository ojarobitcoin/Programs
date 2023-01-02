import random
num=str(random.randint(1000,9999))
all,password=[],""
for char in num:
    all.append(char)
    all.append(random.choice("~`!@#$%^&*()_-+={[}]|\:;<,>.?/"))
    all.append(random.choice("uSNcciihCakcjRiQrREzhiEfdYcAuGGuIYwIvwkRGhQLicPzDywG"))
random.shuffle(all)
for thing in all:
    password+=thing
print(password)