to_print = """
Now let’s say that {b} is a lawyer, and he wants to send a secret message 'hello A, from B' to {a}. 
He takes a box from his shelf, and which has a unique key ({sym_key}). He takes photograph of himself holding the message, 
and puts the message into the box with the photograph ({b_sign}). Next, he takes a box that Alice send to him ({a_public}) 
and puts the secret key into the box. Now Bob cannot open any of the boxes. He then sends the two boxes to Alice. 
Alice takes the second box, and sources the key ({a_private}) to that box. She opens this box, and it contains the key 
for the first box, and then opens it. She then reads the message, and check the photograph.
"""
a="Alice"
b="Bob"
sym_key="symmetric_key"
b_sign="bob's signature"
a_public="alice' public key"
a_private="alice' private key"
print (to_print.format(
    a=a,
    b=b,
    sym_key=sym_key,
    b_sign=b_sign,
    a_public=a_public,
    a_private=a_private
))