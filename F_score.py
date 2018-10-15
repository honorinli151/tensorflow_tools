'''
File: d:\MyProjects\tensorflow_tools\F2_score.py
Project: d:\MyProjects\tensorflow_tools
Created Date: Monday October 15th 2018
Author: Chenle Li
-----
Last Modified: 2018-10-15 11:04:07
Modified By: Chenle Li at <chenle.li@student.ecp.fr>
-----
Copyright (c) 2018 Chenle Li
-----
HISTORY:
Date               	  By     	Comments
-------------------	---------	---------------------------------------------------------
'''




def F_score(Precision, Recall, beta):
    """
    Calculate F score based on Precision and Recall.
    """
    return (1+beta**2)*(Precision*Recall)/(beta**2*Precision+Recall)