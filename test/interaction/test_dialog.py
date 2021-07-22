import alloy.interaction.dialog as aig



def test_split_sentence():

    r = aig.split_sentences("Hello World")
    assert len(r) == 1
    assert r[0] == "Hello World."

    r = aig.split_sentences("Hi! My name is Sam... Who are you?")
    assert len(r) == 3
    assert r[0] == "Hi!"
    assert r[1] == "My name is Sam."
    assert r[2] == "Who are you?"

    r = aig.split_sentences("")
    assert len(r) == 0

    r = aig.split_sentences("Hi!   I am Erin")
    assert len(r) == 2
    assert r[0] == "Hi!"
    assert r[1] == "I am Erin."

    