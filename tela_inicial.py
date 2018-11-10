import tkinter as tk
import os


def ler_tweets():
    os.system('python main.py')





def visualizar():
    os.system('python visualiza_dados.py')

def consultar():
    os.system('python consultas.py')

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

btn_ler_tweets = tk.Button(frame, 
                   text="LER TWEETS", 
                   fg="red",
                   command=ler_tweets)

btn_ler_tweets.pack(side=tk.LEFT)



btn_visualiza = tk.Button(frame, text="VISUALIZA", command=visualizar)
btn_visualiza.pack(side=tk.RIGHT)

btn_consultar = tk.Button(frame, text='CONSULTAS', command=consultar)
btn_consultar.pack(side=tk.RIGHT)

root.mainloop()