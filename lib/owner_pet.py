class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self  # Set the owner attribute of the pet
            self._pets.append(pet)
        else:
            raise ValueError("Can only add instances of Pet")

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)



class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if owner:
            owner.add_pet(self)
