from asyncio import tasks
from optparse import Values
import PySimpleGUI as sg

data = ''

layout = [
    [sg.CalendarButton("Set date", size=(10, 1)),
     sg.T("-- -- -- --", key="-DATE-")],
    [sg.T("Add Task", size=(10, 1)), sg.I(
        key="-TASK-", font=("None 15"), size=(32, 1))],
    [sg.Table(values=data, headings=["Index", "Date", "Task"], key="-TABLE-", size=(500, 10), auto_size_columns=False,
              col_widths=[5, 9, 30], vertical_scroll_only=False, justification='l', font="None 15",enable_click_events=True)],
    [sg.B("ADD",size=(10,1),button_color="green"), sg.B("DELETE", key="-DEL-",button_color="red"), sg.Exit()]
]

window = sg.Window("Task--Reminder..! ", layout)
counter = 1
tasks = []
while True:
    event, value = window.read()
    if event in ("Exit", sg.WIN_CLOSED):
        window.close()
        break
    elif event == "ADD":
        date = window["-DATE-"].get().split()[0]
        task = [[counter,date,value["-TASK-"]]]
        tasks = task+tasks
        window["-TABLE-"].update(tasks)
        window["-TASK-"].update('')
        counter += 1
    elif event == "-DEL-":
        values = value["-TABLE-"]
        if  values:
            index = values[0]
            del tasks[index]
            window["-TABLE-"].update(tasks)


    print(event, value,tasks)
