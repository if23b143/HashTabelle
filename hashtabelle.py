import os
import csv
import matplotlib.pyplot as plt

#globale variable, damit load richtig funktioniert
filename = 'hashtabelle.csv'


class class_stock:
    def __init__(self, name, WKN, kuerzel):
        self.data = []
        self.name = name
        self.WKN = WKN
        self.kuerzel = kuerzel

    def to_dict(self):
        return{"data": self.data, "name": self.name, "WKN": self.WKN, "kuerzel": self.kuerzel}    
    
    def read_csv(self, filename):
        #print("Reading CSV from file:", filename)
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            #next(csv_reader) #skipped die erste Zeile
            for row in csv_reader:
                #print("Read row:", row)
                self.data.append(row)
        #print("CSV data read successfully. Data:", self.data)

    def clear_data(self):
        self.data = []
        self.name = 0
        self.WKN = 0
        self.kuerzel = 0

    def delete_class(self):
        del self.data
        del self.name
        del self.WKN
        del self.kuerzel
        del self


def my_serializer(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    else:
        return obj


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

  


def delete():

    kuerzel = input("Wie heißt das Kürzel: ")
    string_to_int = sum(ord(character) for character in kuerzel)
    hashzahl = string_to_int % 1301

    if hashtabelle[hashzahl] != 0 and hashtabelle[hashzahl].kuerzel == kuerzel:
        print("goodbye")
        hashtabelle[hashzahl].delete_class()
        hashtabelle[hashzahl] = 0
        print("goodbe")
    elif hashtabelle[hashzahl] != 0:
        # quadratische sondierung
        for i in range(1301):
            # erstelle eine neue hashzahl
            t = (hashzahl + i * i) % 1301
            if (hashtabelle[t].kuerzel == kuerzel):
                # Break the loop after
                # inserting the value
                # in the table
               
                # array auf der stelle "hash" wird hineingefügt
                print("hello")
                hashtabelle[t].delete_class()
                hashtabelle[t]
                print("hhel")
                break
    else:
        print("Es wurde kein Kuerzel gefunden!")



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

    #wenn kein objekt --> hashtabelle gibt fehler aus
    if hashtabelle[hashzahl] != 0 and hashtabelle[hashzahl].kuerzel == kuerzel:
        print("goodbye")
        hashtabelle[hashzahl].read_csv(file_path)
        print("goodbye")
        for i in hashtabelle[hashzahl].data:
            hashtabelle[hashzahl].data


    elif hashtabelle[hashzahl] != 0:
        # quadratische sondierung
        for i in range(1301):
            # erstelle eine neue hashzahl
            t = (hashzahl + i * i) % 1301
            if (hashtabelle[t].kuerzel == kuerzel):
                # Break the loop after
                # inserting the value
                # in the table
               
                # array auf der stelle "hash" wird hineingefügt
                print("hello")
                hashtabelle[t].read_csv(file_path)
                print("hhel")
                break
    else:
        print("Es wurde kein Kuerzel gefunden!")

    # print(hashtabelle[hashzahl].data)
    # print(hashtabelle[hashzahl].name)
    # print(hashtabelle[hashzahl].WKN)
    # print(hashtabelle[hashzahl].kuerzel)
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
    kuerzel = input("Wie heißt das Kürzel: ")
    string_to_int = sum(ord(character) for character in kuerzel)
    hashzahl = string_to_int % 1301

    if hashtabelle[hashzahl] != 0 and hashtabelle[hashzahl].kuerzel == kuerzel:
       #gibt den letzten Eintrag
       print("Aktuellster Kurs:", hashtabelle[hashzahl].data[-1])
    elif hashtabelle[hashzahl] != 0:
        # quadratische sondierung
        for i in range(1301):
            # erstelle eine neue hashzahl
            t = (hashzahl + i * i) % 1301
            if (hashtabelle[t].kuerzel == kuerzel):
                # Break the loop after
                # inserting the value
                # in the table
               
                # array auf der stelle "hash" wird hineingefügt
                
                
                print("Aktuellster Kurs:", hashtabelle[hashzahl].data[-1])
                break
    else:
        print("Es wurde kein Kuerzel gefunden!")


def plot():
    kuerzel = input("Welches Kürzel möchten Sie plotten? ")
    string_to_int = sum(ord(character) for character in kuerzel)
    hashzahl = string_to_int % 1301
    
    stock = None

    if hashtabelle[hashzahl] != 0 and hashtabelle[hashzahl].kuerzel == kuerzel:
        stock = hashtabelle[hashzahl]
    elif hashtabelle[hashzahl] != 0:
        for i in range(1301):
            t = (hashzahl + i * i) % 1301
            if hashtabelle[t] != 0 and hashtabelle[t].kuerzel == kuerzel:
                stock = hashtabelle[t]
                break
    
    if stock is not None and stock.data:
        try:
            dates = []
            adj_closes = []
            for row in stock.data:
                try:
                    adj_close = float(row[1])
                    dates.append(row[0])
                    adj_closes.append(adj_close)
                except ValueError:
                    continue

            if dates and adj_closes:
                plt.figure(figsize=(10, 6))
                plt.plot(dates, adj_closes, color='blue', label=kuerzel)
                
                plt.xlabel('Date')
                plt.ylabel('Adj Close')
                plt.title(f'{kuerzel} Aktienkursverlauf')
                
                plt.grid(True)
                plt.legend()
                plt.show()
            else:
                print("Keine gültigen Daten zum Plotten vorhanden.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
    else:
        print("Es wurden keine Daten für das angegebene Kürzel gefunden oder das Kürzel existiert nicht.")

def save():
    #bearbeitet das array in ein besseres objeke?
    serialized_objects = [my_serializer(obj) for obj in hashtabelle]
    headers = ['data', 'name', 'WKN', 'kuerzel']

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for item in serialized_objects:
            #wenn "item" ein dict-object ist: dann True
            if isinstance(item, dict):
                writer.writerow(item)
            else:
                writer.writerow({'data': '[]', 'name': '', 'WKN': 0, 'kuerzel': ''})
    print(f'Data saved to {filename}')


def load():
    #cleared die gesamte hashtabelle vor dem loaden
    global hashtabelle
    hashtabelle = [0] * 1301
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            index = 0
            for row in csv_reader:
                if row['name'] == '' and row['WKN'] == '0' and row['kuerzel'] == '':
                    #wenn es leer ist
                    hashtabelle[index] = 0
                else:
                    #wenn dateien sind
                    stock = class_stock(row['name'], row['WKN'], row['kuerzel'])
                    if row['data'] != '[]':
                        stock.data = eval(row['data'])
                    hashtabelle[index] = stock
                index += 1
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"File {filename} not found. Load operation aborted.")



hashtabelle = [0] * 1301
#TODO BESSERE WHILE SCHLEIFE ERFINDEN
zahl = 1
while zahl == 1:
    print("1. Eine Aktie hinzufügen")
    print("2. Eine Aktie löschen")
    print("3. Aktie aus csv importieren")
    print("4. Die aktuellsten Eintrage einer Aktie suchen")
    print("5. Eine Aktie graphisch darstellen")
    print("6. Die gesamte Tabelle speichern")
    print("7. Eine Tabelle laden")
    print("8. Programm beenden")
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
