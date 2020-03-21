from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import*
import os
from tkinter.colorchooser import askcolor

class Paint(object):
    
    DEFAULT_COLOR = 'black'
    DEFAULT_PEN_SIZE = 5.0
    def __init__(self):
        self.root=Tk()
        self.root.title("My Paint")
        self.root.iconbitmap('C:/Users/hp/Downloads/Dtafalonso-Modern-Xp-ModernXP-32-Filetype-Paint.ico')
        self.root.geometry("644x788")
                
        self.pen_btn=Button(self.root,text="pen",command=self.use_pen)
        self.pen_btn.grid(row=0,column=0)
                
        self.brush_btn=Button(self.root,text="brush",command=self.use_brush)
        self.brush_btn.grid(row=0,column=1)
                        
        self.eraser_btn=Button(self.root,text="eraser",command=self.use_eraser)
        self.eraser_btn.grid(row=0,column=2)
                        
        self.color_btn=Button(self.root,text="color",command=self.choose_color)
        self.color_btn.grid(row=0,column=3)
                        
        self.size =Scale(self.root,from_=0,to=150,orient=HORIZONTAL)
        self.size.grid(row=0,column=4)
                
        self.canvass=Canvas(self.root,bg='white',width=600,height=600)
        self.canvass.grid(row=1,columnspan=5)

        #creating menu bar
        MenuBar=Menu(self.root)
        
        
        optionsMenu=Menu(MenuBar)
        optionsMenu.add_command(label="clear",command=self.clear)
        optionsMenu.add_command(label="exit",command=self.quitApp)
        MenuBar.add_cascade(label="options",menu=optionsMenu)

        HelpMenu=Menu(MenuBar)
        HelpMenu.add_command(label="About",command=self.About)
        MenuBar.add_cascade(label="help",menu=HelpMenu)

        self.setup()
        self.root.config(menu=MenuBar)
        self.root.mainloop()
        

    def setup(self):
        self.old_x=None
        self.old_y=None
        self.line_width= self.size.get()
        self.color=self.DEFAULT_COLOR
        self.eraser_on=False
        self.active_button=self.pen_btn
        self.canvass.bind('<B1-Motion>',self.paint)
        self.canvass.bind('<ButtonRelease-1>',self.reset)
        
    def clear(self):
        self.canvass.delete(ALL)
    def quitApp(self):
        self.root.destroy()
    def About(self):
        showinfo("My-Paint","By Vanishree Desai - 2020")
    
    def use_pen(self):
        self.activate_btn(self.pen_btn)
        
    def use_brush(self):
        self.activate_btn(self.brush_btn)

    def use_eraser(self):
        self.activate_btn(self.eraser_btn,eraser_mode=True)

    def choose_color(self):
        self.eraser_on=False
        self.color=askcolor(color=self.color)[1]
        
    def activate_btn(self,giv_btn,eraser_mode=False):
        self.active_button.config(relief=RAISED)  #currently pressed button
        giv_btn.config(relief=SUNKEN) #button which is pressed just now
       
        self.active_button=giv_btn
        self.eraser_on=eraser_mode
        


    def paint(self,event):
        self.line_width= self.size.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvass.create_line(self.old_x,self.old_y,event.x,event.y,width=self.line_width,fill=paint_color,capstyle=ROUND,smooth=TRUE,splinesteps=36)
        self.old_x=event.x
        self.old_y=event.y

        
    def reset(self,event):
        self.old_x,self.old_y=None,None
    


if __name__=='__main__':
    Paint()
    
    
    


    



    



