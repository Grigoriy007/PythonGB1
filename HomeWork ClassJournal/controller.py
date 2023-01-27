import view
import model

def start():
    find_class = view.input_class()
    model.set_class(find_class)
    model.set_subdject(view.input_subject())
    file = model.open_file1()
    model.open_file2(file)
    student = ''
    while True:
        journal = model.get_jornal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()