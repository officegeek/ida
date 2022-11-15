# if
a = 10
b = 20

if b > a:
    print("b er er størst")

# elif
a = 33
b = 33

if b > a:
  print("b er størrer end a")
elif a == b:
  print("a og b er ens")

# else
a = 200
b = 33

if b > a:
  print("b er størrer end a")
elif a == b:
  print("a og b er ens")
else:
  print("a er størrer end b")

# and
a = 200
b = 33
c = 500

if a > b and c > a:
  print("Begge betingelser er sande/true")

# or
if a > b or a > c:
  print("Mindst en betingelse er sand/true")

# nestede if
x = 15

if x > 10:
  print("Over 10,")
  if x > 20:
    print("også over 20")
  else:
    print("men ikke over 20")

# pass
a = 10
b = 20

if b > a:
    pass

# Loop
# while
i = 1
while i < 6:
  print(i)
  i += 1

# else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i er ikke længere mindre end 6")

# For loop
navne = ["Ole", "Per", "Ulla"]
for n in navne:
  print(n)

for x in "Hellstern":
  print(x)

# Range
for x in range(5):
  print(x)

for x in range(2, 8):
    print(x)
