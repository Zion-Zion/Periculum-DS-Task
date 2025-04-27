# Periculum-DS-Task

This data pipeline is built to extract information from tbles in PDF documtents.  Due to the the unstructured nature of the data in the sample PDF and hypothetical subsequent ones, there's a repeatable process in this pipeline for parsing the PDFs correctly and extracting the specific information expected in the callback responses for future use.

[trigger.py](https://github.com/Zion-Zion/Periculum-DS-Task/blob/main/trigger.py), when run, initiates the pipeline, [periculum_functions.py](https://github.com/Zion-Zion/Periculum-DS-Task/blob/main/periculum_functions.py) to make the unstructured data into dictionary format, then dumps the output as a JSON file, [output](https://github.com/Zion-Zion/Periculum-DS-Task/blob/main/output.json).

The parsing package used is [Tabula](https://tabula.technology/), and the other package that had to be imported is the **os**, library, which was strictly for dealing with file directory issues, not for data manipulation/transformation.
