# -info-retrieval-Hindi

The following is Boolean Query Model for IR-system for Hindi language. 

The project works on the basis of **Inverted Indexing**

## Setting up the project 
* Create a Folder
* Inside that folder create a python virtual environment  <br>
creating an virtual environment using conda - `conda create -n <any_apt_name>`
* Now activate the virtual environment <br>
for conda - `conda activate <any_apt_name>` 
* Installing the required package 
`pip install -r requirements.txt`
* then type following commands
`python`<br> After that type the given command
```
import nltk 
nltk.downloads('punkt')
```
* Now to run the project type
`python index.py`

## Add your own document
To add your document for IR just paste the textfile inside the folder **docs**.<br>
NOTE- The document should strictly be textfile(.txt). Other Document format(eg- .docx, .odt, .rtf etc) is not supported

## Python Packages Used
* tkinter 
* os
* nltk
