# Importa a biblioteca tkinter para criar interfaces gráficas
import tkinter
from tkinter import *

# Cria a janela principal da aplicação
root = Tk()
root.title("Lista de tarefas")  # Define o título da janela
root.geometry("400x650+400+100")  # Define o tamanho e a posição da janela
root.resizable(False, False)  # Define que a janela não pode ser redimensionada

# Lista que armazenará as tarefas
task_list = []

# Função para adicionar uma tarefa
def addTask():
    task = task_entry.get()  # Obtém o texto da entrada de tarefas
    task_entry.delete(0, END)  # Limpa a entrada de tarefas

    if task:
        # Abre o arquivo de tarefas no modo de adição e escreve a nova tarefa
        with open("listatarefa.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)  # Adiciona a nova tarefa à lista de tarefas
        listbox.insert(END, task)  # Adiciona a nova tarefa à lista visual

# Função para deletar uma tarefa
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))  # Obtém a tarefa selecionada na lista
    if task in task_list:
        task_list.remove(task)  # Remove a tarefa da lista de tarefas
        # Reescreve o arquivo de tarefas com a lista atualizada
        with open("listatarefa.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)  # Remove a tarefa da lista visual

# Função para abrir o arquivo de tarefas e carregar as tarefas na lista
def openTaskFile():
    try:
        global task_list
        with open("listatarefa.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('listatarefa.txt', 'w')  # Cria um novo arquivo se não existir
        file.close()

# Ícone da janela
Image_icon = PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

# Barra superior
TopImage = PhotoImage(file="topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

# Cabeçalho
heading = Label(root, text="Tarefas", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Área principal para entrada de tarefas
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()  # Variável que armazenará a tarefa digitada
task_entry = Entry(frame, width=18, font="arial 20", bd=0)  # Campo de entrada de texto
task_entry.place(x=10, y=7)
task_entry.focus()  # Define o foco inicial no campo de entrada

# Botão para adicionar tarefas
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# Listbox para exibir as tarefas
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)  # Barra de rolagem para o listbox
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Carrega as tarefas do arquivo ao iniciar o programa
openTaskFile()

# Botão para deletar tarefas
Delete_icon = PhotoImage(file="delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

# Mantém a janela aberta e em execução
root.mainloop()
