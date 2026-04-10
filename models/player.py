import re


class Player:
    """Représente un joueur d'échecs."""

    def __init__(self, national_id, first_name, last_name, date_of_birth):
        self.national_id = self.validate_national_id(national_id)
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def to_dict(self):
        """Convertit le joueur en un dictionnaire."""
        return {
            "national_id": self.national_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un joueur à partir d'un dictionnaire."""
        return cls(
            national_id=data["national_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
        )

    def __repr__(self):
        """Retourne une représentation du joueur."""
        return f"{self.last_name} {self.first_name} ({self.national_id})"

    def __lt__(self, other):
        """Permet de comparer les joueurs pour les trier par ordre alphabétique."""
        return (self.last_name.lower(), self.first_name.lower()) < \
               (other.last_name.lower(), other.first_name.lower()
                )

    def __eq__(self, other):
        """Permet de comparer les joueurs pour vérifier s'ils sont identiques."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.national_id == other.national_id

    def __hash__(self):
        """Permet de rendre les joueurs hashables en utilisant leur identifiant national."""
        return hash(self.national_id)

    @staticmethod
    def validate_national_id(national_id):
        """Valide l'identifiant national en vérifiant qu'il correspond au format attendu."""
        pattern = r'^[A-Z]{2}\d{5}$'
        if not re.match(pattern, national_id.upper()):
            raise ValueError(f"Identifiant national invalide : {national_id}. Format attendu : AB12345")
        return national_id.upper()
