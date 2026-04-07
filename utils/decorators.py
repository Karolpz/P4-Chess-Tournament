import functools


def autosave(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.database.save()
        return result
    return wrapper
