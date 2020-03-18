__author__ = 'Francois CHANEL'
__version__ = 1.0
__all__ = ['my_special_function', 'Objet_de_ouf']


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


class Objet_de_ouf():
    """
    on va super bien décrire ce que fait la classe:

    Parameters
    ----------
    a : float
        c'est a
    b : int
        that is b

    Returns
    -------
    un sublime objet
        ça renvoie une instance de notre incroyable classe de ouf !
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



