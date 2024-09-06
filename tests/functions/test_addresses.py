from frapars.functions.addresses import parse

class TestAddressFunction:

    def test_special_case_1_address(self):
        address_str = "10 Avenue des Vieux Moulins (Annecy) 74000 Annecy"
        result = parse(address_str)
        print(result)
        assert result == [{
            'raw': '10 Avenue des Vieux Moulins (Annecy) 74000 Annecy', 
            'urba_names': ['avenue', 'des'], 
            'city': ['vieux moulins', 'annecy', 'annecy'], 
            'insee': [], 
            'postcode': ['74000'], 
            'codes': [], 
            'address_num': ['10'], 
            'department': [], 
            'street_name': [], 
            'formatted': '10 Avenue Des Vieux Moulins Annecy Annecy 74000'
            }
        ]
    
    def test_special_case_2_address(self):
        # everithing inside parenthesys 
        address_str = "Chaussée (11, Rue de la )"
        result = parse(address_str)
        print(result)
        assert result == [
            {
                'raw': 'Chaussée (11, Rue de la )', 
                'urba_names': ['rue', 'de la'], 
                'city': [], 
                'address_num': ['11'], 
                'department': [], 
                'street_name': ['chaussée'], 
                'formatted': '11 Rue De La Chaussée'
            }
        ]