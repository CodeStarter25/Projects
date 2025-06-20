from project import generate_password, password_strength_check, dashes_calculator


def test_generate_password_length():
    length_list = [-5, 0, 3, 6, 8, 9, 12, 20]
    assert len(generate_password(length_list[0])) == 8
    assert len(generate_password(length_list[1])) == 8
    assert len(generate_password(length_list[2])) == 8
    assert len(generate_password(length_list[3])) == 8
    assert len(generate_password(length_list[4])) == 8
    assert len(generate_password(length_list[5])) == 9
    assert len(generate_password(length_list[6])) == 12
    assert len(generate_password(length_list[7])) == 20


def test_password_strength_check():
    assert password_strength_check("A1") == "Weak"
    assert password_strength_check("A1B2C3") == "Weak"
    assert password_strength_check("6.4C#Ade") == "Good"
    assert password_strength_check("KZ7n%6R#io") == "Good"
    assert password_strength_check("zcR)21I%") == "Good"
    assert password_strength_check("A1B2C3D4E5F6#") == "Good"
    assert password_strength_check("4sm<~$8RlGGO") == "Strong"
    assert password_strength_check("@[,[Bs6OXIuDX2bIn#Fc") == "Strong"


def test_dashes_calculcator():
    assert dashes_calculator("Process Interrupted By User") == 24
    assert dashes_calculator("PASSWORD CREATOR") == 29
    assert dashes_calculator("GOODBYE") == 34
    assert dashes_calculator("DATA WAS NOT DELETED") == 27

    