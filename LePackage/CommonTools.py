__author__ = 'Francois CHANEL'
__version__ = 1.0
__all__ = [
    'premiere_fonction',
    'remove_proxy'
]

import functools

def premiere_fonction(x, y, z):
    """
    ça va faire des trucs trop bien avec x, y et z

    Parameters
    ----------
    x : float
        c'est x
    y : float
        c'est y
    z : float 
        c'est z

    Returns
    -------
    float
        renvoie x+y+z
    """

    res = x+y+z
    return res


def deuxieme_fonction(a, b):

    """

    Cette fonction est géniale.

    Parameters
    ----------
    a : float
        c'est un bon petit float
    b : int
        c'est un gentil int

    Returns
    -------
    bool
        dit si a == b

    """

    return a == b



#* decorateur plus efficace a priori
def remove_proxy(func):
    """retire le proxy

    Grave, comme je le disais ça retire le proxy

    Parameters
    ----------
    fund : fonction
        c'est la fonction à traiter !

    Returns
    -------
    fonction
        fonction altérée

    """
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # on sauvegarde les valeurs d'intérêt de os.environ pour pouvoir les restituer ensuite
        _save = dict()
        for key in ['http_proxy', 'https_proxy']:
            for casse in [lambda x:x.lower(), lambda x:x.upper()]:
                key = casse(key)
                _save.update({key:os.environ.get(key, None)})
        
        # on écrase toutes les valeurs vues comme not None:
        for key, val in _save.items():
            if val is not None:
                # del os.environ[key]
                os.environ[key] = ''

        # on exécute la fonction   
        value = func(*args, **kwargs)
        
        # On restitue les valeurs antérieures
        for key, val in _save.items():
            if val is not None:
                os.environ[key] = val

        return value
    return wrapper_decorator
