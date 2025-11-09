from Language_data import country_code, country_language_data, end

def test_country_code():
    assert country_code("india") == 'IN'

def test_country_language_data():
    assert country_language_data("IN") == ["English", 'Hindi', 'Tamil']

def test_end():
    assert end() == "Program Ended"

