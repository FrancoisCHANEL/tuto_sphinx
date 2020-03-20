LePackage package
=================

Submodules
----------

.. _label_CommonTools:

LePackage.CommonTools module
----------------------------

.. automodule:: LePackage.CommonTools
   :members:
   :undoc-members:
   :show-inheritance:

LePackage.SpecialFunctions module
---------------------------------

.. automodule:: LePackage.SpecialFunctions
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: LePackage
   :members:
   :undoc-members:
   :show-inheritance:



essai soulignement simple avec ###
##################################


essai soulignement simple avec ***
**********************************


essai soulignement simple avec ===
==================================


essai soulignement simple avec ---
----------------------------------


essai soulignement simple avec ^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


essai soulignement simple avec """
""""""""""""""""""""""""""""""""""


[essai] footnotes
===================================

Lorem ipsum [#]_ dolor sit amet ... [#]_

.. rubric:: Footnotes

.. [#] Text of the first footnote.
.. [#] Text of the second footnote.


[essai] sectionauthor
===================================
.. sectionauthor:: François CHANEL <francois.chanel@edf.fr>



[essai] \:mod\:
-----------------

:mod:`parrot` -- Dead parrot access
===================================

.. module:: parrot
   :platform: Unix, Windows
   :synopsis: Analyze and reanimate dead parrots.
.. moduleauthor:: Eric Cleese <eric@python.invalid>
.. moduleauthor:: John Idle <john@python.invalid>


[essai] ..function
===================================

.. function:: spam(eggs)
              ham(eggs)
   :noindex:

   Spam or ham the foo.


[essai] ..data
===================================

.. data:: ma_data(truc)

   ci-gît la docstring de data


[essai] ..decorator
===================================
.. decorator:: removename

   Remove name of the decorated function.

.. decorator:: setnewname(name)

   Set name of the decorated function to *name*.


[essai] ..class
===================================
.. class:: Spam

   Description of the class.

   .. attribute:: ham

      Description of the attribute.
   

   .. method:: taChatte

      fait un truc immonde



[essai] code python
===================================

>>> 2+2
4
>>> 3+3
6


[essai] code python v2
===================================
.. code-block:: python
   :linenos:


   >>> 2+2
   4
   >>> 3+3
   6


.. code-block:: python
   :linenos:


   >>> df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
   ...                    columns=['a', 'b', 'c'])
   >>> df2
      a  b  c
   0  1  2  3
   1  4  5  6
   2  7  8  9


.. code-block:: python
   :linenos:

   >>> import numpy as np
   >>> import pandas as pd

   >>> my_index = pd.date_range(
   ...   start=2010, 
   ...   periods=10, 
   ...   freq='24h', 
   ...   tz='Europe/Paris'
   ... )

   >>> my_data  = np.random.randint(0, 10, len(my_index))

   >>> ts = pd.Series(
   ...   index=my_index,
   ...   data=my_data
   ... )

   >>> ts
   1970-01-01 00:00:00.000002010    1
   1970-01-02 00:00:00.000002010    9
   1970-01-03 00:00:00.000002010    4
   1970-01-04 00:00:00.000002010    9
   1970-01-05 00:00:00.000002010    1
   1970-01-06 00:00:00.000002010    1
   1970-01-07 00:00:00.000002010    6
   1970-01-08 00:00:00.000002010    1
   1970-01-09 00:00:00.000002010    2
   1970-01-10 00:00:00.000002010    4
   Freq: 24H, dtype: int32



.. literalinclude:: example.py
   :linenos:




[essai] rôles markups
===================================
:meth:`~Queue.Queue.get`

:mod:`oh_le_joli_module`

:class:`oh_la_jolie_classe`

:token:`oh_le_joli_token`

:menuselection:`Start --> Programs`



.. _my-reference-label:

[essai] Section to cross-reference
===================================

This is the text of the section.

It refers to the section itself, see :ref:`my-reference-label`.

Et là on revient à CommonTools, regardez --> :ref:`label_CommonTools`


[essai] Paragraph-level markup
===================================
.. note::

   This function is not suitable for sending spam e-mails.


.. warning::

   Le motherfuckiing proxy c'est trop chiant !


.. deprecated:: 3.8

   n'utilisez que la version ultime avec décorateur made in francoischanel


.. seealso::

   Module :mod:`zipfile`
      Documentation of the :mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.


.. .. centered::

..    voilà le paragraphe qu'on espère retrouver centré.


.. .. toctree::
..    :maxdepth: 2

..    LePackage


.. index::
   single: execution; context
   module: __main__
   module: sys
   triple: module; search; path


.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`


Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.




[essai] headers et consort
===================================

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+



	

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
=====  =====  ======



[essai] audomodule math
===================================

.. automodule:: math