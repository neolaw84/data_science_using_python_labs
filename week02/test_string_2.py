
def test_string_2(capsys):
    import lab_string_2 as ls2
    captured = capsys.readouterr()
    output = captured.out
    output = output.strip()
    output = output.replace("\n", " ")
    output = output.replace("  ", " ")
    output = output.replace("  ", " ").replace("  ", " ") 
    to_check = """Now let’s say that Bob is a lawyer, and he wants to send a secret message
'hello A, from B' to Alice. He takes a box from his shelf, and which has a 
unique key (symmetric_key). He takes photograph of himself holding the message, 
and puts the message into the box with the photograph (bob's signature). Next, 
he takes a box that Alice send to him (alice' public key) and puts the secret 
key into the box. Now Bob cannot open any of the boxes. He then sends the two 
boxes to Alice. Alice takes the second box, and sources the key (alice' private key) 
to that box. She opens this box, and it contains the key for the first box, and then 
opens it. She then reads the message, and check the photograph.""" \
    .strip().replace("\n", " ") \
    .replace("  ", " ").replace("  ", " ") \
    .replace("  ", " ").replace("  ", " ")
    print (to_check)
    print (output)
    assert to_check == output
    assert ls2.a=="Alice"
    assert ls2.b=="Bob"
    assert ls2.sym_key=="symmetric_key"
    assert ls2.b_sign=="bob's signature"
    assert ls2.a_public=="alice' public key"
    assert ls2.a_private=="alice' private key"
    with open("lab_string_2.py", "rt") as f:
        program = f.read()
        program = program\
        .strip().replace("\n", " ") \
        .replace("  ", " ").replace("  ", " ") \
        .replace("  ", " ").replace("  ", " ")
        assert to_check not in program