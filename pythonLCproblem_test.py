from pythonLCproblem import canConstruct

def test_can_construct():
    assert canConstruct("a", "abcdefg") == True
    assert canConstruct("abc", "abcdefg") == True
    assert canConstruct("hello", "world") == False