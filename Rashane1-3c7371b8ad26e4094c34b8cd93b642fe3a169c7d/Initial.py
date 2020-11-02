import sys

initials = ""
for name in sys.argv[1:]:
    initials += name[0].upper()
print (initials)
