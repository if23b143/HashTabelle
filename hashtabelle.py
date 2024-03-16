import os
import csv


class class_stock:


    def __init__(self, name, WKN, kuerzel):
        self.data = []
        self.name = name
        self.WKN = WKN
        self.kuerzel = kuerzel
        
    def read_csv(self, filename):
        print("Reading CSV from file:", filename)
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print("Read row:", row)
                self.data.append(row)
        print("CSV data read successfully. Data:", self.data)

    def clear_data(self):
        self.data = []


def add():
   

    name = input("Geben Sie einen Namen ein: ")
    WKN = input("Geben Sie die WertpapierKennnummer: ")
    Kuerzel = input("Geben Sie ein Kürzel ein: ")

    stock = class_stock(name, WKN, Kuerzel)  # Create a new instance of class_stock
    # nimmt ein character und wandelt es in eine zahl um und macht das mit dem gesamten Wort
    #[ord(c) for c in test]

    
    # string in int konvertieren
    string_to_int = sum(ord(character) for character in Kuerzel)
    print(string_to_int)

    # int wird gehasht
    hashzahl = string_to_int % 1301

    if hashtabelle[hashzahl] != 0:
        # quadratische sondierung
        for i in range(1301):
            # erstelle eine neue hashzahl
            t = (hashzahl + i * i) % 1301
            if hashtabelle[t] == 0:
                # Break the loop after
                # inserting the value
                # in the table
                hashtabelle[hashzahl] = stock
                break
    else:
        # array auf der stelle "hash" wird hineingefügt
        hashtabelle[hashzahl] = stock

    print(hashtabelle[hashzahl])


def delete():
    print("2. DEL")


def importieren():
    # Get the current directory
    current_directory = os.getcwd()

    # Define the folder name containing the CSV files
    folder_name = 'csv'

    # Construct the full path to the CSV folder
    folder_path = os.path.join(current_directory, folder_name)

    userinput = input("Wählen Sie die Datei: ")
    file_path = os.path.join(folder_path, userinput)

    kuerzel = input("Wie heißt das Kürzel: ")
    string_to_int = sum(ord(character) for character in kuerzel)
    hashzahl = string_to_int % 1301


    if hashtabelle[hashzahl] != 0 and hashtabelle[hashzahl].kuerzel == kuerzel:
        # quadratische sondierung
        for i in range(1301):
            # erstelle eine neue hashzahl
            t = (hashzahl + i * i) % 1301
            if (hashtabelle[t].kuerzel == kuerzel):
                # Break the loop after
                # inserting the value
                # in the table
                print("goodbye")
                hashtabelle[hashzahl].read_csv(file_path)
                print("goodbye")
                break
    else:
        # array auf der stelle "hash" wird hineingefügt
        print("hello")
        hashtabelle[hashzahl].read_csv(file_path)
        print("hhel")

    print(hashtabelle[hashzahl].data)
    print(hashtabelle[hashzahl].name)
    print(hashtabelle[hashzahl].WKN)
    print(hashtabelle[hashzahl].kuerzel)
    #stock_backlog.append(userinput)
    #print(stock_backlog)

    #stock = class_stock(userinput)  # Create a new instance of class_stock
    '''
    stock.read_csv(file_path)

    for i in stock.data:
        print(i)

    print(stock.file_path)

    print("3. IMPORT")
    '''


def search():
    print("4. SEARCH")


def plot():
    print("5. PLOT")


def save():
    print("6. SAVE")


def load():
    print("7. LOAD")

stock_backlog = []

hashtabelle = [0] * 1301
#TODO BESSERE WHILE SCHLEIFE ERFINDEN
zahl = 1
while zahl == 1:
    numberinput = int(input("Geben Sie eine Zahl ein: "))
    match numberinput:
        case 1:
            add()
        case 2:
            delete()
        case 3:
            importieren()
        case 4:
            search()
        case 5:
            plot()
        case 6:
            save()
        case 7:
            load()
        case 8:
            zahl = 2
        case default:
            print("default")
