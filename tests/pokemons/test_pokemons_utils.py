from src.pokemons.utils import remove_empty_items


def test_remove_empty_items():
    items = remove_empty_items(['a', '', 'c', '', 'l'])

    assert items.__str__() == "['a', 'c', 'l']"
    assert items[0] == 'a'
    assert items[1] == 'c'
