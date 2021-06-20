from tkinter import *
from tkinter import filedialog, messagebox
from random import *
from PIL import Image, ImageTk, ImageGrab


def dice_select():
    main.withdraw()
    dice_wind_select.deiconify()

def dice_select_one():
    dice_wind_select.withdraw()
    dice_wind_one.deiconify()

def dice_select_two():
    dice_wind_select.withdraw()
    dice_wind_two.deiconify()

def roll_one():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    die_face_one.config(text = f'{choice(number)}')
    die_face_one.pack()

def roll_two():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    die_face_two.config(text = f'{choice(number)}{choice(number)}')
    die_face_two.pack()

def diceback():
    dice_wind_one.withdraw()
    dice_wind_two.withdraw()
    main.deiconify()

def rps_select():
    main.withdraw()
    rps_wind.deiconify()

def main_screen():
    rps_wind.withdraw()
    main.deiconify()

def paint_select():
    main.withdraw()
    paint_wind.deiconify()

def update_msg(x):
    ans = x
    msg['text'] = str(ans)


def update_user_score():
    score = int(user_score['text'])
    score += 1
    user_score['text'] = str(score)

def update_comp_score():
    score = int(comp_score['text'])
    score += 1
    comp_score['text'] = str(score)

def check_winner(player, comp):
    if player == comp:
        update_msg("IT iss a drawww!!")
    elif player == 'rock':
        if comp == 'paper':
            update_msg("Youu looose BOYYY!")
            update_comp_score()
        else:
            update_msg("Youu win BOYYY!")
            update_user_score()
    elif player == 'paper':
        if comp == 'sissor':
            update_msg('Youu looose BOYYY!')
            update_comp_score()
        else:
            update_msg('Youu win BOYYY!')
            update_user_score()
    elif player == 'sissor':
        if comp == 'rock':
            update_msg('Youu looose BOYYY!')
            update_comp_score()
        else:
            update_msg('Youu win BOYYY!')
            update_user_score()
    else:
        pass


choices = ['rock', 'paper', 'sissor']
def update_choice(x):
    comp_choice = choices[randint(0,2)]
    if comp_choice == 'rock':
        comp_label.configure(image=rock_img_comp)
    elif comp_choice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    if x == 'rock':
        user_label.configure(image=rock_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    check_winner(x, comp_choice)


main = Tk()
main.title('Mini Games')
main.geometry("650x200+400+100")
main.configure(background='#ffffff')
main.resizable(width=False, height=False)

btn_dice = Button(main, text="Dice Simulator", width=15, font=('Corbel Light', 18), command=dice_select)
btn_rps = Button(main, text="Rock Paper Sissors", width=15, font=('Corbel Light', 18), command=rps_select)
btn_paint = Button(main, text="Paint", width=15, font=('Corbel Light', 18), command=paint_select)

btn_dice.place(x=230, y=70)
btn_rps.place(x=20, y=70)
btn_paint.place(x=440, y=70)



dice_wind_select = Toplevel(main)
dice_wind_select.title("Dice Simulator")
dice_wind_select.geometry("450x150+400+100")
dice_wind_select.configure(background='#ffffff')
dice_wind_select.resizable(width=False, height=False)

info = Label(dice_wind_select, text='Select number of Dice', font=('Corbel Light', 20), bg="#ffffff")
dice_roll_one = Button(dice_wind_select, text = "One", width=10, font = ('Corbel Light', 18), command = dice_select_one)
dice_roll_two = Button(dice_wind_select, text = 'Two', width=10, font = ('Corbel Light', 18), command = dice_select_two)

info.place(x=100, y=10)
dice_roll_one.place(x=75, y=70)
dice_roll_two.place(x=235, y=70)
dice_wind_select.withdraw()




dice_wind_one = Toplevel(main)
dice_wind_one.title("Dice Simulator")
dice_wind_one.geometry("500x400+400+100")
dice_wind_one.resizable(width=False, height=False)

die_face_one = Label(dice_wind_one, text='', font=('Helvetica', 200))
dice_roll_one = Button(dice_wind_one, text = "Roll", width=10, font = ('Corbel Light', 18), command = roll_one)
dice_back_one = Button(dice_wind_one, text = 'Back', width=10, font = ('Corbel Light', 18), command = diceback)

dice_roll_one.place(x=85, y=300)
dice_back_one.place(x=270, y=300)
dice_wind_one.withdraw()




dice_wind_two = Toplevel(main)
dice_wind_two.title("Dice Simulator")
dice_wind_two.geometry("500x400+400+100")
dice_wind_two.resizable(width=False, height=False)

die_face_two = Label(dice_wind_two, text='', font=('Helvetica', 200))
dice_roll_two = Button(dice_wind_two, text = "Roll", width=10, font = ('Corbel Light', 18), command = roll_two)
dice_back_two = Button(dice_wind_two, text = 'Back', width=10, font = ('Corbel Light', 18), command = diceback)

dice_roll_two.place(x=85, y=300)
dice_back_two.place(x=270, y=300)
dice_wind_two.withdraw()



rps_wind = Toplevel(main)
rps_wind.title('Rock Paper Sissors')
rps_wind.configure(background='#ffffff')
rps_wind.resizable(width=False, height=False)


# adding pictures
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("sissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("sissors.png"))


user_label = Label(rps_wind, image=scissor_img, bg="#ffffff")
comp_label = Label(rps_wind, image=scissor_img_comp, bg="#ffffff")
user_score = Label(rps_wind, text=0, font=100, bg = '#ffffff')
comp_score = Label(rps_wind, text=0, font=100, bg = '#ffffff')
user_indicator = Label(rps_wind, text='USER', font=50, bg="#ffffff").grid(row=0, column=1)
comp_indicator = Label(rps_wind, text='COMPUTER', font=50, bg="#ffffff").grid(row=0, column=3)
rock = Button(rps_wind, text='ROCK', width=20, height=2, bg = '#99154e', fg='white', command= lambda: update_choice('rock'))
paper = Button(rps_wind, text='PAPER', width=20, height=2, bg = '#f98404', fg='white', command= lambda: update_choice('paper'))
sissor = Button(rps_wind, text='SCISSORS', width=20, height=2, bg = '#185adb', fg='white', command= lambda: update_choice('sissor'))
back = Button(rps_wind, text="BACK", width=10, height=2, bg = '#706c61', fg='white', command= main_screen)
msg = Label(rps_wind, text = '', font=50, bg="#ffffff")
msg.grid(row=3, column=2)

comp_label.grid(row=1, column=4)
user_label.grid(row=1, column=0)
user_score.grid(row=1, column=1)
comp_score.grid(row=1, column=3)
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
sissor.grid(row=2, column=3)
back.grid(row=2, column=4)

rps_wind.withdraw()

current_x, current_y = 0,0
color = 'black'
def locate_xy(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y

def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), fill=color)
    current_x, current_y = event.x, event.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()

def save_canvas():
    try:
        file = filedialog.asksaveasfile(initialdir = 'C:/',defaultextension = '.jpg')
        ImageGrab.grab().crop((480, 180, 1300, 600)).save(file)
        messagebox.showinfo('Save successful', 'IMAGE SAAAVEDD BOYYY!')
    except:
        messagebox.showinfo('Error', 'Image Not saved')

def canvas_to_main():
    paint_wind.withdraw()
    main.deiconify()

paint_wind = Toplevel(main)
paint_wind.title("Paint")
paint_wind.state('zoomed')
paint_wind.geometry("900x500+400+100")

#paint_wind.resizable(width=False, height=False)

paint_wind.rowconfigure(0, weight = 1)
paint_wind.columnconfigure(0, weight=1)

menubar = Menu(paint_wind)
paint_wind.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)


canvas = Canvas(paint_wind, background='white')
canvas.grid(row=0,column=0, sticky='nsew')
canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)
canvas_back = Button(paint_wind, text='Back', width= 5, bg = '#99154e', fg='white', command= canvas_to_main)
canvas_back.place(x= 10, y=300)
canvas_save = Button(paint_wind, text='Save', width= 5, bg = '#f98404', fg='white', command= save_canvas)
canvas_save.place(x= 10, y=330)

def display_pallete():
    id = canvas.create_rectangle((10,10, 30, 30), fill='black')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('black'))

    id = canvas.create_rectangle((10, 40, 30, 60), fill='gray')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('gray'))

    id = canvas.create_rectangle((10,70, 30, 90), fill='brown4')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('brown4'))

    id = canvas.create_rectangle((10,100, 30, 120), fill='red')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('red'))

    id = canvas.create_rectangle((10,130, 30, 150), fill='orange')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('orange'))

    id = canvas.create_rectangle((10,160, 30, 180), fill='yellow')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('yellow'))

    id = canvas.create_rectangle((10,190, 30, 210), fill='green')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('green'))

    id = canvas.create_rectangle((10,220, 30, 240), fill='blue')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('blue'))

    id = canvas.create_rectangle((10,250, 30, 270), fill='purple')
    canvas.tag_bind(id, '<Button-1>', lambda x:show_color('purple'))

display_pallete()


paint_wind.withdraw()



main.mainloop()