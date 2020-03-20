__author__ = 'Francois CHANEL'
__version__ = 1.0
__all__ = [
    'my_special_function', 
    'google_style_docstring',
    'test_fonction_avec_decorateur',
    '_my_private_parts',
    'Objet_de_ouf',
    'Foo',
    ]


from . import CommonTools
from .CommonTools import remove_proxy
from .CommonTools import premiere_fonction

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


def google_style_docstring(gimme_your_int, your_diviseur):
    """fonction test pour la doc google_style

    On peut donc aisément constater avec cet exemple que la docString googleStyle est hideuse...

    Args:
        gimme_your_int (int): on va diviser ce petit con 
        your_diviseur (int): on va diviser avec ce petit machin !

    Returns:
        mon_rest (int): t'as qu'à bouffer mes restes !

    """

    return gimme_your_int % your_diviseur


@remove_proxy
def test_fonction_avec_decorateur(x, y):
    """
    ça va faire des opérations ultra spéciales avec  x, y et z

    Parameters
    ----------
    x : float
        c'est x
    y : float
        oh le joli petit y !


    Returns
    -------
    bool
        test un truc de ouf si x == 2 * y
    """

    return x == 2*y


def _my_private_parts(x, y):
    """
    pour voir l'effet du tiret sur une fonction hors classe

    Parameters
    ----------
    x : float
        c'est x
    y : float
        oh le joli petit y !


    Returns
    -------
    float
        returns x+y
    """

    return x + y


class Objet_de_ouf():
    """
    We are Borg !
    """

    def __init__(self, a, b):
        """
        Ici on décrit ce que fait l'init

        Parameters
        ----------
        a : float
            nous somme dans __init__, et c'est ici qu'on décrit a
        b : int
            nous somme dans __init__, et c'est ici qu'on décrit b

        Returns
        -------
        un sublime objet
            on est dans le __init__, et ça renvoie une instance de notre incroyable classe de ouf !
        """
        self.a = a
        self.b = b
    

    def show_me_your_attributes(self):
        """
        cette fonction sert à voir les attributs de la classe

        Parameters
        ----------
        self

        Returns
        -------
        None
        """

        for key, val in self.__dict__.items():
            print(f'{key:<5} : {val}')
    

    def __repr__(self):
        """
        ici on est supposés écrire la docstring de __repr__ mais comme c'est une fonction
        cachée elle n'apparaîtra pas !

        Parameters
        ----------
        self

        Returns
        -------
        string
            la string de repr de l'objet
        """
        my_string_repr = ''
        for key, val in self.__dict__.items():
            my_string_repr += f'{key:<5} : {val}'
        return my_string_repr
    

    def fais_de_la_merde_avec_les_attributs(self):
        """
        toy_fonction idiote juste pour en avoir une deuxième sous le coude

        Parameters
        ----------
        self

        Returns
        -------
        string
            renvoie une string mélangeant attributs et valeurs
        """
        res_key = ''
        res_val = 0
        for key, val in self.__dict__.items():
            res_key += key
            res_val += val
        
        my_res = f'{res_key} -- {res_val}'
        return my_res


    def modif_dynamique(self, other_arg):
        """pour voir si on peut ajouter sans refaire sphinx-apidoc

        On refit de la merde juste pour vérifier

        Parameters
        ----------
        other_arg : int
            c'est un super paramètre

        Returns
        -------
        bool
            check si un arg de __dict__ est égal à other_arg
        """

        res = False
        
        for val in self.__dict__.values():
            if val == other_arg:
                res = True

        return res

    
    def _pour_voir_effet_underscore_simple():
        """
        # RIEN ! Makache
        """

        return None


class Foo:
    """Docstring for class Foo."""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""

    def __init__(self, qux, spam):
        """
        Bonjour, je suis le __init__ de Foo !
        """
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""
        
        #: Doc comment pour thing ??
        self.thing = qux + spam