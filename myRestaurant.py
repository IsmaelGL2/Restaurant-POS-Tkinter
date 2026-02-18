from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

preciosComida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
preciosBebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
preciosPostres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visorCalculadora.delete(0, END)
    visorCalculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visorCalculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visorCalculadora.delete(0, END)
    visorCalculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadrosComida:
        if variableComida[x].get() == 1:
            cuadrosComida[x].config(state=NORMAL)
            if cuadrosComida[x].get() == '0':
                cuadrosComida[x].delete(0, END)
            cuadrosComida[x].focus()
        else:
            cuadrosComida[x].config(state=DISABLED)
            textoComida[x].set('0')
        x += 1
    
    x = 0
    for c in cuadrosBebida:
        if variableBebida[x].get() == 1:
            cuadrosBebida[x].config(state=NORMAL)
            if cuadrosBebida[x].get() == '0':
                cuadrosBebida[x].delete(0, END)
            cuadrosBebida[x].focus()
        else:
            cuadrosBebida[x].config(state=DISABLED)
            textoBebida[x].set('0')
        x += 1

    x = 0
    for c in cuadrosPostre:
        if variablePostre[x].get() == 1:
            cuadrosPostre[x].config(state=NORMAL)
            if cuadrosPostre[x].get() == '0':
                cuadrosPostre[x].delete(0, END)
            cuadrosPostre[x].focus()
        else:
            cuadrosPostre[x].config(state=DISABLED)
            textoPostre[x].set('0')
        x += 1

def total():
    subTotalComida = 0
    p = 0
    for cantidad in textoComida:
        subTotalComida = subTotalComida + (float(cantidad.get()) * preciosComida[p])
        p += 1

    subTotalBebida = 0
    p = 0
    for cantidad in textoBebida:
        subTotalBebida = subTotalBebida + (float(cantidad.get()) * preciosBebida[p])
        p += 1

    subTotalPostre = 0
    p = 0
    for cantidad in textoPostre:
        subTotalPostre = subTotalPostre + (float(cantidad.get()) * preciosPostres[p])
        p += 1

    subTotal = subTotalComida + subTotalBebida + subTotalPostre
    impuestos = subTotal * 0.07
    total = subTotal + impuestos

    varCostoComida.set(f'$ {round(subTotalComida, 2)}')
    varCostoBebida.set(f'$ {round(subTotalBebida, 2)}')
    varCostoPostre.set(f'$ {round(subTotalPostre, 2)}')
    varSubtotal.set(f'$ {round(subTotal, 2)}')
    varInpuesto.set(f'$ {round(impuestos, 2)}')
    varTotal.set(f'$ {round(total, 2)}')

def recibo():
    textoRecibo.delete(1.0, END)
    numRecibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fechaRecibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    textoRecibo.insert(END, f'Datos:\t{numRecibo}\t\t{fechaRecibo}\n')
    textoRecibo.insert(END, f'*' * 47 + '\n')
    textoRecibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    textoRecibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in textoComida:
        if comida.get() != '0':
            textoRecibo.insert(END, f'{listaComidas[x]}\t\t{comida.get()}\t'
                               f'$ {int(comida.get()) * preciosComida[x]}\n')
        x += 1

    x = 0
    for bebida in textoBebida:
        if bebida.get() != '0':
            textoRecibo.insert(END, f'{listaBebidas[x]}\t\t{bebida.get()}\t'
                               f'$ {int(bebida.get()) * preciosBebida[x]}\n')
        x += 1

    x = 0
    for postre in textoPostre:
        if postre.get() != '0':
            textoRecibo.insert(END, f'{listaPostres[x]}\t\t{postre.get()}\t'
                               f'$ {int(postre.get()) * preciosPostres[x]}\n')
        x += 1

    textoRecibo.insert(END, f'-' * 54 + '\n')
    textoRecibo.insert(END, f' Costo de la comida: \t\t\t{varCostoComida.get()}\n')
    textoRecibo.insert(END, f' Costo de la Bebida: \t\t\t{varCostoBebida.get()}\n')
    textoRecibo.insert(END, f' Costo de la Postres: \t\t\t{varCostoPostre.get()}\n')
    textoRecibo.insert(END, f'-' * 54 + '\n')
    textoRecibo.insert(END, f' Sub-total: \t\t\t{varSubtotal.get()}\n')
    textoRecibo.insert(END, f' Impuestos: \t\t\t{varInpuesto.get()}\n')
    textoRecibo.insert(END, f' Total: \t\t\t{varTotal.get()}\n')
    textoRecibo.insert(END, f'*' * 47 + '\n')
    textoRecibo.insert(END, 'Lo esperamos pronto')

def guardar():
    infoRecibo = textoRecibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(infoRecibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

def resetear():
    textoRecibo.delete(0.1, END)

    for texto in textoComida:
        texto.set('0')
    for texto in textoBebida:
        texto.set('0')
    for texto in textoPostre:
        texto.set('0')

    for cuadro in cuadrosComida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadrosBebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadrosPostre:
        cuadro.config(state=DISABLED)

    for v in variableComida:
        v.set(0)
    for v in variableBebida:
        v.set(0)
    for v in variablePostre:
        v.set(0)

    varCostoComida.set('')
    varCostoBebida.set('')
    varCostoPostre.set('')
    varSubtotal.set('')
    varInpuesto.set('')
    varTotal.set('')

#Iniciar tkinter
aplicacion = Tk()

#tamno de la ventana
aplicacion.geometry('1020x630+0+0')

#Evitat maximizar
aplicacion.resizable(0, 0)

#Titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

#color de fondo de la ventana
aplicacion.config(bg='burlywood')

#Panel superior
panelSuperior = Frame(aplicacion, bd=1, relief=FLAT)
panelSuperior.pack(side=TOP)

#Etiqueta titulo
etiquetaTitulo = Label(panelSuperior, text='Sistema de facturacion', fg='azure4',
                       font=('Dosis', 58), bg='burlywood', width=27)

etiquetaTitulo.grid(row=0, column=0)

#panel izquierdo
panelIzquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panelIzquierdo.pack(side=LEFT)

#Panel costos
panelCostos = Frame(panelIzquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panelCostos.pack(side=BOTTOM)

#Panel comida
panelComidas = LabelFrame(panelIzquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panelComidas.pack(side=LEFT)

#Panel bebidas
panelBebidas = LabelFrame(panelIzquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panelBebidas.pack(side=LEFT)

#Panel postres
panelPostres = LabelFrame(panelIzquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panelPostres.pack(side=LEFT)

#Panel derecha
panelDerecha = Frame(aplicacion, bd=1, relief=FLAT)
panelDerecha.pack(side=RIGHT)

#panel calculadora
panelCalculadora = Frame(panelDerecha, bd=1, relief=FLAT, bg='burlywood')
panelCalculadora.pack()

#panel recibo
panelRecibo = Frame(panelDerecha, bd=1, relief=FLAT, bg='burlywood')
panelRecibo.pack()

#panel botones
panelBotones = Frame(panelDerecha, bd=1, relief=FLAT, bg='burlywood')
panelBotones.pack()

#Lista de productos
listaComidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
listaBebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
listaPostres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

#Generar items comida
variableComida = []
cuadrosComida =[]
textoComida = []
contador = 0
for comida in listaComidas:

    #Crear checkbutton
    variableComida.append('')
    variableComida[contador] = IntVar()
    comida = Checkbutton(panelComidas, 
                         text=comida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variableComida[contador],
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    #Cear los cuadros de entrada
    cuadrosComida.append('')
    textoComida.append('')
    textoComida[contador] = StringVar()
    textoComida[contador].set('0')
    cuadrosComida[contador] = Entry(panelComidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=textoComida[contador])
    cuadrosComida[contador].grid(row=contador,
                                 column=1)
    contador += 1

#Generar items bebida
variableBebida = []
cuadrosBebida =[]
textoBebida = []
contador = 0
for bebida in listaBebidas:

    #Crear checkbutton
    variableBebida.append('')
    variableBebida[contador] = IntVar()
    bebida = Checkbutton(panelBebidas, 
                         text=bebida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variableBebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #Cear los cuadros de entrada
    cuadrosBebida.append('')
    textoBebida.append('')
    textoBebida[contador] = StringVar()
    textoBebida[contador].set('0')
    cuadrosBebida[contador] = Entry(panelBebidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=textoBebida[contador])
    cuadrosBebida[contador].grid(row=contador,
                                 column=1)

    contador += 1

#Generar items postre
variablePostre = []
cuadrosPostre =[]
textoPostre = []
contador = 0
for postre in listaPostres:

    #Crear checkbutton
    variablePostre.append('')
    variablePostre[contador] = IntVar()
    postre = Checkbutton(panelPostres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variablePostre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)
    
    #Cear los cuadros de entrada
    cuadrosPostre.append('')
    textoPostre.append('')
    textoPostre[contador] = StringVar()
    textoPostre[contador].set('0')
    cuadrosPostre[contador] = Entry(panelPostres,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=textoPostre[contador])
    cuadrosPostre[contador].grid(row=contador,
                                 column=1)

    contador += 1

#Variables
varCostoComida = StringVar()
varCostoBebida = StringVar()
varCostoPostre = StringVar()
varSubtotal = StringVar()
varInpuesto = StringVar()
varTotal = StringVar()

#Etiquetas de costo y campos de entrada
etiquetaCostoComida = Label(panelCostos,
                            text='Costo Comida',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiquetaCostoComida.grid(row=0, column=0)

textoCostoComida = Entry(panelCostos,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=varCostoComida)
textoCostoComida.grid(row=0, column=1, padx=41)

etiquetaCostoBebida = Label(panelCostos,
                            text='Costo Bebida',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiquetaCostoBebida.grid(row=1, column=0)

textoCostoBebida = Entry(panelCostos,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=varCostoBebida)
textoCostoBebida.grid(row=1, column=1, padx=41)

#-Postre
etiquetaCostoPostre = Label(panelCostos,
                            text='Costo Postre',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiquetaCostoPostre.grid(row=2, column=0)

textoCostoPostre = Entry(panelCostos,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=varCostoPostre)
textoCostoPostre.grid(row=2, column=1, padx=41)

#-Subtotal
etiquetaSubtotal = Label(panelCostos,
                            text='Subtotal',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiquetaSubtotal.grid(row=0, column=2)

textoSubtotal = Entry(panelCostos,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=varSubtotal)
textoSubtotal.grid(row=0, column=3, padx=41)

#-Inpuesto
etiquetaInpuesto = Label(panelCostos,
                            text='Inpuesto',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiquetaInpuesto.grid(row=1, column=2)

textoInpuesto = Entry(panelCostos,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=varInpuesto)
textoInpuesto.grid(row=1, column=3, padx=41)

#-Total
etiquetaTotal = Label(panelCostos,
                            text='Total',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiquetaTotal.grid(row=2, column=2)

textoTotal = Entry(panelCostos,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=varTotal)
textoTotal.grid(row=2, column=3, padx=41)

#Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botonesCreados = []
columnas = 0
for boton in botones:
    boton = Button(panelBotones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    
    botonesCreados.append(boton)
    
    boton.grid(row=0,
               column=columnas)
    columnas += 1

botonesCreados[0].config(command=total)
botonesCreados[1].config(command=recibo)
botonesCreados[2].config(command=guardar)
botonesCreados[3].config(command=resetear)

#Area de recibo
textoRecibo = Text(panelRecibo,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=42,
                   height=10)
textoRecibo.grid(row=0,
                 column=0)

#Calculadora
visorCalculadora = Entry(panelCalculadora,
                         font=('Dosis', 16, 'bold'),
                         width=32,
                         bd=1)
visorCalculadora.grid(row=0,
                      column=0,
                      columnspan=4)

botonesCalculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                      '1', '2', '3', 'x', 'R', 'B', '0', '/']
botonesGuardados = []

fila = 1
columna = 0
for boton in botonesCalculadora:
    boton = Button(panelCalculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    
    botonesGuardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botonesGuardados[0].config(command=lambda : click_boton('7'))
botonesGuardados[1].config(command=lambda : click_boton('8'))
botonesGuardados[2].config(command=lambda : click_boton('9'))
botonesGuardados[3].config(command=lambda : click_boton('+'))
botonesGuardados[4].config(command=lambda : click_boton('4'))
botonesGuardados[5].config(command=lambda : click_boton('5'))
botonesGuardados[6].config(command=lambda : click_boton('6'))
botonesGuardados[7].config(command=lambda : click_boton('-'))
botonesGuardados[8].config(command=lambda : click_boton('1'))
botonesGuardados[9].config(command=lambda : click_boton('2'))
botonesGuardados[10].config(command=lambda : click_boton('3'))
botonesGuardados[11].config(command=lambda : click_boton('*'))
botonesGuardados[12].config(command=obtener_resultado)
botonesGuardados[13].config(command=borrar)
botonesGuardados[14].config(command=lambda : click_boton('0'))
botonesGuardados[15].config(command=lambda : click_boton('/'))


#Evtiar que la pantalla se cierre
aplicacion.mainloop()