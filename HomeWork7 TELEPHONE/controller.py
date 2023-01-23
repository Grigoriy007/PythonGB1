from model import db_phone as db
import view
import model

def start():
    user_choise = 0
    while user_choise != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = db.get()
                view.show_contacts(phone_book)
            case 2:
                db.open()
                view.load_success()
            case 3:
                db.save()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                db.update(new)
            case 5:
                pass
            case 6:
                pass
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
