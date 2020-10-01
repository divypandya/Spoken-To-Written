
=================
Spoken To Written
=================
This is a Python module which can that can convert a paragraph of spoken english to written english.

 For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

+++++++++++++
Installation:
+++++++++++++

  You can install the module using Python Package Index using the below command.

.. code-block:: python

   >>python3 setup.py install  



+++++
Usage:
+++++

.. code-block:: python
    
    	>>python3
	>>from spokentowritten import sp2wr
	>>sp2wr.convert_sp_to_wr()
	>>
	[IN]:Enter Your paragraph of spoken english:
 	
 	Hi! I am divy. I am a small Programmer. I work at apple store from 9 A M to 5 P M. I earn hundred dollars per day. My contact number contains double 0, quadruple 4, single 2 and triple 4. Recently, My weight got double the weight of my friend whom I call C M. 

	[OUT]:The input Spoken English Paragraph: 

 	" Hi! I am divy. I am a small Programmer. I work at apple store from 9 A M to 5 P M. I earn hundred dollars per day. My contact number contains double 0, quadruple 4, single 2 and triple 4. Recently, My weight got double the weight of my friend whom I call C M. "

	Converted Written English Paragraph: 

 	" Hi! I am divy. I am a small Programmer. I work at apple store from 9 AM to 5 PM. I earn $100 per day. My contact number contains 00, 4444, 2 and 444. Recently, My weight got double the weight of my friend whom I call CM."