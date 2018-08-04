import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan :)")
    label2.pack()

label = tkinter.Label(main_window, text="Hallo World \n Saya Anang Nugraha \n 09021381722106")
tombol = tkinter.Button(main_window, text="Klik Disini", command=event_tekan)

label.pack()
tombol.pack()

main_window.mainloop()
