from frapars.helper.formatter import Formatter, AddressFields

# Test class for Formatter
class TestFormatter:
    
    def setup_method(self):
        self.formatter = Formatter()

    def test_default_format(self):
        address_info = {
            'address_num': ['50'],
            'urba_names': ['Rue'],
            'street_name': ['Jacquart'],
            'city': ['Paris'],
            'postcode': ['75001'],
            'insee': ['75101'],
            'codes': ['ABC123'],
            'department': ['75']
        }
        formatted = self.formatter.format(address_info)
        expected = '50 Rue Jacquart Paris 75001 75101 Abc123 75'
        assert formatted == expected
    
    def test_custom_format(self):
        custom_format = f"{AddressFields.ADDRESS_NUM.value} - {AddressFields.CITY.value} - {AddressFields.POSTCODE.value}"
        self.formatter = Formatter(template=custom_format)
        address_info = {
            'address_num': ['50'],
            'city': ['Paris'],
            'postcode': ['75001']
        }
        formatted = self.formatter.format(address_info)
        expected = '50 - Paris - 75001'
        assert formatted == expected
    
    def test_multiple_addresses(self):
        address_info1 = {
            'address_num': ['50'],
            'urba_names': ['Rue'],
            'street_name': ['Jacquart'],
            'city': ['Paris'],
            'postcode': ['75001'],
            'insee': ['75101'],
            'codes': ['ABC123'],
            'department': ['75']
        }
        address_info2 = {
            'address_num': ['128'],
            'urba_names': ['Avenue'],
            'street_name': ['Jean Jaures'],
            'city': ['Paris'],
            'postcode': ['75012'],
            'insee': ['75102'],
            'codes': ['XYZ789'],
            'department': ['75']
        }
        formatted = self.formatter.format_all([address_info1, address_info2], sep='et')
        expected = '50 Rue Jacquart Paris 75001 75101 Abc123 75 et 128 Avenue Jean Jaures Paris 75012 75102 Xyz789 75'
        assert formatted == expected
    
    def test_extra_spaces(self):
        address_info = {
            'address_num': ['50 '],
            'urba_names': [' Rue '],
            'street_name': [' Jacquart '],
            'city': [' Paris '],
            'postcode': [' 75001 '],
            'insee': [' 75101 '],
            'codes': [' ABC123 '],
            'department': [' 75 ']
        }
        formatted = self.formatter.format(address_info)
        expected = '50 Rue Jacquart Paris 75001 75101 Abc123 75'
        assert formatted == expected
    
    def test_capitalization(self):
        address_info = {
            'address_num': ['50'],
            'urba_names': ['rue'],
            'street_name': ['jacquart'],
            'city': ['paris'],
            'postcode': ['75001'],
            'insee': ['75101'],
            'codes': ['abc123'],
            'department': ['75']
        }
        formatted = self.formatter.format(address_info)
        expected = '50 Rue Jacquart Paris 75001 75101 Abc123 75'
        assert formatted == expected

    def test_invalid_keys(self):
        address_info = {
            'invalid_key': 'value'
        }
        formatted = self.formatter.format(address_info)
        expected = ''
        assert formatted == expected

    def test_empty_keys(self):
        address_info = {}
        formatted = self.formatter.format(address_info)
        expected = ''
        assert formatted == expected