Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=========== RESTART: C:/Users/ajayk/OneDrive/Documents/NLP CO2-AT1.py ==========
---------------------------------------------------------------------------
Word           Root           Suffix    Type              Normalized     
---------------------------------------------------------------------------
connected      connect        ed        Inflectional      connect        
connecting     connect        ing       Inflectional      connect        
connection     connect        ion       Derivational      connect        

========= RESTART: C:/Users/ajayk/OneDrive/Documents/NLP CO2-AT1 Q2.py =========
-----------------------------------------------------------------------------------------------
Word           Prefix    Base Form      Suffix    Type              Morphological Breakdown  Root      
-----------------------------------------------------------------------------------------------
unhappy        un        happy          -         Derivational      un + happy               happy     
happiness      -         happy          ness      Derivational      happy + ness             happy     
happily        -         happy          ly        Derivational      happy + ly               happy     
>>> 
========= RESTART: C:/Users/ajayk/OneDrive/Documents/NLP CO2-AT1 Q3.py =========
-----------------------------------------------------------------------------------------------
Original Word  Stem           Removed Affix  Type              Normalized Form
-----------------------------------------------------------------------------------------------
played         play           ed             Inflectional      play           
player         play           er             Derivational      play           
playing        play           ing            Inflectional      play           
>>> 
========= RESTART: C:/Users/ajayk/OneDrive/Documents/NLP CO2-AT1 Q4.py =========
------------------------------------------------------------------------------------------------------------------------
Word        State Transition         Morphological Breakdown  Root           Classification        Normalized     
------------------------------------------------------------------------------------------------------------------------
writes      q0 -> q1 -> q2           write + s                write          Regular Inflection    write          
writing     q0 -> q1 -> q3           write + ing              write          Regular Inflection    write          
written     q0 -> q4                 written -> write         write          Irregular Inflection  write          
>>> 
========= RESTART: C:/Users/ajayk/OneDrive/Documents/NLP CO2-AT1 Q5.py =========
--------------------------------------------------------------------------------------------------------------
Word           Applied Rule             Intermediate Form        Final Stem     
--------------------------------------------------------------------------------------------------------------
relational     ational -> ate           relate                   relat          
relation       ion removed              relate                   relat          
relate         Remove final e           relate                   relat          
