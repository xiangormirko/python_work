# List exercise 2
# Mirko (xiang@bu.edu)

def main():
    animals=["cow","sheep","pig"]
    print animals

    for animal in animals:
        print "the %s says..." % animal
    animals.append("goat")
    print animals
    animals.append("cow")
    animals.append("pig")
    print animals
    print animals.count("cow")
    print animals.count("dinosaur")

    animals.sort()
    print animals
    animals.reverse()
    print animals
    animals.remove("goat")
    print animals
main()
