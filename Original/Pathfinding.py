import tkinter,threading#,base64,time,winsound,random,sys,os,ast
#from tkinter import messagebox,filedialog
#from ctypes import windll,byref,create_unicode_buffer,create_string_buffer
GWL_EXSTYLE=-20
WS_EX_APPWINDOW=0x00040000
WS_EX_TOOLWINDOW=0x00000080
def set_appwindow(root):
    hwnd = windll.user32.GetParent(root.winfo_id())
    style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())
    
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str): 
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)
class AStar:
    class Node:
        def __init__(self,node,g,h,parent=None):
            self.node=node
            self.h=h
            self.g=g
            self.parent=parent
        def __getattr__(self,name):
            return {"h":self.h,"g":self.h,"f":self.h+self.g}[name]
        def __eq__(self,other):
            if type(other) == AStar.Node:
                return self.node==other.node
            else:
                return self.node==other
        def __str__(self):
            if self.parent:
                return "node:{} f:{} g:{} h:{} parent:{}".format(self.node,self.f,self.g,self.h,self.parent.node)
            else:
                return "node:{} f:{} g:{} h:{} parent:{}".format(self.node,self.f,self.g,self.h,self.parent)
class Mathf:
    def Clamp(value,minimum,maximum):
        return min(max(value,minimum),maximum)
class tools:
    class Grid:
        def getNeighbours(node):
            neighbours=[]
            for _x in range(-1,2):
                for _y in range(-1,2):
                    if (_x,_y) == (0,0):
                        continue
                    neighbours.append((node[0]+_x,node[1]+_y))
            return neighbours
        def getDistance(nodeA,nodeB):
            distX = abs(nodeA[0]-nodeB[0])
            distY = abs(nodeA[1]-nodeB[1])
            if (distX>distY):
                return 14*distY+10*(distX-distY)
            return 14*distX+10*(distY-distX)
    class GeneratorOBJ:
        def __init__(self,generator,length):
            self.generator=generator
            self.length = length
        def __len__(self):
            return self.length
        def __iter__(self):
            return self.generator
    def insertCharBefore(origin,char,buffer):
        return("{}{}".format(char*(buffer-len(str(origin))),str(origin)))
    def insertCharAfter(origin,char,buffer):
        return("{}{}".format(str(origin),char*(buffer-len(str(origin)))))
    def insertDecimalPoint(origin,points):
        return("{}{}".format(str(origin),"0"*(points-(len(str(origin).split(".")[-1])))))
    def loadingPercentageString(iterable):
        for index,item in enumerate(iterable):
            percentage=((index+1)*100)/len(iterable)
            yield (tools.insertCharBefore(tools.insertDecimalPoint(percentage,2),"0",6),item)
    def loadingPercentageFloat(iterable):
        for index,item in enumerate(iterable):
            percentage=((index+1)*100)/len(iterable)
            yield (percentage,item)
    def loadingPercentageGenString(generator):
        for index,item in enumerate(generator):
            percentage=((index+1)*100)/generator.length
            yield (tools.insertCharBefore(tools.insertDecimalPoint(percentage,2),"0",6),item)
    def loadingPercentageGenFloat(generator):
        for index,item in enumerate(generator):
            percentage=((index+1)*100)/generator.length
            yield (percentage,item)
    def loadModules():
        global messagebox
        from tkinter import messagebox
        yield "."
        global base64
        try:
            import base64
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        global time
        try:
            import time
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global winsound
        try:
            import winsound
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global random
        try:
            import random
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        global sys
        try:
            import sys
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global ast
        try:
            import ast
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global filedialog
        try:
            from tkinter import filedialog
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global os
        try:
            import os
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global windll
        try:
            from ctypes import windll
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        
        global byref
        try:
            from ctypes import byref
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        
        global create_unicode_buffer
        try:
            from ctypes import create_unicode_buffer
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        
        global create_string_buffer
        try:
            from ctypes import create_string_buffer
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        try:
            loadfont("Interface/Fonts/BebasNeue.otf")
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Fonts","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global Image
        try:
            from PIL import Image
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
        time.sleep(0.1)
        global ImageTk
        try:
            from PIL import ImageTk
        except Exception as detectedException:
            messagebox.showinfo("Error Loading Module","It appears an error has occured:\n{}".format(detectedException))
        yield "."
    def getGridFromAStarFileDir(directory):
        print(directory)
        if len(directory.split("."))>0:
            if directory.split(".")[-1]=="astar":
               with open(directory,"rb") as binfile:
                   contents=((base64.b64decode(binfile.read())).decode("utf-8","ignore"))
                   #contents=binfile.read()
                   return contents
    def saveGridToAStarFileDir(directory,grid):
        with open(directory,"wb") as binfile:
            binfile.write(base64.b64encode((str(grid).encode("utf-8","ignore"))))
class loadWindow(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#ffffff')
        self.master.title("GOL Load")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=450
        self.h=225
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/LOADING/Active.gif"),tkinter.PhotoImage(file="Interface/GIF/LOADING/Inactive.gif")]
        self.inactive = tkinter.Label(self.master,image=self.images[1],background="#FFFFFF")
        self.inactive.place(x=0,y=0)
        
        self.progressBar=tkinter.Frame(self.master,height=225,width=int(0),background="#1D60A7",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.active = tkinter.Label(self.progressBar,image=self.images[0],background="#FFFFFF",borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.active.place(x=3,y=2)
        self.progressBar.place(x=0,y=0)

        self.loadmodules()
    def loadmodules(self,*args):
        self.completion=0
        threading.Thread(target=self.percentStart).start()
        self.checkForPercent()
    def percentStart(self):
        for a,b in tools.loadingPercentageGenFloat(tools.GeneratorOBJ(tools.loadModules(),15)):
            self.completion = a
        return 
    def cancel(self):
        self.master.destroy()
    def checkForPercent(self):
        if self.completion < 100:
            self.progressBar.config(width=int((self.completion/100)*450))
            self.master.after(50,self.checkForPercent)
        else:
            self.progressBar.config(width=450)
            self.cancel()
appLoad=loadWindow(tkinter.Tk())
appLoad.mainloop()
#windows
class window(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        self.deltanode = ""
        self.gridnodes={}
        self.obstacles=[]
        self.path=[]
        self.prev_path=[]
        self.postcalc=False
        self.locked = False
        
        self.target=(24,14)
        self.start=(15,14)
        
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#D4D4D4')
        self.master.bind("<Escape>",self.cancel)
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Unactive/Calculate.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Active/Calculate.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Save.gif"),tkinter.PhotoImage(file="Interface/GIF/UNACTIVE/Save.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Active/Information.gif"),tkinter.PhotoImage(file="INTERFACE/GIF/Alert.gif")]
        self.master.title("Pathfinding")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w1=475
        self.h1=300
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w1/2)
        self.y1=(self.hs/2)-(self.h1/2)
        
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF",bd=0,highlightthickness=0)
        self.drag.place(x=400,y=75)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)
        
        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0,highlightthickness=0)
        self.close.place(x=400,y=0,height=75,width=75)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<ButtonPress-3>", self.closepress2)
        self.close.bind("<ButtonRelease-3>", self.closeunactive2)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)
        
        self.information = tkinter.Label(self.master,image=self.images[4],background="#FFFFFF",bd=0,highlightthickness=0)
        self.information.place(x=400,y=150)
        self.informationactive = False
        self.information.bind("<ButtonPress-1>", self.informationpress)
        self.information.bind("<ButtonRelease-1>", self.informationunactive)
        self.information.bind("<ButtonPress-3>", self.informationpress2)
        self.information.bind("<ButtonRelease-3>", self.informationunactive2)
        self.information.bind("<Enter>",self.informationhighlight)
        self.information.bind("<Leave>",self.informationunhighlight)

        self.save = tkinter.Label(self.master,image=self.images[7],background="#FFFFFF",bd=0,highlightthickness=0)
        self.save.place(x=400,y=225)
        self.saveactive = False
        self.save.bind("<ButtonPress-1>", self.savepress)
        self.save.bind("<ButtonRelease-1>", self.saveunactive)
        self.save.bind("<ButtonPress-3>", self.savepress2)
        self.save.bind("<ButtonRelease-3>", self.saveunactive2)
        self.save.bind("<Enter>",self.savehighlight)
        self.save.bind("<Leave>",self.saveunhighlight)

        self.progressBuffer={"filedir":"INTERFACE/GIF/LOADING/Buffer.gif"}
        self.progressBuffer["canvas"] = tkinter.Canvas(self.master,height=75,width=75,bd=0,highlightthickness=0,bg="#FFFFFF")
        self.progressBuffer["image"] = Image.open(self.progressBuffer["filedir"]).convert("RGBA")
        self.progressBuffer["angle"]=0
        self.progressBuffer["tkImage"]=ImageTk.PhotoImage(self.progressBuffer["image"].rotate(self.progressBuffer["angle"],expand=1))
        self.progressBuffer["canvas_obj"] = self.progressBuffer["canvas"].create_image(38, 38, image=self.progressBuffer["tkImage"])
        
        self.master.geometry('%dx%d+%d+%d' % (self.w1,self.h1,self.x,self.y1))
        
        self.griddisplay = tkinter.Canvas(self.master,height=300,width=400,bd=0,highlightthickness=0)
        for xiter in range(40):
            for yiter in range(30):
                x=(xiter*10)+1
                y=yiter*10
                points=[x,y,x+9,y,x+9,y+9,x,y+9]
                self.gridnodes[(xiter,yiter)]=self.griddisplay.create_polygon(points, outline="",fill=["#D4D4D4","#0F3156"][(xiter,yiter) in self.obstacles])
                self.griddisplay.tag_bind(self.gridnodes[(xiter,yiter)],"<ButtonPress-1>",lambda event,arg=(xiter,yiter): self.togglenode(arg))
                self.griddisplay.tag_bind(self.gridnodes[(xiter,yiter)],"<ButtonRelease-1>",self.unactivetogglednode)
                self.griddisplay.tag_bind(self.gridnodes[(xiter,yiter)],"<ButtonPress-2>",self.settarget)
                self.griddisplay.tag_bind(self.gridnodes[(xiter,yiter)],"<Shift-ButtonPress-2>",self.setstart)
        self.griddisplay.itemconfig(self.gridnodes[self.start],fill="#15477C")
        self.griddisplay.itemconfig(self.gridnodes[self.target],fill="#216DBE")
        
        self.griddisplay.bind("<B2-Motion>",self.settarget)
        self.griddisplay.bind("<Shift-B2-Motion>",self.setstart)
        self.griddisplay.bind("<B1-Motion>",self.dragactivenode)
        self.griddisplay.bind("<B3-Motion>",self.dragunactivenode)
        self.griddisplay.bind("<ButtonPress>",self.resetPostCalculation)
        self.griddisplay.bind("<ButtonRelease>",self.resetPostCalculationRelease)
        self.griddisplay.place(x=0,y=0)
        
        self.failAlert=tkinter.Label(self.master,image=self.images[-1],background="#FFFFFF",bd=0,highlightthickness=0)
        self.failAlertActive=False
    def resetPostCalculation(self,*args):
        if self.postcalc:
            threading.Thread(target=self.popon).start()
            self.griddisplay.config(background="#257BD6")
            if self.failAlertActive:
                self.failAlert.place_forget()
                self.failAlertActive=False
    def resetPostCalculationRelease(self,*args):
        if self.postcalc:
            self.griddisplay.config(background="#FFFFFF")
            self.locked=False
            self.postcalc=False
            threading.Thread(target=self.updateDisplay()).start()
    def animateBuffer(self):
        self.progressBuffer["canvas"].delete(self.progressBuffer["canvas_obj"])
        self.progressBuffer["angle"]+=5
        self.progressBuffer["angle"]%=360
        self.progressBuffer["tkImage"]=ImageTk.PhotoImage(self.progressBuffer["image"].rotate(self.progressBuffer["angle"],expand=1))
        self.progressBuffer["canvas_obj"] = self.progressBuffer["canvas"].create_image(38, 38, image=self.progressBuffer["tkImage"])
    def savehighlight(self,*args):
        if self.saveactive==False:
            self.save.config(background="#D4D4D4")
    def saveunhighlight(self,*args):
        if self.saveactive==False:
            self.save.config(background="#FFFFFF")
    def savepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.save.config(background='#1D60A7',image=self.images[6])
        self.saveactive=True
    def saveunactive(self,*args):
        self.save.config(background='#D4D4D4',image=self.images[7])
        self.saveactive=False
        self.saveAStarFile()
    def savepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.save.config(background='#1D60A7',image=self.images[6])
        self.saveactive=True
    def saveunactive2(self,*args):
        self.save.config(background='#D4D4D4',image=self.images[7])
        self.saveactive=False
        self.openAStarFile()

    def openAStarFile(self,*args):
        fileDir = filedialog.askopenfilename(filetypes=(("A* files","*.astar"),("All files", "*.*") ))
        if fileDir:
            try:
                grid=tools.getGridFromAStarFileDir(fileDir).split("|")
                self.start=ast.literal_eval(grid[0])
                self.target=ast.literal_eval(grid[1])
                self.obstacles=ast.literal_eval(grid[2])
                self.updateDisplay()
            except Exception as detectedError:
                if messagebox.askyesno("Error",message="ERROR OPENING GRID:\n{}\nOpen again?".format(detectedError)):
                    self.openAStarFile()
    def saveAStarFile(self,*args):
        fileDir = filedialog.asksaveasfilename(filetypes=(("A* files","*.astar"),("All files", "*.*") ))
        if fileDir:
            try:
                if not fileDir.endswith(".astar"):
                    fileDir="{}.astar".format(fileDir)
                tools.saveGridToAStarFileDir(fileDir,"{}|{}|{}".format(str(self.start),str(self.target),str(self.obstacles)))
            except Exception as detectedError:
                if messagebox.askyesno("Error",message="ERROR SAVING GRID:\n{}\nSave again?".format(detectedError)):
                    self.saveAStarFile()
                    
    def settarget(self,event):
        if not self.locked:
            threading.Thread(target=self.popon).start()
            x=(event.x-1)//10
            y=(event.y)//10
            node=(x,y)
            if (0<=x<40) and (0<=y<30):
                if node!=self.start:
                    if node in self.obstacles:
                        self.obstacles.remove(node)
                    self.griddisplay.itemconfig(self.gridnodes[self.target],fill="#D4D4D4")
                    self.target=node
                    self.griddisplay.itemconfig(self.gridnodes[self.target],fill="#216DBE")
    def setstart(self,event):
        if not self.locked:
            threading.Thread(target=self.popon).start()
            x=(event.x-1)//10
            y=(event.y)//10
            node=(x,y)
            if (0<=x<40) and (0<=y<30):
                if node!=self.target:
                    if node in self.obstacles:
                        self.obstacles.remove(node)
                    self.griddisplay.itemconfig(self.gridnodes[self.start],fill="#D4D4D4")
                    self.start=node
                    self.griddisplay.itemconfig(self.gridnodes[self.start],fill="#15477C")
    def dragactivenode(self,event):
        if not self.locked:
            x=(event.x-1)//10
            y=(event.y)//10
            node=(x,y)
            if (0<=x<40) and (0<=y<30):
                if (node not in self.obstacles) and (node not in [self.deltanode,self.start,self.target]):
                    self.obstacles.append(node)
                    self.griddisplay.itemconfig(self.gridnodes[node],fill=["#D4D4D4","#0F3156"][node in self.obstacles])
    def unactivetogglednode(self,event):
        self.deltanode=""
    def dragunactivenode(self,event):
        if not self.locked:
            x=(event.x-1)//10
            y=(event.y)//10
            node=(x,y)
            if (0<=x<40) and (0<=y<30):
                if node in self.obstacles and (node not in [self.start,self.target]):
                    self.obstacles.remove(node)
                    self.griddisplay.itemconfig(self.gridnodes[node],fill=["#D4D4D4","#0F3156"][node in self.obstacles])
    def togglenode(self,node,*args):
        if not self.locked:
            self.deltanode=node
            threading.Thread(target=self.popon).start()
            if node in self.obstacles:
                self.obstacles.remove(node)
            else:
                if (node not in [self.start,self.target]):
                    self.obstacles.append(node)
            if (node not in [self.start,self.target]):
                self.griddisplay.itemconfig(self.gridnodes[node],fill=["#D4D4D4","#0F3156"][node in self.obstacles])
    def updateDisplay(self):
        for node in self.gridnodes:
            self.griddisplay.itemconfig(self.gridnodes[node],fill=["#D4D4D4","#0F3156"][node in self.obstacles])
        self.griddisplay.itemconfig(self.gridnodes[self.start],fill="#15477C")
        self.griddisplay.itemconfig(self.gridnodes[self.target],fill="#216DBE")
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w1,self.h1,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def closepress2(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive2(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        if not self.locked:
            for node in self.obstacles:
                self.griddisplay.itemconfig(self.gridnodes[node],fill="#D4D4D4")
            self.obstacles=[]
    def informationhighlight(self,*args):
        if self.informationactive==False:
            self.information.config(background="#D4D4D4")
    def informationunhighlight(self,*args):
        if self.informationactive==False:
            self.information.config(background="#FFFFFF")
    def informationpress(self,*args):
        self.information.config(background='#1D60A7',image=self.images[5])
        threading.Thread(target=self.popon).start()
        self.informationactive=True
    def informationunactive(self,*args):
        self.information.config(background='#FFFFFF',image=self.images[4])
        self.informationactive=False
        if self.failAlertActive:
            self.failAlert.place_forget()
            self.failAlertActive=False
        self.locked=True
        self.progressBuffer["canvas"].place(x=400,y=150)
        self.update()
    def informationpress2(self,*args):
        self.information.config(background='#1D60A7',image=self.images[8])
        threading.Thread(target=self.popon).start()
        self.informationactive=True
    def informationunactive2(self,*args):
        self.information.config(background='#FFFFFF',image=self.images[4])
        self.informationactive=False
        self.spawninfo()
    def popon(self,*args):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
    def spawninfo(self):
        infowin = infowindow(tkinter.Toplevel())
        infowin.mainloop()
    def update(self):
        for node in self.prev_path:
            if self.griddisplay.itemcget(self.gridnodes[node],"fill") == "#1D60A7":
                self.griddisplay.itemconfig(self.gridnodes[node],fill="#D4D4D4")
        open_nodes=[AStar.Node(self.start,0,tools.Grid.getDistance(self.start,self.target)),]
        closed_nodes=[]
        found=False
        while open_nodes:
            self.animateBuffer()
            self.master.update()
            current=open_nodes[0]
            for node in open_nodes:
                if (node.f<current.f) or (node.f == current.f and node.h < current.h):
                    current=node
            open_nodes.remove(current)
            closed_nodes.append(current)
            
            if current.node == self.target:
                found=True
                break
            for neighbournode in tools.Grid.getNeighbours(current.node):
                self.animateBuffer()
                self.master.update()
                neighbour = AStar.Node(neighbournode,tools.Grid.getDistance(neighbournode,self.start),tools.Grid.getDistance(neighbournode,self.target),current)
                if neighbour in closed_nodes or neighbournode in self.obstacles or not (0<=neighbournode[0]<=39 and 0<=neighbournode[1]<=29):
                    continue
                newMovementCostToNeighbour = current.g+tools.Grid.getDistance(current.node,neighbournode)
                if neighbour in open_nodes:
                    if newMovementCostToNeighbour<open_nodes[open_nodes.index(neighbour)].g:
                        open_nodes[open_nodes.index(neighbour)] = neighbour
                else:
                    open_nodes.append(neighbour)
        if found:
            currentParent=current.parent
            path=[]
            while currentParent:
                if currentParent.node not in [self.start,self.target]:
                    path.append(currentParent.node)
                currentParent=currentParent.parent
            for node in path:
                self.griddisplay.itemconfig(self.gridnodes[node],fill="#1D60A7")
            self.prev_path=path
        else:
            self.failAlertActive=True
            self.failAlert.place(x=125,y=112)
            self.master.update()
        self.progressBuffer["canvas"].place_forget()
        self.postcalc=True
class infowindow(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self, master)    
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.overrideredirect(True)
        self.master.resizable(0,0)
        self.master.configure(background='#FFFFFF')
        self.master.bind("<Escape>",self.cancel)
        self.master.title("GOL Information")
        self.master.iconbitmap("Interface/ICO/Icon.ico")
        self.w=75*5
        self.h=75
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x=(self.ws/2)-(self.w/2)
        self.y=(self.hs/2)-(self.h/2)
        self.master.wm_attributes("-topmost", True)
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,self.x,self.y))
        self.images=[tkinter.PhotoImage(file="Interface/GIF/Unactive/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Drag.gif"),tkinter.PhotoImage(file="Interface/GIF/Unactive/Cancel.gif"),tkinter.PhotoImage(file="Interface/GIF/Active/Cancel.gif")]
        self.texts = [tkinter.PhotoImage(file="Interface/GIF/Message{}.gif".format(x+1)) for x in range(10)]
        self.drag = tkinter.Label(self.master,image=self.images[0],background="#FFFFFF")
        self.drag.place(x=0,y=0)
        self.dragactive = False
        self.drag.bind("<ButtonPress-1>", self.StartMove)
        self.drag.bind("<ButtonRelease-1>", self.StopMove)
        self.drag.bind("<B1-Motion>", self.OnMotion)
        self.drag.bind("<Enter>",self.draghighlight)
        self.drag.bind("<Leave>",self.dragunhighlight)

        self.close = tkinter.Label(self.master,image=self.images[2],background="#FFFFFF",bd=0,highlightthickness=0)
        self.close.place(x=75,y=0)
        self.closeactive = False
        self.close.bind("<ButtonPress-1>", self.closepress)
        self.close.bind("<ButtonRelease-1>", self.closeunactive)
        self.close.bind("<Enter>",self.closehighlight)
        self.close.bind("<Leave>",self.closeunhighlight)

        self.textsindex=0
        self.text = tkinter.Label(self.master,image=self.texts[self.textsindex],background="#FFFFFF",bd=0,highlightthickness=0)
        self.text.place(x=75*2,y=0)
        self.textactive = False
        self.text.bind("<Enter>",self.texthighlight)
        self.text.bind("<Leave>",self.textunhighlight)
        self.text.bind("<ButtonRelease-1>",self.animate)
    def texthighlight(self,*args):
        self.text.config(background="#D4D4D4")
    def textunhighlight(self,*args):
        self.text.config(background="#FFFFFF")
    def draghighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#D4D4D4")
    def dragunhighlight(self,*args):
        if self.dragactive==False:
            self.drag.config(background="#FFFFFF")
    def StartMove(self, event):
        threading.Thread(target=self.popon).start()
        self.drag.config(background='#1D60A7',image=self.images[1])
        self.dragactive = True
        self.x1 = event.x
        self.y1 = event.y
    def StopMove(self, event):
        self.drag.config(background='#D4D4D4',image=self.images[0])
        self.dragactive = False
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('%dx%d+%d+%d' % (self.w,self.h,x,y))
    def cancel(self,*args):
        self.master.destroy()
    def closehighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#D4D4D4")
    def closeunhighlight(self,*args):
        if self.closeactive==False:
            self.close.config(background="#FFFFFF")
    def closepress(self,*args):
        threading.Thread(target=self.popon).start()
        self.close.config(background='#1D60A7',image=self.images[3])
        self.closeactive=True
    def closeunactive(self,*args):
        self.close.config(background='#D4D4D4',image=self.images[2])
        self.closeactive=False
        time.sleep(0.1)
        self.cancel()
    def animate(self,*args):
        threading.Thread(target=self.popon).start()
        self.textsindex = (self.textsindex+1)%len(self.texts)
        self.text.config(image=self.texts[self.textsindex])
    def popon(self):
        sounds=['Interface/AUDIO/popoff.wav','Interface/AUDIO/pop.wav']
        winsound.PlaySound(sounds[random.randint(0,1)],winsound.SND_ASYNC)
app =window(tkinter.Tk())
set_appwindow(app.master)
app.mainloop()
