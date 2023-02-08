ANIMALS = ["ocelot", "octopus", "opossum", "orangutan", "orca", "oriole", "oryx", "osprey"];

def has_animal(species):
    """O(n) Linear algorithm -- worst case is every element is checked.
    """
    for a in ANIMALS:
        if species == a:
            return True
    return False

def animal_pairs():
    """Quadratic O(n^2) Complexity -- """
    pairs = []
    for a in ANIMALS:
        for b in ANIMALS:
            pairs.append((a, b))
    return pairs

def main():
    import timeit
    print(timeit.timeit('animal_pairs()'))

if __name__ == "__main__":
    main()
