from todo import ToDoRepository

def start_console(repo: ToDoRepository):
    while True:
        print("(1) Verwalten")
        print("(2) Hinzufügen")
        print("(3) Beenden")
        selection = input()

        if selection == "3":
            return

        if selection == "1":
            todos = []  # <- ToDo: Get list of all?
            if len(todos) == 0:
                print("Keine Einträge vorhanden")
            else:
                count = 0
                for i in todos:
                    print(f"({count}) {str(i)}")
                    count = count + 1

                while True:
                    mark_as_done = input('Abhacken (x für Abbruch): ')
                    if mark_as_done == "x":
                        break
                    id = int(mark_as_done)
                    # <- ToDo: id... use todos-list
        elif selection == "2":
            titel = input('Titel: ')
            # <- ToDo: add new ToDo-Entry?
