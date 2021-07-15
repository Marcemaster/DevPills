import tkinter

wroot = tkinter.Tk()


fr_buttons = tkinter.Frame(wroot, width=360, height=360, bg="#f0f0f0")
fr_buttons.place(x=0,y=0)
fr_buttons.pack_propagate(False)
fr_buttons.config(width=360, height=360)
btn_reset = tkinter.Button(fr_buttons, text="Reset")
btn_max = tkinter.Button(fr_buttons, text="Full Screen")
btn_centrar = tkinter.Button(fr_buttons, text="Centrar")

btn_reset.pack(side=tkinter.TOP)
btn_max.pack(side=tkinter.TOP)
btn_centrar.pack(side=tkinter.TOP)

btn_reset.pack(expand=True)
btn_max.pack(expand=True, fill=tkinter.BOTH)
btn_centrar.pack(expand=True, fill=tkinter.Y)

wroot.title("Jugando con Widgets")
wroot.geometry('600x600')
wroot.geometry()
