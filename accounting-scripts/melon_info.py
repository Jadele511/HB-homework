"""Print out all the melons in our inventory."""


from melons import melons_dict

def print_melon(melons_dict):
    """Print each melon with corresponding attribute information."""

    for melon, attrs in melons_dict.items():
        print(f'{melon.upper()}')
        for attr, val in attrs.items():
            print(f'{attr} {val}')

print_melon(melons_dict)