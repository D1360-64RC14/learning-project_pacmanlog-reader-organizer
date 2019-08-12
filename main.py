log = open('example/pacman.log', 'r').read()
import json
import Organize

""" (Work In Progress)
log = Organize.log2list(log)
print('\n [A]ll, [I]nstalled, [U]pgraded, [R]emoved')
user = {
    "option": str,
    "quantity": int(100),
    "date": str
}
user["option"] = input('(A|I|U|R) > ')

print('\n Quantity of itens (optional)')
tmp = input('(Default: 100) > ')
user["quantity"] = int(tmp) if 

print('\n Date of the itens (optional)')
user["date"] = input('(day/month/year) > ')

print(user)"""

open('example/file.json', 'w').write( json.dumps(Organize.log2json(log), indent="\t") )
