from tkinter import*

root = Tk() 

#создаем кликабельное игровое поле
board_buttons = [Button(width=6,height=2, font=('Calibri', 28), text=' ', bg='white smoke') for i in range(9)]
row=1
column=0
for i in range(9):
    board_buttons[i].config(command= lambda bb=board_buttons[i]:butclick(bb))
    board_buttons[i].grid(row=row, column=column)
    column+=1
    if column==3:
        row+=1
        column=0


click = True 
player= 'X' #игра начинается с Х
count=0
#function to click buttons
def butclick(bb):
    global click, count, player, label

    if bb['text']==' ' and click==True:
        bb['text']='X'
        click = False
        player = 'O'
        count+=1
        label.config(text=player +' turn')
    elif bb['text']==' ' and click==False:
        bb['text']='O'
        click = True
        player = 'X'
        count+=1
        label.config(text=player +' turn')
    else:
        label.config(text='This place has is already selected\n Pick an emphty one')
    checkwin()

#смотрим есть ли winner
def checkwin():
    global player, count

    if board_buttons[0]['text']==board_buttons[1]['text']==board_buttons[2]['text']!=' ' or board_buttons[3]['text']==board_buttons[4]['text']==board_buttons[5]['text']!=' ' or board_buttons[6]['text']==board_buttons[7]['text']==board_buttons[8]['text']!=' ':
        if player =='X':
            player='O'
        else:
            player='X'
        label.config(text=player + ' won!!')
        disable_all()
    elif board_buttons[0]['text']==board_buttons[3]['text']==board_buttons[6]['text']!=' ' or board_buttons[1]['text']==board_buttons[4]['text']==board_buttons[7]['text']!=' ' or board_buttons[2]['text']==board_buttons[5]['text']==board_buttons[8]['text']!=' ':
        if player =='X':
            player='O'
        else:
            player='X'
        label.config(text=player + ' won!!')
        disable_all()
    elif board_buttons[0]['text']==board_buttons[4]['text']==board_buttons[8]['text']!=' ' or board_buttons[2]['text']==board_buttons[4]['text']==board_buttons[6]['text']!=' ':
        if player =='X':
            player='O'
        else:
            player='X'
        label.config(text=player + ' won!!')
        disable_all()
    elif count==9:
        label.config(text='TIE!')
        disable_all()

#stopping the game if smn has won
def disable_all():
    for i in range(9):
        board_buttons[i].config(state=DISABLED)

#строка, где будет инфа о игре
label = Label(text=player + ' turn', font=('Calibri', 16))
label.grid(row=4, columnspan=3)

root.mainloop()