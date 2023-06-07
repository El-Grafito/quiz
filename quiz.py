import tkinter as tk
from csv import *
from tkinter import messagebox
from tkinter import ttk
w = tk.Tk()
w.title('Quiz')
w.iconbitmap('icon3.png') #Думаю эта иконка лучше
w.geometry('435x700')
w.resizable(0,0)
result={'Имя':'','Счет':0,'Оценка игры':''}
def quit():
    a = messagebox.askyesno(title='Тест на бессердечность',message='Вы действительно хотите выйти? Вы хотите взять на себя ответственность за разбитое сердце создателя этого квиза? Вы настолько жестоки? Если да то автор квиза не берет ответственность за ваши бессоные ночи, причиной которых будет являтся ваши раздумия о вашей же жестокости, о том кем вы стали, о том насколько низко вы пали, о том что вы не прошли этот квиз полностью. А еще результаты этой игры не сохранятся.')
    if a==True:
        w.destroy()
def quit2(x,y):
    a = messagebox.askyesno(title='Тест на преданност',message='Еще раз спасибо за игру:) Вы действительно хотите выйти?')
    if a==True:
        result['Имя']=x.get()
        result['Оценка игры']=y.get()
        with open('result.txt','a',encoding='utf-8') as f:
            f.write(f'Имя: {result["Имя"]} \nCчет: {str(result["Счет"])} \nОценка игры: {str(result["Оценка игры"])}\n\n\n')
        w.destroy()
quitt = tk.Button(text='Выйти',font=('Roboto',15),bg='red',command=quit)
quitt.place(x=0,y=660)
field={'Python':['200','300','400','500'],'География':['200','300','400','500'],'Разное':['200','300','400','500'],'Миллионеры':['200','300','400','500'],'История':['200','300','400','500']}
che=[0] # тут по идее должны быть цифра и кода сумма этих цифер вроде бы станет 25 или не помню сколько, крч игра должна закончится
question = tk.Label(text='',font=('Roboto',15),wraplength=430)
question.place(x=0,y=300)
bal=tk.Label(text='Ваш счет: 0',font=('Roboto',15))
bal.place(x=0,y=250)
otl=[] #тут находятся варианты ответов. Не знаю для чего нужно. Но код работает так что не трону
aa=[] #очень нужная переменная, без нее не работает. Не спрашивай у меня почему она нужна, я уже успел забыть его предназначение
vop=[] #Тут находятся все словари из урана которых уже выбрали. Да я даю непонятные названия переменным
cnt=[] #А тут кнопки отвечающие за предидущую штуку cnt+vop=любоф
gqw=[] #Еще один словарь который тоже нужен чтобы чтото сохранить чтобы им потом воспользовалась какаято функция и кинул его на вечнось. Маленький элемент кода который чувствует себя не нужным. Крч тут кнопки ответов
rr=[]
def prov(c):
    if gqw.index(c)==int(vop[-1]['cor']):
        c.config(bg='green',fg='white')
        cnt[-1].config(bg='green',fg='white',state='disabled')
        for i in gqw:
            i.config(state='disabled')
        for i in aa:
            i.config(state='normal')
        result['Счет']=(result['Счет']+int(vop[-1]['ball']))
        bal.config(text=('Ваш счет: '+str(result['Счет'])))
    else:
        c.config(bg='red',fg='white')
        gqw[int(vop[-1]['cor'])].config(bg='green',fg='white')
        cnt[-1].config(bg='red',fg='white')
        for i in gqw:
            i.config(state='disabled')
        for i in aa:
            i.config(state='normal')
    che.append(1)
    if sum(che)==20:
        a=messagebox.askyesno(title='Зе енд',message='Вы ответили на все вопросы. Хотите завершить игру? Если нет то в любой мoмент можете завершить игру с помощю кнопки "Завершить игру"')
        if a==True:
            end(enda)
def funk(x,y,bt): #Эта функция делает много чего. Находит вопрос, сохраняет вопрос, чернит кнопку, помогает при боли суставов, помогает при головной боли, уничтожает вредителей и насекомых, помогает при бессонице, уничтажает врагов, проходит Калофдйюти за тебя, сдает экзамены и тд.bt.configure(state='disabled',bg='#000000')
    if sum(che)==0:
        for i in ['A','B','C','D']: #какойто цикл
            ot = tk.Button(text=i,font=('Roboto',15))
            ot.place(x=0,y=390+(50*(['A','B','C','D'].index(i))))
            gqw.append(ot)
            otv=tk.Label(text='',font=('Roboto',15))
            otv.place(x=35,y=395+(50*(['A','B','C','D'].index(i))))
            otl.append(otv)
        for i in gqw:
            i.config(command=lambda c=i: prov(c))
    bt.config(state='disabled',bg='black')
    aa.remove(bt)
    for i in aa:
        i.config(state='disabled')
    for i in gqw:
        i.config(state='normal',bg='white',fg='black')
    cnt.append(bt)
    with open('uran.csv','r',encoding='utf-8') as f:
        for i in DictReader(f,delimiter=';',fieldnames=['class','ball','task','0','1','2','3','cor']):
            if i['class']==x and i['ball']==y:
                vop.append(i)
                question.config(text=i['task'],justify=tk.LEFT)
                for e in otl:
                    e.config(text=i[str(otl.index(e))])
for k,v in field.items(): #Этот цикл тоже топчик. Создает игровое поле. Хороший челик
    btk=tk.Button(text=k,width=11,height=3)
    btk.grid(row=1,column=list(field.keys()).index(k))
    rr.append(btk)
    for i in v:
        btv=tk.Button(text=i,width=11,height=2)
        btv.grid(row=(v.index(i))+2,column=list(field.keys()).index(k))
        aa.append(btv)
for i in aa: #Этот цикл я написал когда сидел на уроке. Было сложно додуматся но я включил всеь свой математический гении и решил эту непостижимую задачу. Крч цикл задает команды кнопкам. Почему нельзя было задать прямо на крутой функции? Потому что НАЗВАНИЯ КНОПОК!!!
    i.config(command=lambda x=list(field.keys())[(aa.index(i))//4],y=field[list(field.keys())[(aa.index(i))//4]][(aa.index(i))%4],bt=i:funk(x,y,bt))
def end(c):
    for i in [aa,cnt,gqw,rr,otl]:
        def popp(x):
            for e in x:
                e.destroy()
        popp(i)
    c.destroy()
    question.destroy()
    tht=tk.Label(text='Спасибо что прошли квиз. Теперь пожалуисто введите следующие данные. Все результаты можете посмотреть в файле result.txt',font=('Roboto',15),wraplength=430,justify=tk.CENTER)
    tht.pack()
    name=tk.Label(text='Имя',font=('Roboto',15))
    name.place(x=0,y=300)
    namee=tk.Entry(font=('Roboto',15))
    namee.place(x=50,y=300)
    vrt=tk.Label(text='Оцените квиз',font=('Roboto',15))
    vrt.place(x=0,y=350)
    c=ttk.Combobox()
    c['values']=(1,2,3,4,5,6,7,8,9,10)
    c.current(9)
    c.place(x=135,y=355)
    quitt.config(command=lambda:quit2(namee,c))
def psevend():
    a=messagebox.askyesno(title='ъуъ',message='Вы действительно хотите завершить игру?')
    if a==True:
        end(enda)
enda=tk.Button(text='Завершить игру',font=('Roboto',15),bg='red',command=psevend)
enda.place(x=272,y=660)
w.mainloop()
