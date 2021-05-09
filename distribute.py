import os
import yagmail
import jellyfish

subject = "DM1 FOND2"

def sendDocument(yag, receiver, filename):
    # input: yag is the yagmail session
    #       receiver: emailof the receiver
    # send to receiver the document in the file filename
    yag.send(
        to=receiver,
        subject=subject,
        contents="Bonjour, veuillez trouver le document en pièce jointe. Merci de ne pas répondre à ce mail. Bonne journée, François",
        attachments=filename,
    )


def emails():
    # return the emails written in the file emails.txt
    with open('emails.txt', 'r') as fp:
        emails = fp.readlines()
        emails = filter(lambda line: "@" in line, emails)
        emails = map(lambda line: line.strip(), emails)
        emails = filter(lambda line: not line.startswith("#"), emails)
        return list(emails)


def files():
    # return a list of files in the current directory
    return os.listdir()


def distance(string1, string2):
    # return the distance between two strings. If the distance is close to 0, the strings are similar
    return jellyfish.levenshtein_distance(string1.lower(), string2.lower())


def match(emails, files):
    # return the dictionnary that match the emails to the file whose filename is the closest to the email (in terms of strings)
    dict = {}
    for email in emails:
        d = 100000
        currentFile = ""
        for file in files:
            newd = distance(email, file)
            if(newd < d):
                d = newd
                currentFile = file
        dict[email] = currentFile
    return dict


def printMatch(dict):
    # print the dictionnary {email: filename}
    row_format = "{:<40}" * 2
    print(row_format.format("Email", "Document"))
    for email in dict:
        print(row_format.format(email, dict[email]))


def main():
    dict = match(emails(), files())
    printMatch(dict)
    if(input("Do you want to send the documents? [y/n]") == "y"):
        yag = yagmail.SMTP("francois.schwarzentruber@gmail.com")
        for email in dict:
            print(f"sending {dict[email]} to {email}...")
            sendDocument(yag, email, dict[email])
            print(f"[done]")
    else:
        print("nothing has been sent.")


main()
