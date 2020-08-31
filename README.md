# -info-retrieval-Hindi

## Abstract

Information retrieval (IR) may be defined as a software program that deals with the organization, storage, retrieval and evaluation of information from document repositories particularly textual information. The system assists users in finding the information they require but it does not explicitly return the answers of the questions. It informs the existence and location of documents that might consist of the required information. The documents that satisfy the user's requirement are called relevant documents. A perfect IR system will retrieve only relevant documents.The main goal of IR research is to develop a model for retrieving information from the repositories of documents. Here, we are going to discuss a classical problem, named ad-hoc retrieval problem, related to the IR system.In ad-hoc retrieval, the user must enter a query in natural language that describes the required information. Then the IR system will return the required documents related to the desired information. For example, suppose we are searching something on the Internet and it gives some exact pages that are relevant as per our requirement but there can be some non-relevant pages too. This is due to the ad-hoc retrieval problem.
<br>

### How it's done

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
