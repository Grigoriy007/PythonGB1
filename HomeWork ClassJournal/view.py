import model
import os.path

def input_class():
    cl = input('С каким классом работаем?: ').upper()
    choice_class = model.set_class(cl)
    control = os.path.exists(choice_class)
    if control == True:
        return cl
    else:
        print('Класс не существует!')
        return input_class()

def input_subject():
    subject = input('Какой предмет?: ').lower()
    file_open = model.open_file1()
    for string in file_open:
        if subject in string:
            return subject
            break
    print('Предмет не найден!')
    return input_subject()

def who_answer():
    student = input('Кто будет отвечать?: ')
    file_open = model.open_file1()
    for string in file_open:
        if student in string:
            return student
            break
    print('Такой ученик не найден!')
    return who_answer()


def what_mark():
    estimation = input('На какую оценку ответил?:  ')
    if int(estimation) > 5 or int(estimation) < 1:
        print('Оценка неверна!')
        return what_mark()
    else:
        return estimation


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')