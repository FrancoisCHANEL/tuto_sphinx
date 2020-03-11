__author__ = 'Francois CHANEL'
__version__ = 1.0
__all__ = ['my_special_function']


from . import CommonTools

def my_special_function(x, y, z):
    """
    ça va faire des opérations ultra spéciales avec  x, y et z

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
        renvoie un machin incroyablement complexe à partir de x, y et z
    """

    res = CommonTools.premiere_fonction(x, y, z)

    return res * res