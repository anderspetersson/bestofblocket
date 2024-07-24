VERSION = (1, 1, 0, 'alpha', 0)

def get_version(*args, **kwargs):
    # Don't litter django/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from bestofblocket.core.utils import get_version
    return get_version(*args, **kwargs)
