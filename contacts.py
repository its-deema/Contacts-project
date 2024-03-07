import person

class Contacts(list) :

    def count_duplicates(self) -> int :
        seen = []
        duplicates = []
        for person in self:
            person_tuple = (person.name, tuple(person.numbers.items()), person.email)
            if person_tuple in seen and person_tuple not in duplicates:
                duplicates.append(person_tuple)
            elif person_tuple not in seen:
                seen.append(person_tuple)
        return len(duplicates)


        