import functools


def autosave(method):
    """Décorateur qui sauvegarde automatiquement la base de données après l'exécution de la méthode."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Exécute la méthode décorée puis déclenche la sauvegarde de la base de données."""
        result = method(self, *args, **kwargs)
        self.database.save()
        return result
    return wrapper
