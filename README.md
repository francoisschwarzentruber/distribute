# distribute
Distribute documents by email.

## Motivation
Suppose you have a list of student emails in emails.txt. You also have PDFs to distribute to them. The name of PDFs are close to the emails. For instance, the PDF of "robert.dupond@awesomeuniversity.fr" is "ROBert_DUPOND_doc.pdf". This script will match the documents to the emails, and then send the documents.

It avoids to do by hand, or to use a cryptic graphical user interface.


## Usage

- Create a folder
- Add `distribute.py` in it
- Add the list of emails in emails.txt in it
- Add the documents whose names somehow close to the emails
- Run `python3 distribute.py`
