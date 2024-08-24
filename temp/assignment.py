x="beej"
print(id(x)) #140388174083056

#slices as a whole and reassigns it
x=x[:]
print(id(x)) #140388174083056 [no change]

#slices and reassigns it
x=x[1:]
print(id(x)) #140388172121136 [changes]