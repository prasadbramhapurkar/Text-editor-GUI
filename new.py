from tkinter import *
from tkinter import ttk,colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab

class main:
    def __init__(self,master):
        self.master = master
        self.master.title("Prasad Paint Application")
        self.master.geometry("600x600")
        self.bg_color = "white"
        self.fg_color = "black"
        self.penwidth = 5
        self.old_x = None
        self.old_y = None
        self.ereser_color = "white"
        self.widgets()

        self.color_frame = LabelFrame(self.master,text = "Colors",bd = 5,relief = SUNKEN,font = "arial 15",padx = 2)
        self.color_frame.place(x=1,y=5,width = 350,height = 105)

        colors = ["black",'red',"violet","yellow","pink","crimson","green","purple","white","orange","blue","maroon","indigo","gold","brown","beige","pink","red","green"]
        i=j=0
        for color in colors:
            Button(self.color_frame,bg = color,bd = 5,relief = SUNKEN,command = lambda col = color:self.select_color(col),padx = 9,pady = 2).grid(row = i,column = j,ipadx = 2)
            j += 1
            if j == 9:
               j = 0
               i = 1

        self.canvus = Canvas(self.master,width = 1520,height = 680,bd = 5,relief = RIDGE,bg = self.bg_color)
        self.canvus.place(x = 0,y = 110)
        self.canvus.bind("<B1-Motion>",self.Paint)
        self.canvus.bind("<ButtonRelease-1>",self.reset)
        
    
        self.pen_size_frame = LabelFrame(self.master,text = "Size",bd = 5,relief = SUNKEN,font = "arial 15")
        self.pen_size_frame.place(x = 400,y = 1,height = 105,width = 400)

        self.slider = Scale(self.pen_size_frame,from_=0,to = 100,command = self.change_pen_width,orient = HORIZONTAL,length = 370)
        self.slider.set(self.penwidth)
        self.slider.grid(row = 3,column = 3)

        self.ereser_button = Button(self.master,text = "Ereser",bd = 7,relief = SUNKEN,bg = "gray",command = self.ereser,width = 15,padx = 5)
        self.ereser_button.place(x = 840,y = 50)

        self.clear_button = Button(self.master,text = "Clear",bd = 7,relief = SUNKEN,bg = "gray",command = self.clear,width = 15,padx = 5)
        self.clear_button.place(x = 1000,y = 50)

        self.canvus_button = Button(self.master,text = "Canvus",bd = 7,relief = SUNKEN,bg = "gray",command = self.change_bg,width = 15,padx = 5)
        self.canvus_button.place(x = 1165,y = 50)

        self.exit_button = Button(self.master,text = "Exit",bd = 7,relief = SUNKEN,bg = "gray",command = self.master.destroy,width = 15,padx = 5)
        self.exit_button.place(x = 1335,y = 50)
    
    def ereser(self):
           self.fg_color = self.ereser_color

    def select_color(self,col):
        self.fg_color = col

    def Paint(self,event):
        if self.old_y and self.old_x:
            self.canvus.create_line(self.old_x,self.old_y,event.x,event.y,smooth = True,capstyle = ROUND,fill = self.fg_color,width = self.penwidth)
        self.old_x = event.x
        self.old_y = event.y
    
    def reset(self,event):
        self.old_x = None
        self.old_y = None
    
    def clear(self):
        self.canvus.delete(ALL)
    
    def change_bg(self):
        self.bg_color = colorchooser.askcolor(color = self.bg_color)[1]
        self.msg = messagebox.askquestion('You want to change Background Color?','If you change the Background/canvus color then your drawing wiil be automatically clear.')
        
        if self.msg == "yes":
            self.canvus['bg'] = self.bg_color
            self.ereser_color = self.bg_color
            self.fg_color = "black"
            self.clear()
        else:
            pass
    
    def change_fg(self):
        self.fg_color = colorchooser.askcolor(color=self.fg_color)[1]

    def change_pen_width(self,e):
        self.penwidth = e

    def widgets(self):
        menu = Menu(self.master)
        self.master.config(menu = menu)
        optionmenu = Menu(menu,tearoff = 0)
        colormenu = Menu(menu,tearoff = 0)
        menu.add_cascade(label = "Colors",menu = colormenu)
        colormenu.add_command(label = "Backgroung Color",command = self.change_bg)
        colormenu.add_command(label = "Brush Color",command = self.change_fg)
        menu.add_cascade(label = "Options",menu = optionmenu)
        optionmenu.add_command(label = "Clear Canvus",command = self.clear)
        optionmenu.add_separator()
        optionmenu.add_command(label = "Exit",command = self.master.destroy)


if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()