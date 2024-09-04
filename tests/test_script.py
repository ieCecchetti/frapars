from frapars.main import parse, parse_single_address

# ptvsd.enable_attach(address=('localhost', 5678))
# ptvsd.wait_for_attach()

list_addresses = [
    "Allée Combes (Des)",
    "3 Rue Industrie (De l')",
    "Route Départementale 49",
    "02210 Rozet Saint Albin",
    "Pont Romain, 12, Rue Du",
    "Chaussée (11, Rue de la )",
    "Jaures (128, Avenue Jean) et Ferdinand Buisson (42, Rue)",
    "Jacquart (50, 52 Rue) ; Lecat (50, Rue)",
    "Deguise Olivier (3, Rue)   Rd360",
    #  new cases
    "02 Juin 1940 (Rue Du)",
    "100/101, Quai de Paludate",
    "1001 Bis Avenue RÃ©publique (De La)",
    "1007 Avenue de la Mer 83140 Six-Fours-les-Plages",
    "1007 Avenue Juin 1940 (De)",  # case date
]


def test_single_cases():
    parse_single_address("3 Rue Industrie (De l')")
    parse_single_address("route JUVARDEIL (DE) 49330 CHATEAUNEUF SUR SARTHE")
    parse_single_address("Route Départementale 49")
    parse_single_address("02210 Rozet Saint Albin")
    parse_single_address("Pont Romain, 12, Rue Du")
    parse_single_address("Chaussée (11, Rue de la )")
    parse_single_address("Deguise Olivier (3, Rue)   Rd360")
    assert True


def test_multiple_cases():
    parse("Jaures (128, Avenue Jean) et Ferdinand Buisson (42, Rue)")
    parse("Jaures (128, Avenue Jean) et Ferdinand Buisson (42, Rue)")
    parse("02 Juin 1940 (Rue Du)")
    parse("1007 Avenue Juin 1940 (De)")
    parse("1001 Bis Avenue RÃ©publique (De La)")
    parse("100/101, Quai de Paludate")
    parse("1007 Avenue de la Mer 83140 Six-Fours-les-Plages")
    assert True


def test_with_list():
    for address_text in list_addresses:
        parse_single_address(address_text, True)
    assert True
