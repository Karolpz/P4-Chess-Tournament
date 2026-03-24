import re

class Player:
    def __init__(self, national_id, first_name, last_name, date_of_birth):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"{self.last_name} {self.first_name} ({self.national_id})"

    def __lt__(self, other):
        return (self.last_name.lower(), self.first_name.lower()) < \
               (other.last_name.lower(), other.first_name.lower()) # Permet de comparer les joueurs pour ensuite les trier par ordre alphabétique

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.national_id == other.national_id
    
    def __hash__(self):
        return hash(self.national_id)
    
    def validate_national_id(national_id):
        pattern = r'^[A-Z]{2}\d{5}$'
        if not re.match(pattern, national_id.upper()):
            raise ValueError(f"Identifiant national invalide : {national_id}. Format attendu : AB12345")
        return national_id.upper()