# -info-retrieval-Hindi

The following is Boolean Query Model for IR-system for Hindi language. 

The project works on the basis of **Inverted Indexing**

## Following steps are happening in -info-retrieval-Hindi
1. Tokenization
2. Text Filtration
3. Punctuation Removal 
4. Stopword Removal
5. Stemming
6. Inverted Indexing

### Type of Searching performed are
1. Single search
2. AND search
3. OR search
4. NOT search

## Setting up the project 
* Create a Folder.
* Open Anaconda terminal( or command prompt also).
* Change the terminal directory to the project folder you have created. 
* Now create a python virtual environment  <br>
**creating an virtual environment using conda - `conda create -n <any_apt_name>`**
* Now activate the virtual environment <br>
**for conda - `conda activate <any_apt_name>`**
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
NOTE- The document should strictly be textfile(**.txt**). Other Document format(**eg- .docx, .odt, .rtf etc**) is not supported

## Python Packages Used
* tkinter 
* os
* nltk
