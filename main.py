

def main_gui():
    import selenium_module as SM
    import tkinter as tk
    import tkinter.messagebox
    import Jc_sequence as Jc


    Jc.booting_data()

    window = tk.Tk()
    window.geometry('800x600')
    window.title('JC Macro ver 0.1')
    window.resizable(False,False)

    def check_digit(x):
        try:
            float(x)
            return True
        except:
            return False


    def close():
        window.quit()
        window.destroy()
        print('close')
    def move_to_frame1():
        listUp()
        frame1.tkraise()
        print('move_to_frame1')
    def move_to_frame2():
        frame2.tkraise()
        frame2_1.tkraise()
        print('move_to_frame2')
    def move_to_frame2_2():
        entry2_2_1.delete(0,'end')
        frame2_2.tkraise()
        print('move_to_frame2_2')
    def move_to_frame2_3():
        entry2_3_1.delete(0, 'end')
        frame2_3.tkraise()
        print('move_to_frame2_3')
    def move_to_frame2_4():
        entry2_4_1.delete(0, 'end')
        frame2_4.tkraise()
        print('move_to_frame2_4')
    def move_to_frame2_5():
        entry2_5_1.delete(0, 'end')
        entry2_5_2.delete(0, 'end')
        entry2_5_3.delete(0, 'end')
        frame2_5.tkraise()
        print('move_to_frame2_5')
    def move_to_frame2_6():
        entry2_6_1.delete(0, 'end')
        frame2_6.tkraise()
        print('move_to_frame2_6')
    def move_to_frame2_7():
        entry2_7_1.delete(0, 'end')
        frame2_7.tkraise()
        print('move_to_frame2_7')
    def move_to_frame3():
        frame3.tkraise()
        frame3_1.tkraise()
        print('move_to_frame3')
    def move_to_frame3_2():
        entry3_2_1.delete(0, 'end')
        frame3_2.tkraise()
        print('move_to_frame3_2')
    def move_to_frame4():
        frame4.tkraise()
        frame4_1.tkraise()
        print('move_to_frame4')
    def move_to_frame5():
        frame5.tkraise()
        frame5_1.tkraise()
        print('move_to_frame5')
    def move_to_frame5_2():
        entry5_2_1.delete(0, 'end')
        frame5_2.tkraise()
        print('move_to_frame5_2')

    def confirm_address():# 주소 입력
        global listbox1

        txt=input_text2_2_1.get()
        Jc.add_sequence('주소 입력',txt,'1')
        print('confirm_address')
        move_to_frame1()

    def confirm_wait():
        global listbox1
        print('confirm_wait')
        txt=input_text2_3_1.get()
        if check_digit(txt):
            Jc.add_sequence('대기시간',txt,'2')
            move_to_frame1()

        else:
            tkinter.messagebox.showerror('에러','오류발생, 숫자를 입력하세요.')

    def confirm_elem():
        global listbox1
        global find_target

        print('confirm_elem')
        target=input_text2_4_1.get()
        type=elem_var.get()
        txt=[type,target]
        Jc.add_sequence('elem 찾기',txt,'3')
        move_to_frame1()


    def confirm_elems():
        global listbox1
        global find_target

        print('confirm_elems')
        target=input_text2_5_1.get()
        type=elems_var.get()
        start_num=input_text2_5_2.get()
        end_num=input_text2_5_3.get()
        if not start_num.isdigit() or not end_num.isdigit():
            tkinter.messagebox.showerror('에러', '인덱싱 번호를 입력하세요')
        else:
            txt=[type,target,[int(start_num),int(end_num)]]
            print(txt)
            Jc.add_sequence('elems 찾기',txt,'4')
            move_to_frame1()

    def confirm_save():
        global listbox1
        global find_target

        print('confirm_save')
        Jc.add_sequence('txt저장',0,'5')
        move_to_frame1()

    def confirm_check():
        global listbox1
        global find_target

        print('confirm_check')
        Jc.add_sequence('데이터체크',0,'6')
        move_to_frame1()

    def confirm_saveImage():
        global listbox1
        global find_target

        print('confirm_saveImage')
        txt=input_text2_6_1.get()

        Jc.add_sequence('이미지저장',txt,'5_2')
        move_to_frame1()

    def release_stack():
        global listbox1
        global find_target

        print('confirm_stack')

        Jc.add_sequence('데이터 초기화',0,'5_3')
        move_to_frame1()

    def datas_stack():
        global listbox1
        global find_target

        print('datas_stack')

        Jc.add_sequence('데이터 쌓기',0,'5_4')
        move_to_frame1()

    def confirm_repeatStart():
        global listbox1
        global find_target

        print('confirm_repeatStart')

        Jc.add_sequence('!!!!!!!!!!!!!!!!!!!!!반복시작',0,'21')
        move_to_frame1()

    def confirm_repeatStop():
        global listbox1
        global find_target

        print('confirm_repeatStop')
        txt=input_text2_7_1.get()
        Jc.add_sequence('!!!!!!!!!!!!!!!!!!!!!반복종료',txt,'22')
        move_to_frame1()

    def confirm_keyword():
        print('confirm_keyword')
        global listbox1

        txt=input_text3_2_1.get()
        Jc.add_sequence('문자 입력',txt,'7')
        move_to_frame1()

    def confirm_keyDown():
        print('confirm_keyDown')
        global listbox1

        Jc.add_sequence('Tab',0,'8')
        move_to_frame1()

    def confirm_keyUp():
        print('confirm_keyUp')
        global listbox1

        Jc.add_sequence('Space',0,'9')
        move_to_frame1()

    def confirm_enter():
        print('confirm_enter')
        global listbox1

        Jc.add_sequence('Enter', 0, '10')
        move_to_frame1()


    def confirm_click():
        print('confirm_click')
        global listbox1

        Jc.add_sequence('click', 0, '11')
        move_to_frame1()

    def confirm_doubleClick():
        print('confirm_doubleClick')
        global listbox1

        Jc.add_sequence('doubleClick', 0, '12')
        move_to_frame1()

    def confirm_moveMouse():
        print('confirm_moveMouse')
        global listbox1

        Jc.add_sequence('moveMouse', 0, '13')
        move_to_frame1()

    def confirm_hold():
        print('confirm_hold')
        global listbox1

        Jc.add_sequence('hold', 0, '14')
        move_to_frame1()

    def confirm_release():
        print('confirm_release')
        global listbox1

        Jc.add_sequence('release', 0, '15')
        move_to_frame1()

    def confirm_scrollHeight():
        print('confirm_scrollHeight')
        global listbox1

        Jc.add_sequence('스크롤 끝까지', 0, '16')
        move_to_frame1()

    def confirm_scrollTo():
        print('confirm_scrollTo')
        global listbox1
        txt=input_text5_2_1.get()
        Jc.add_sequence('얼마나 스크롤', txt, '17')
        move_to_frame1()

    def confirm_moveScroll():
        print('confirm_moveScroll')
        global listbox1

        Jc.add_sequence('elem으로 이동', 0, '18')
        move_to_frame1()

    def confirm_pageDown():
        print('confirm_pageDown')
        global listbox1

        Jc.add_sequence('pageDown', 0, '19')
        move_to_frame1()

    def confirm_scrollEnd():
        print('confirm_scrollEnd')
        global listbox1

        Jc.add_sequence('scrollEnd', 0, '20')
        move_to_frame1()


    def save_sequence():
        print('save_sequence')
        Jc.save_sequence()
    def reset_sequence():
        print('reset_sequence')
        Jc.reset_sequence()
        move_to_frame1()
    def import_sequence():
        print('import_sequence')
        def get_txt(input_text):
            path=input_text.get()
            print(path)
            if Jc.import_txt(path):
                pass
            else:
                tkinter.messagebox.showerror('파일명 오류', '해당하는 파일이 없습니다.')

            move_to_frame1()
            t_name.destroy()

        input_text=tk.StringVar()
        t_name=tk.Toplevel(window)
        t_name.resizable(False,False)
        t_name.geometry('300x200')
        t_entry=tk.Entry(t_name, textvariable=input_text)
        t_entry.place(x=75, y=50, width=150)
        t_button=tk.Button(t_name, text='확인', command=lambda : get_txt(input_text))
        t_button.place(x=125, y=150, width=50)

        t_name.mainloop()

    def listUp():
        print('listUp')
        global listbox1

        listbox1 = tk.Listbox(frame1,highlightcolor='red',selectmode='single')
        listbox1.delete(0,'end')

        lines=Jc.read_my_sequence()
        lines=lines[1:]
        for i in range(len(lines)):
            if lines[i][1]=='0':
                listbox1.insert(i, '{}'.format(lines[i][0]))
            else:
                listbox1.insert(i,'{} :{}'.format(lines[i][0],lines[i][1]))
        listbox1.place(x=150, y=120, width=275, height=250)
        listbox1.selection_set('end')
        listbox1.see('end')

    def dupSeq():
        print('dupSeq')
        global listbox1
        ndex=listbox1.curselection()
        ndex=int(ndex[0])
        if ndex == 0:
            pass
        else:
            Jc.dup_sequence(ndex)
        move_to_frame1()

    def uP():
        print('uP')
        global listbox1
        ndex=listbox1.curselection()
        ndex=int(ndex[0])
        if ndex <= 1:
            pass
        else:
            Jc.up_sequence(ndex)
        move_to_frame1()

    def dN():
        print('dN')
        global listbox1
        ndex=listbox1.curselection()
        ndex=int(ndex[0])
        limit=len(Jc.read_my_sequence())
        if ndex+2 == limit:
            pass
        elif ndex==0:
            pass
        else:
            Jc.dn_sequence(ndex)
        move_to_frame1()
    def deL():
        print('deL')
        global listbox1
        ndex=listbox1.curselection()
        ndex=int(ndex[0])
        if ndex == 0:
            pass
        else:
            Jc.del_sequence(ndex)
        move_to_frame1()
    def start_macro():
        SM.start_Macro()


    # 옵션창 생성
    menubar=tk.Menu(window)

    menu_1=tk.Menu(menubar, tearoff=0)
    menu_1.add_command(label="메인화면", command=move_to_frame1)
    menu_1.add_command(label="초기화", command=reset_sequence)
    menu_1.add_separator()
    menu_1.add_command(label="종료하기", command=close)
    menubar.add_cascade(label="메인 메뉴", menu=menu_1)

    menu_2=tk.Menu(menubar, tearoff=0)
    menu_2.add_radiobutton(label="실행", command=start_macro)
    menu_2.add_radiobutton(label="불러오기", command=import_sequence)
    menu_2.add_radiobutton(label="내보내기", command=save_sequence)
    menubar.add_cascade(label="시퀀스", menu=menu_2)

    menu_3=tk.Menu(menubar, tearoff=0)
    menu_3.add_checkbutton(label="하위 메뉴 3-1")
    menu_3.add_checkbutton(label="하위 메뉴 3-2")
    menubar.add_cascade(label="3번 메뉴", menu=menu_3)

    window.config(menu=menubar)

    # 세팅 프레임 생성
    frame2=tk.Frame(window)
    frame2.place(x=0,y=0,width=800,height=600)
    # 세팅 프레임의 버튼
    button2_1=tk.Button(frame2,text='주소 입력', command=move_to_frame2_2)
    button2_1.place(x=550,y=120,width=100,height=35)
    button2_2=tk.Button(frame2,text='대기시간', command=move_to_frame2_3)
    button2_2.place(x=550,y=220,width=100,height=35)
    button2_3=tk.Button(frame2,text='element찾기', command=move_to_frame2_4)
    button2_3.place(x=550, y=320, width=100, height=35)
    button2_4=tk.Button(frame2,text='txt 저장', command=confirm_save)
    button2_4.place(x=550,y=420,width=100,height=35)
    button2_5=tk.Button(frame2,text='데이터 체크', command=confirm_check)
    button2_5.place(x=680,y=420,width=100,height=35)
    button2_6 = tk.Button(frame2, text='elements찾기', command=move_to_frame2_5)
    button2_6.place(x=680,y=320,width=100,height=35)
    button2_7 = tk.Button(frame2, text='구글 이미지 크롤링', command=move_to_frame2_6)
    button2_7.place(x=680,y=220,width=100,height=35)
    button2_8 = tk.Button(frame2, text='데이터 초기화', command=release_stack)
    button2_8.place(x=680,y=120,width=100,height=35)
    button2_8 = tk.Button(frame2, text='데이터 쌓기', command=datas_stack)
    button2_8.place(x=550,y=20,width=100,height=35)
    button2_9=tk.Button(frame2,text='반복시작', command=confirm_repeatStart)
    button2_9.place(x=550,y=520,width=100,height=35)
    button2_10=tk.Button(frame2,text='반복종료', command=move_to_frame2_7)
    button2_10.place(x=680,y=520,width=100,height=35)
    # 세팅 주소입력
    frame2_2=tk.Frame(frame2)
    label2_2_1 = tk.Label(frame2_2,text='해당 사이트 주소 입력.')
    label2_2_1.place(x=70,y=60)
    input_text2_2_1 = tk.StringVar()
    entry2_2_1 = tk.Entry(frame2_2, textvariable=input_text2_2_1)
    entry2_2_1.place(x=25,y=100,width=225)
    frame2_2.place(x=150,y=120,width=275,height=355)

    button2_2_1 = tk.Button(frame2_2, text='돌아가기', command=move_to_frame1)
    button2_2_1.place(x=0,y=300, width=50, height=35)
    button2_2_2 = tk.Button(frame2_2, text='확인', command=confirm_address)
    button2_2_2.place(x=225,y=300, width=50, height=35)
    # 세팅 대기시간
    frame2_3=tk.Frame(frame2)
    label2_3_1 = tk.Label(frame2_3,text='대기 시간(단위 :초) 입력.')
    label2_3_1.place(x=70,y=60)
    input_text2_3_1 = tk.StringVar()
    entry2_3_1 = tk.Entry(frame2_3, textvariable=input_text2_3_1)
    entry2_3_1.place(x=25,y=100,width=225)
    frame2_3.place(x=150,y=120,width=275,height=355)

    button2_3_1 = tk.Button(frame2_3, text='돌아가기', command=move_to_frame1)
    button2_3_1.place(x=0,y=300, width=50, height=35)
    button2_3_2 = tk.Button(frame2_3, text='확인',command=confirm_wait)
    button2_3_2.place(x=225,y=300, width=50, height=35)
    # 세팅 element찾기
    frame2_4=tk.Frame(frame2)
    label2_4_1 = tk.Label(frame2_4,text='해당 element 선택 후 이름 입력')
    label2_4_1.place(x=50,y=60)
    input_text2_4_1 = tk.StringVar()
    entry2_4_1 = tk.Entry(frame2_4,textvariable=input_text2_4_1)
    entry2_4_1.place(x=25,y=100,width=225)
    frame2_4.place(x=150,y=120,width=275,height=355)
    elem_var=tk.StringVar()
    radio_1=tk.Radiobutton(frame2_4, text='selector', value='selector', variable=elem_var)
    radio_1.select()
    radio_1.place(x=15,y=150)
    radio_2=tk.Radiobutton(frame2_4, text='Xpath', value='Xpath', variable=elem_var)
    radio_2.place(x=15,y=200)
    radio_3=tk.Radiobutton(frame2_4, text='class', value='class', variable=elem_var)
    radio_3.place(x=100,y=150)
    radio_4=tk.Radiobutton(frame2_4, text='id', value='id', variable=elem_var)
    radio_4.place(x=100,y=200)
    radio_5=tk.Radiobutton(frame2_4, text='link_text', value='link_text', variable=elem_var)
    radio_5.place(x=175,y=150)
    radio_6=tk.Radiobutton(frame2_4, text='p_link_text', value='p_link_text', variable=elem_var)
    radio_6.place(x=175,y=200)

    button2_4_1 = tk.Button(frame2_4, text='돌아가기', command=move_to_frame1)
    button2_4_1.place(x=0,y=300, width=50, height=35)
    button2_4_2 = tk.Button(frame2_4, text='확인',command=confirm_elem)
    button2_4_2.place(x=225,y=300, width=50, height=35)
    # 세팅 elements 찾기 (다중 찾기)
    frame2_5=tk.Frame(frame2)
    label2_5_1 = tk.Label(frame2_5,text='해당 element 선택 후 이름 입력\n'
                                        '(star 0 end 0 〓 전체검색)')
    label2_5_1.place(x=50,y=60)
    input_text2_5_1 = tk.StringVar()
    entry2_5_1 = tk.Entry(frame2_5,textvariable=input_text2_5_1)
    entry2_5_1.place(x=25,y=100,width=225)

    label2_5_2=tk.Label(frame2_5, text='start')
    label2_5_2.place(x=60,y=125)
    input_text2_5_2 = tk.StringVar()
    entry2_5_2 = tk.Entry(frame2_5, textvariable=input_text2_5_2)
    entry2_5_2.place(x=50,y=150,width=50)

    label2_5_3=tk.Label(frame2_5, text='end')
    label2_5_3.place(x=185,y=125)
    input_text2_5_3 = tk.StringVar()
    entry2_5_3 = tk.Entry(frame2_5, textvariable=input_text2_5_3)
    entry2_5_3.place(x=175,y=150,width=50)

    frame2_5.place(x=150,y=120,width=275,height=355)
    elems_var=tk.StringVar()
    radio_1=tk.Radiobutton(frame2_5, text='selector', value='selector', variable=elems_var)
    radio_1.select()
    radio_1.place(x=15,y=200)
    radio_2=tk.Radiobutton(frame2_5, text='Xpath', value='Xpath', variable=elems_var)
    radio_2.place(x=15,y=230)
    radio_3=tk.Radiobutton(frame2_5, text='class', value='class', variable=elems_var)
    radio_3.place(x=100,y=200)
    radio_4=tk.Radiobutton(frame2_5, text='id', value='id', variable=elems_var)
    radio_4.place(x=100,y=230)
    radio_5=tk.Radiobutton(frame2_5, text='link_text', value='link_text', variable=elems_var)
    radio_5.place(x=175,y=200)
    radio_6=tk.Radiobutton(frame2_5, text='p_link_text', value='p_link_text', variable=elems_var)
    radio_6.place(x=175,y=230)

    button2_5_1 = tk.Button(frame2_5, text='돌아가기', command=move_to_frame1)
    button2_5_1.place(x=0,y=300, width=50, height=35)
    button2_5_2 = tk.Button(frame2_5, text='확인',command=confirm_elems)
    button2_5_2.place(x=225,y=300, width=50, height=35)
    # 이미지찾기
    frame2_6=tk.Frame(frame2)
    label2_6_1 = tk.Label(frame2_6,text='해당 이미지url 주소 입력.\n(구글 이미지기준 xpath 추천)')
    label2_6_1.place(x=50,y=60)
    input_text2_6_1 = tk.StringVar()
    entry2_6_1 = tk.Entry(frame2_6,textvariable=input_text2_6_1)
    entry2_6_1.place(x=25,y=100,width=225)
    frame2_6.place(x=150,y=120,width=275,height=355)
    img_var=tk.StringVar()
    radio_1=tk.Radiobutton(frame2_6, text='selector', value='selector', variable=img_var)
    radio_1.select()
    radio_1.place(x=15,y=150)
    radio_2=tk.Radiobutton(frame2_6, text='Xpath', value='Xpath', variable=img_var)
    radio_2.place(x=15,y=200)
    radio_3=tk.Radiobutton(frame2_6, text='class', value='class', variable=img_var)
    radio_3.place(x=100,y=150)
    radio_4=tk.Radiobutton(frame2_6, text='id', value='id', variable=img_var)
    radio_4.place(x=100,y=200)
    radio_5=tk.Radiobutton(frame2_6, text='link_text', value='link_text', variable=img_var)
    radio_5.place(x=175,y=150)
    radio_6=tk.Radiobutton(frame2_6, text='p_link_text', value='p_link_text', variable=img_var)
    radio_6.place(x=175,y=200)

    button2_6_1 = tk.Button(frame2_6, text='돌아가기', command=move_to_frame1)
    button2_6_1.place(x=0,y=300, width=50, height=35)
    button2_6_2 = tk.Button(frame2_6, text='확인',command=confirm_saveImage)
    button2_6_2.place(x=225,y=300, width=50, height=35)
    # 세팅 반복
    frame2_7=tk.Frame(frame2)
    label2_7_1 = tk.Label(frame2_7,text='몇 회 반복? (무한반복 :0)')
    label2_7_1.place(x=70,y=60)
    input_text2_7_1 = tk.StringVar()
    entry2_7_1 = tk.Entry(frame2_7, textvariable=input_text2_7_1)
    entry2_7_1.place(x=25,y=100,width=225)
    frame2_7.place(x=150,y=120,width=275,height=355)

    button2_7_1 = tk.Button(frame2_7, text='돌아가기', command=move_to_frame1)
    button2_7_1.place(x=0,y=300, width=50, height=35)
    button2_7_2 = tk.Button(frame2_7, text='확인',command=confirm_repeatStop)
    button2_7_2.place(x=225,y=300, width=50, height=35)
    # 세팅 프레임 첫 하위 프레임
    frame2_1=tk.Frame(frame2)
    label2_1_1 = tk.Label(frame2_1,text='우측에서 옵션을 선택하세요.')
    label2_1_1.place(x=70,y=60)
    frame2_1.place(x=150,y=120,width=275,height=355)
    button2_1 = tk.Button(frame2_1, text='돌아가기', command=move_to_frame1)
    button2_1.place(x=0,y=300, width=50, height=35)

    # 키보드 프레임 생성
    frame3=tk.Frame(window)
    frame3.place(x=0,y=0,width=800,height=600)
    # 키보드 프레임의 버튼
    button3_1=tk.Button(frame3,text='문자 입력', command=move_to_frame3_2)
    button3_1.place(x=550,y=120,width=100,height=35)
    button3_2=tk.Button(frame3,text='Tab', command=confirm_keyDown)
    button3_2.place(x=550,y=220,width=100,height=35)
    button3_3=tk.Button(frame3,text='Space', command=confirm_keyUp)
    button3_3.place(x=550,y=320,width=100,height=35)
    button3_4=tk.Button(frame3,text='Enter', command=confirm_enter)
    button3_4.place(x=550,y=420,width=100,height=35)
    # 키보드 키보드 입력
    frame3_2=tk.Frame(frame3)
    label3_2_1 = tk.Label(frame3_2,text='문자 입력')
    label3_2_1.place(x=70,y=60)
    input_text3_2_1 = tk.StringVar()
    entry3_2_1 = tk.Entry(frame3_2, textvariable=input_text3_2_1)
    entry3_2_1.place(x=25,y=100,width=225)
    frame3_2.place(x=150,y=120,width=275,height=355)

    button3_2_1 = tk.Button(frame3_2, text='돌아가기', command=move_to_frame1)
    button3_2_1.place(x=0,y=300, width=50, height=35)
    button3_2_2 = tk.Button(frame3_2, text='확인', command=confirm_keyword)
    button3_2_2.place(x=225,y=300, width=50, height=35)
    # 키보드 프레임 첫 하위 프레임
    frame3_1=tk.Frame(frame3)
    label3_1_1 = tk.Label(frame3_1,text='우측에서 옵션을 선택하세요.')
    label3_1_1.place(x=70,y=60)
    frame3_1.place(x=150,y=120,width=275,height=355)
    button3_li_1 = tk.Button(frame3_1, text='돌아가기', command=move_to_frame1)
    button3_li_1.place(x=0,y=300, width=50, height=35)

    # 마우스 프레임 생성
    frame4=tk.Frame(window)
    frame4.place(x=0,y=0,width=800,height=600)
    # 마우스 프레임의 버튼
    button4_1=tk.Button(frame4,text='클릭', command=confirm_click)
    button4_1.place(x=550,y=120,width=100,height=35)
    button4_2=tk.Button(frame4,text='더블클릭', command=confirm_doubleClick)
    button4_2.place(x=550,y=220,width=100,height=35)
    button4_3=tk.Button(frame4,text='elem 이동하기', command=confirm_moveMouse)
    button4_3.place(x=550,y=320,width=100,height=35)
    button4_4=tk.Button(frame4,text='홀드', command=confirm_hold)
    button4_4.place(x=550,y=420,width=100,height=35)
    button4_5=tk.Button(frame4,text='해제', command=confirm_release)
    button4_5.place(x=680,y=420,width=100,height=35)
    # 마우스 프레임 첫 하위 프레임
    frame4_1=tk.Frame(frame4)
    label4_1_1 = tk.Label(frame4_1,text='우측에서 옵션을 선택하세요.')
    label4_1_1.place(x=70,y=60)
    frame4_1.place(x=150,y=120,width=275,height=355)
    button4_li_1 = tk.Button(frame4_1, text='돌아가기', command=move_to_frame1)
    button4_li_1.place(x=0,y=300, width=50, height=35)

    # 휠 프레임 생성
    frame5=tk.Frame(window)
    frame5.place(x=0,y=0,width=800,height=600)
    # 휠 프레임의 버튼
    button5_1=tk.Button(frame5,text='페이지 마지막으로', command=confirm_scrollHeight)
    button5_1.place(x=550,y=120,width=100,height=35)
    button5_2=tk.Button(frame5,text='원하는 만큼', command=move_to_frame5_2)
    button5_2.place(x=550,y=220,width=100,height=35)
    button5_3=tk.Button(frame5,text='elem 이동하기', command=confirm_moveScroll)
    button5_3.place(x=550,y=320,width=100,height=35)
    button5_4=tk.Button(frame5,text='PAGE_DOWN', command=confirm_pageDown)
    button5_4.place(x=550,y=420,width=100,height=35)
    button5_5=tk.Button(frame5,text='계속 스크롤다운', command=confirm_scrollEnd)
    button5_5.place(x=680,y=120,width=100,height=35)
    # 휠 원하는 만큼
    frame5_2=tk.Frame(frame5)
    label5_2_1 = tk.Label(frame5_2,text='휠 얼마나 ?')
    label5_2_1.place(x=70,y=60)
    input_text5_2_1 = tk.StringVar()
    entry5_2_1 = tk.Entry(frame5_2, textvariable=input_text5_2_1)
    entry5_2_1.place(x=25,y=100,width=225)
    frame5_2.place(x=150,y=120,width=275,height=355)

    button5_2_1 = tk.Button(frame5_2, text='돌아가기', command=move_to_frame1)
    button5_2_1.place(x=0,y=300, width=50, height=35)
    button5_2_2 = tk.Button(frame5_2, text='확인', command=confirm_scrollTo)
    button5_2_2.place(x=225,y=300, width=50, height=35)
    # 휠 프레임 첫 하위 프레임
    frame5_1=tk.Frame(frame5)
    label5_1_1 = tk.Label(frame5_1,text='우측에서 옵션을 선택하세요.')
    label5_1_1.place(x=70,y=60)
    frame5_1.place(x=150,y=120,width=275,height=355)
    button5_li_1 = tk.Button(frame5_1, text='돌아가기', command=move_to_frame1)
    button5_li_1.place(x=0,y=300, width=50, height=35)

    # 메인 프레임 생성
    frame1=tk.Frame(window)
    frame1.place(x=0,y=0,width=800,height=600)
    # 메인 프레임의 버튼
    button1_1=tk.Button(frame1,text='세팅', command=move_to_frame2)
    button1_1.place(x=550,y=120,width=100,height=35)
    button1_2=tk.Button(frame1,text='키보드', command=move_to_frame3)
    button1_2.place(x=550,y=220,width=100,height=35)
    button1_3=tk.Button(frame1,text='마우스', command=move_to_frame4)
    button1_3.place(x=550,y=320,width=100,height=35)
    button1_4=tk.Button(frame1,text='휠', command=move_to_frame5)
    button1_4.place(x=550,y=420,width=100,height=35)
    # 메인 프레임의 리스트박스
    listUp()
    # 메인 프레임 리스트박스 하위 버튼
    button1_li_1 = tk.Button(frame1, text='↑', command=uP)
    button1_li_1.place(x=150,y=420, width=50, height=35)
    button1_li_2 = tk.Button(frame1, text='↓', command=dN)
    button1_li_2.place(x=225,y=420, width=50, height=35)
    button1_li_2 = tk.Button(frame1, text='저장', command=save_sequence)
    button1_li_2.place(x=300,y=420, width=50, height=35)
    button1_li_3 = tk.Button(frame1, text='삭제', command=deL)
    button1_li_3.place(x=375,y=420, width=50, height=35)
    button1_li_4 = tk.Button(frame1, text='복사', command=dupSeq )
    button1_li_4.place(x=375,y=500, width=50, height=35)


    window.mainloop()

if __name__ == '__main__':

    browser=''
    find_target=''
    stacked_data=[]
    main_gui()