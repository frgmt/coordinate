coordinate
========

日本測地系と世界測地系の変換
  
How to use
-------

.. code-block:: python
  
  from coordinate import Coordinate

  c = Coordinate('35.248058', '139.039646')
  c.wgs84_to_tokyo()
  
  print(c.get_deg_latitude())
  print(c.get_deg_longitude())
