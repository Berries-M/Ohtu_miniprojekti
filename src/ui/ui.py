"""Yksinkertainen tekstikäyttöliittymä.
"""
from entities.readingtip import ReadingTip
from repositories.db_interface import DatabaseInterface

class UI:
    """Käyttöliittymäluokka, joka pystyy lisäämään ja
    näyttämään lukuvinkkejä.
    """

    def __init__(self, db: DatabaseInterface):
        self.actions = {
            "a": "add a new item",
            "v": "view your items",
            "c": "clear all items",
            "q": "exit program"
        }

        self.db = db

    def start(self):
        """Käyttöliittymälooppi. Kysyy toimintaa ja kutsuu
        sen perusteella toiminnan käsittelevää metodia.
        """
        print("Recommendations")

        while True:
            self._print_actions()
            action = input()

            if action == "v":
                self._view_items()
            elif action == "a":
                self._add_item()
            elif action == "c":
                self._clear_db()
            elif action == "q":
                self.db.Delete()
                break
            else:
                print("\ncommand not found\n")
                continue

    def _print_actions(self):
        """Tulostaa vaihtoehdot
        """
        print("choose action:")
        for i in self.actions:
            print(f"\"{i}\": {self.actions[i]}")


    def _add_item(self):
        """Kysyy lukuvinkin tiedot ja lisää sen listaan
        """
        description = input("item description: ")
        item = ReadingTip(description)
        self.db.Add(item)

        print(f"\nitem {item} added \n")


    def _view_items(self):
        """Näyttää listan lukuvinkit
        """
        print("\nitems: \n")
        for index, lukuvinkki in enumerate(self.db.Read()):
            print(f'{index+1}: {lukuvinkki}')


    def _clear_db(self):
        """Poistaa kaikki lukuvinkit
        """
        self.db.Clear()
