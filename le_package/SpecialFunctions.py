__author__ = 'Francois CHANEL'
__version__ = 1.0
__all__ = ['def my_special_function(x, y, z)']


from . import CommonTools

def my_special_function(x, y, z):
    """
    ça va faire des opérations ultra spéciales avec  x, y et z

    @input:
    - x : c'est x
    - y : c'est y
    - z : c'est z

    @output:
    - un truc incroyablement sophistiqué sur x, y et z
    """

    res = CommonTools.premiere_fonction(x, y, z)

    return res * res