#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 13, 2020 01:32:23 PM PST  platform: Windows NT

import sys
import os

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Serration_magic_page_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Serration_magic_page_support.set_Tk_var()
    top = app_window (root)
    Serration_magic_page_support.init(root, top)
    root.mainloop()

w = None
def create_app_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Serration_magic_page_support.set_Tk_var()
    top = app_window (w)
    Serration_magic_page_support.init(w, top, *args, **kwargs)
    return w, top

def destroy_app_window():
    global w
    w.destroy()
    w = None

class app_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font23 = "-family Consolas -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x486+450+124")
        top.minsize(1, 1)
        top.maxsize(3844, 1061)
        top.resizable(0, 0)
        top.title("")
        top.configure(background="#000000")
        top.iconbitmap(Serration_magic_page_support.resource_path('favicon-big.ico'))

        self.Label_directory = tk.Label(top)
        self.Label_directory.place(relx=0.0, rely=0.288, height=23, width=121)
        self.Label_directory.configure(activebackground="#000000")
        self.Label_directory.configure(activeforeground="white")
        self.Label_directory.configure(activeforeground="#c0c0c0")
        self.Label_directory.configure(background="#000000")
        self.Label_directory.configure(disabledforeground="#a3a3a3")
        self.Label_directory.configure(font=font9)
        self.Label_directory.configure(foreground="#c0c0c0")
        self.Label_directory.configure(justify='left')
        self.Label_directory.configure(text='''Output Directory''')

        logo = tk.PhotoImage(file=Serration_magic_page_support.resource_path('logo.png'))
        s_logo = tk.PhotoImage(file=Serration_magic_page_support.resource_path('S Logo.png'))

        self.s_logo = tk.Label(top, image=s_logo)
        self.s_logo.photo = s_logo
        self.s_logo.place(relx=0.8, rely=0.021,)
        self.s_logo.configure(background="#000000")
        self.s_logo.configure(disabledforeground="#a3a3a3")
        self.s_logo.configure(font="-family {Segoe UI} -size 9")
        self.s_logo.configure(foreground="#000000")

        self.logo = tk.Label(top, image=logo)
        self.logo.photo = logo
        self.logo.place(relx=0.017, rely=0.021, height=111, width=454)
        self.logo.configure(background="#000000")
        self.logo.configure(disabledforeground="#a3a3a3")
        self.logo.configure(font="-family {Segoe UI} -size 9")
        self.logo.configure(foreground="#000000")
        self.logo.configure(text='''Label''')

        self.Entry_directory = tk.Entry(top)
        self.Entry_directory.place(relx=0.017, rely=0.35, height=20
                , relwidth=0.823)
        self.Entry_directory.configure(background="#000000")
        self.Entry_directory.configure(disabledforeground="#a3a3a3")
        self.Entry_directory.configure(font=font23)
        self.Entry_directory.configure(foreground="#c0c0c0")
        self.Entry_directory.configure(insertbackground="#c0c0c0")
        self.Entry_directory.configure(textvariable=Serration_magic_page_support.post_directory)

        self.choose_button = tk.Button(top)
        self.choose_button.place(relx=0.867, rely=0.35, height=20, width=61)
        self.choose_button.configure(activebackground="#000000")
        self.choose_button.configure(activeforeground="white")
        self.choose_button.configure(activeforeground="#c0c0c0")
        self.choose_button.configure(background="#000000")
        self.choose_button.configure(command=Serration_magic_page_support.get_dir)
        self.choose_button.configure(disabledforeground="#a3a3a3")
        self.choose_button.configure(font="-family {Segoe UI} -size 9")
        self.choose_button.configure(foreground="#c0c0c0")
        self.choose_button.configure(highlightbackground="#d9d9d9")
        self.choose_button.configure(highlightcolor="black")
        self.choose_button.configure(pady="0")
        self.choose_button.configure(text='''Select''')

        self.Label_part_number = tk.Label(top)
        self.Label_part_number.place(relx=0.017, rely=0.432, height=23, width=81)

        self.Label_part_number.configure(activebackground="#000000")
        self.Label_part_number.configure(activeforeground="white")
        self.Label_part_number.configure(activeforeground="#c0c0c0")
        self.Label_part_number.configure(background="#000000")
        self.Label_part_number.configure(disabledforeground="#a3a3a3")
        self.Label_part_number.configure(font="-family {Segoe UI} -size 9")
        self.Label_part_number.configure(foreground="#c0c0c0")
        self.Label_part_number.configure(highlightbackground="#d9d9d9")
        self.Label_part_number.configure(highlightcolor="black")
        self.Label_part_number.configure(justify='left')
        self.Label_part_number.configure(text='''Part Number''')

        self.Entry_part_no = tk.Entry(top)
        self.Entry_part_no.place(relx=0.017, rely=0.494, height=20
                , relwidth=0.357)
        self.Entry_part_no.configure(background="#000000")
        self.Entry_part_no.configure(disabledforeground="#a3a3a3")
        self.Entry_part_no.configure(font="-family {Consolas} -size 10")
        self.Entry_part_no.configure(foreground="#c0c0c0")
        self.Entry_part_no.configure(highlightbackground="#d9d9d9")
        self.Entry_part_no.configure(highlightcolor="black")
        self.Entry_part_no.configure(insertbackground="#c0c0c0")
        self.Entry_part_no.configure(justify='center')
        self.Entry_part_no.configure(selectbackground="#c4c4c4")
        self.Entry_part_no.configure(selectforeground="black")
        self.Entry_part_no.configure(textvariable=Serration_magic_page_support.part_number)

        self.Label_program_number = tk.Label(top)
        self.Label_program_number.place(relx=0.4, rely=0.432, height=23
                , width=131)
        self.Label_program_number.configure(activebackground="#000000")
        self.Label_program_number.configure(activeforeground="white")
        self.Label_program_number.configure(activeforeground="#c0c0c0")
        self.Label_program_number.configure(background="#000000")
        self.Label_program_number.configure(disabledforeground="#a3a3a3")
        self.Label_program_number.configure(font="-family {Segoe UI} -size 9")
        self.Label_program_number.configure(foreground="#c0c0c0")
        self.Label_program_number.configure(highlightbackground="#d9d9d9")
        self.Label_program_number.configure(highlightcolor="black")
        self.Label_program_number.configure(justify='left')
        self.Label_program_number.configure(text='''Program Number''')

        self.Entry_program_number = tk.Entry(top)
        self.Entry_program_number.place(relx=0.433, rely=0.494, height=20
                , relwidth=0.142)
        self.Entry_program_number.configure(background="#000000")
        self.Entry_program_number.configure(disabledforeground="#a3a3a3")
        self.Entry_program_number.configure(font="-family {Consolas} -size 10")
        self.Entry_program_number.configure(foreground="#c0c0c0")
        self.Entry_program_number.configure(highlightbackground="#d9d9d9")
        self.Entry_program_number.configure(highlightcolor="black")
        self.Entry_program_number.configure(insertbackground="#c0c0c0")
        self.Entry_program_number.configure(justify='center')
        self.Entry_program_number.configure(selectbackground="#c4c4c4")
        self.Entry_program_number.configure(selectforeground="black")
        self.Entry_program_number.configure(textvariable=Serration_magic_page_support.program_number)

        self.Label_work_offset = tk.Label(top)
        self.Label_work_offset.place(relx=0.633, rely=0.432, height=23, width=91)

        self.Label_work_offset.configure(activebackground="#000000")
        self.Label_work_offset.configure(activeforeground="white")
        self.Label_work_offset.configure(activeforeground="#c0c0c0")
        self.Label_work_offset.configure(background="#000000")
        self.Label_work_offset.configure(disabledforeground="#a3a3a3")
        self.Label_work_offset.configure(font="-family {Segoe UI} -size 9")
        self.Label_work_offset.configure(foreground="#c0c0c0")
        self.Label_work_offset.configure(highlightbackground="#d9d9d9")
        self.Label_work_offset.configure(highlightcolor="black")
        self.Label_work_offset.configure(justify='left')
        self.Label_work_offset.configure(text='''Work Offset''')

        self.Entry_work_offset = tk.Entry(top)
        self.Entry_work_offset.place(relx=0.65, rely=0.494, height=20
                , relwidth=0.142)
        self.Entry_work_offset.configure(background="#000000")
        self.Entry_work_offset.configure(disabledforeground="#a3a3a3")
        self.Entry_work_offset.configure(font="-family {Consolas} -size 10")
        self.Entry_work_offset.configure(foreground="#c0c0c0")
        self.Entry_work_offset.configure(highlightbackground="#d9d9d9")
        self.Entry_work_offset.configure(highlightcolor="black")
        self.Entry_work_offset.configure(insertbackground="#c0c0c0")
        self.Entry_work_offset.configure(justify='center')
        self.Entry_work_offset.configure(selectbackground="#c4c4c4")
        self.Entry_work_offset.configure(selectforeground="black")
        self.Entry_work_offset.configure(textvariable=Serration_magic_page_support.work_offset)

        self.Label_tool_number = tk.Label(top)
        self.Label_tool_number.place(relx=0.817, rely=0.432, height=23, width=91)

        self.Label_tool_number.configure(activebackground="#000000")
        self.Label_tool_number.configure(activeforeground="white")
        self.Label_tool_number.configure(activeforeground="#c0c0c0")
        self.Label_tool_number.configure(background="#000000")
        self.Label_tool_number.configure(disabledforeground="#a3a3a3")
        self.Label_tool_number.configure(font="-family {Segoe UI} -size 9")
        self.Label_tool_number.configure(foreground="#c0c0c0")
        self.Label_tool_number.configure(highlightbackground="#d9d9d9")
        self.Label_tool_number.configure(highlightcolor="black")
        self.Label_tool_number.configure(justify='left')
        self.Label_tool_number.configure(text='''Tool Number''')

        self.Entry_tool_number = tk.Entry(top)
        self.Entry_tool_number.place(relx=0.833, rely=0.494, height=20
                , relwidth=0.142)
        self.Entry_tool_number.configure(background="#000000")
        self.Entry_tool_number.configure(disabledforeground="#a3a3a3")
        self.Entry_tool_number.configure(font="-family {Consolas} -size 10")
        self.Entry_tool_number.configure(foreground="#c0c0c0")
        self.Entry_tool_number.configure(highlightbackground="#d9d9d9")
        self.Entry_tool_number.configure(highlightcolor="black")
        self.Entry_tool_number.configure(insertbackground="#c0c0c0")
        self.Entry_tool_number.configure(justify='center')
        self.Entry_tool_number.configure(selectbackground="#c4c4c4")
        self.Entry_tool_number.configure(selectforeground="black")
        self.Entry_tool_number.configure(textvariable=Serration_magic_page_support.tool_number)

        self.Label_location = tk.Label(top)
        self.Label_location.place(relx=0.0, rely=0.576, height=23, width=141)
        self.Label_location.configure(activebackground="#000000")
        self.Label_location.configure(activeforeground="white")
        self.Label_location.configure(activeforeground="#c0c0c0")
        self.Label_location.configure(background="#000000")
        self.Label_location.configure(disabledforeground="#a3a3a3")
        self.Label_location.configure(font="-family {Segoe UI} -size 9")
        self.Label_location.configure(foreground="#c0c0c0")
        self.Label_location.configure(highlightbackground="#d9d9d9")
        self.Label_location.configure(highlightcolor="black")
        self.Label_location.configure(justify='left')
        self.Label_location.configure(text='''Location of Serration:''')

        self.Label_x_center = tk.Label(top)
        self.Label_x_center.place(relx=0.0, rely=0.638, height=23, width=81)
        self.Label_x_center.configure(activebackground="#000000")
        self.Label_x_center.configure(activeforeground="white")
        self.Label_x_center.configure(activeforeground="#c0c0c0")
        self.Label_x_center.configure(background="#000000")
        self.Label_x_center.configure(disabledforeground="#a3a3a3")
        self.Label_x_center.configure(font="-family {Segoe UI} -size 9")
        self.Label_x_center.configure(foreground="#c0c0c0")
        self.Label_x_center.configure(highlightbackground="#d9d9d9")
        self.Label_x_center.configure(highlightcolor="black")
        self.Label_x_center.configure(justify='left')
        self.Label_x_center.configure(text='''X - Center''')

        self.Entry_x_center = tk.Entry(top)
        self.Entry_x_center.place(relx=0.017, rely=0.7, height=20
                , relwidth=0.142)
        self.Entry_x_center.configure(background="#000000")
        self.Entry_x_center.configure(disabledforeground="#a3a3a3")
        self.Entry_x_center.configure(font="-family {Consolas} -size 10")
        self.Entry_x_center.configure(foreground="#c0c0c0")
        self.Entry_x_center.configure(highlightbackground="#d9d9d9")
        self.Entry_x_center.configure(highlightcolor="black")
        self.Entry_x_center.configure(insertbackground="#c0c0c0")
        self.Entry_x_center.configure(justify='center')
        self.Entry_x_center.configure(selectbackground="#c4c4c4")
        self.Entry_x_center.configure(selectforeground="black")
        self.Entry_x_center.configure(textvariable=Serration_magic_page_support.x_center)

        self.Label_y_center = tk.Label(top)
        self.Label_y_center.place(relx=0.217, rely=0.638, height=23, width=71)
        self.Label_y_center.configure(activebackground="#000000")
        self.Label_y_center.configure(activeforeground="white")
        self.Label_y_center.configure(activeforeground="#c0c0c0")
        self.Label_y_center.configure(background="#000000")
        self.Label_y_center.configure(disabledforeground="#a3a3a3")
        self.Label_y_center.configure(font="-family {Segoe UI} -size 9")
        self.Label_y_center.configure(foreground="#c0c0c0")
        self.Label_y_center.configure(highlightbackground="#d9d9d9")
        self.Label_y_center.configure(highlightcolor="black")
        self.Label_y_center.configure(justify='left')
        self.Label_y_center.configure(text='''Y - Center''')

        self.Label_b = tk.Label(top)
        self.Label_b.place(relx=0.633, rely=0.638, height=23, width=71)
        self.Label_b.configure(activebackground="#000000")
        self.Label_b.configure(activeforeground="white")
        self.Label_b.configure(activeforeground="#c0c0c0")
        self.Label_b.configure(background="#000000")
        self.Label_b.configure(disabledforeground="#a3a3a3")
        self.Label_b.configure(font="-family {Segoe UI} -size 9")
        self.Label_b.configure(foreground="#c0c0c0")
        self.Label_b.configure(highlightbackground="#d9d9d9")
        self.Label_b.configure(highlightcolor="black")
        self.Label_b.configure(justify='left')
        self.Label_b.configure(text='''B - Angle''')

        self.Entry_y_center = tk.Entry(top)
        self.Entry_y_center.place(relx=0.233, rely=0.7, height=20
                , relwidth=0.142)
        self.Entry_y_center.configure(background="#000000")
        self.Entry_y_center.configure(disabledforeground="#a3a3a3")
        self.Entry_y_center.configure(font="-family {Consolas} -size 10")
        self.Entry_y_center.configure(foreground="#c0c0c0")
        self.Entry_y_center.configure(highlightbackground="#d9d9d9")
        self.Entry_y_center.configure(highlightcolor="black")
        self.Entry_y_center.configure(insertbackground="#c0c0c0")
        self.Entry_y_center.configure(justify='center')
        self.Entry_y_center.configure(selectbackground="#c4c4c4")
        self.Entry_y_center.configure(selectforeground="black")
        self.Entry_y_center.configure(textvariable=Serration_magic_page_support.y_center)

        self.Entry_z = tk.Entry(top)
        self.Entry_z.place(relx=0.433, rely=0.7,height=20, relwidth=0.142)
        self.Entry_z.configure(background="#000000")
        self.Entry_z.configure(disabledforeground="#a3a3a3")
        self.Entry_z.configure(font="-family {Consolas} -size 10")
        self.Entry_z.configure(foreground="#c0c0c0")
        self.Entry_z.configure(highlightbackground="#d9d9d9")
        self.Entry_z.configure(highlightcolor="black")
        self.Entry_z.configure(insertbackground="#c0c0c0")
        self.Entry_z.configure(justify='center')
        self.Entry_z.configure(selectbackground="#c4c4c4")
        self.Entry_z.configure(selectforeground="black")
        self.Entry_z.configure(textvariable=Serration_magic_page_support.z_top)

        self.Label_Z_top = tk.Label(top)
        self.Label_Z_top.place(relx=0.417, rely=0.638, height=23, width=61)
        self.Label_Z_top.configure(activebackground="#000000")
        self.Label_Z_top.configure(activeforeground="white")
        self.Label_Z_top.configure(activeforeground="#c0c0c0")
        self.Label_Z_top.configure(background="#000000")
        self.Label_Z_top.configure(disabledforeground="#a3a3a3")
        self.Label_Z_top.configure(font="-family {Segoe UI} -size 9")
        self.Label_Z_top.configure(foreground="#c0c0c0")
        self.Label_Z_top.configure(highlightbackground="#d9d9d9")
        self.Label_Z_top.configure(highlightcolor="black")
        self.Label_Z_top.configure(justify='left')
        self.Label_Z_top.configure(text='''Z - Top''')

        self.Entry_b = tk.Entry(top)
        self.Entry_b.place(relx=0.65, rely=0.7,height=20, relwidth=0.142)
        self.Entry_b.configure(background="#000000")
        self.Entry_b.configure(disabledforeground="#a3a3a3")
        self.Entry_b.configure(font="-family {Consolas} -size 10")
        self.Entry_b.configure(foreground="#c0c0c0")
        self.Entry_b.configure(highlightbackground="#d9d9d9")
        self.Entry_b.configure(highlightcolor="black")
        self.Entry_b.configure(insertbackground="#c0c0c0")
        self.Entry_b.configure(justify='center')
        self.Entry_b.configure(selectbackground="#c4c4c4")
        self.Entry_b.configure(selectforeground="black")
        self.Entry_b.configure(textvariable=Serration_magic_page_support.b_angle)

        self.Label_feed = tk.Label(top)
        self.Label_feed.place(relx=0.817, rely=0.638, height=23, width=81)
        self.Label_feed.configure(activebackground="#000000")
        self.Label_feed.configure(activeforeground="white")
        self.Label_feed.configure(activeforeground="#c0c0c0")
        self.Label_feed.configure(background="#000000")
        self.Label_feed.configure(disabledforeground="#a3a3a3")
        self.Label_feed.configure(font="-family {Segoe UI} -size 9")
        self.Label_feed.configure(foreground="#c0c0c0")
        self.Label_feed.configure(highlightbackground="#d9d9d9")
        self.Label_feed.configure(highlightcolor="black")
        self.Label_feed.configure(justify='left')
        self.Label_feed.configure(text='''Feed Rate''')

        self.Entry_feed_rate = tk.Entry(top)
        self.Entry_feed_rate.place(relx=0.833, rely=0.7, height=20
                                   , relwidth=0.142)
        self.Entry_feed_rate.configure(background="#000000")
        self.Entry_feed_rate.configure(disabledforeground="#a3a3a3")
        self.Entry_feed_rate.configure(font="-family {Consolas} -size 10")
        self.Entry_feed_rate.configure(foreground="#c0c0c0")
        self.Entry_feed_rate.configure(highlightbackground="#d9d9d9")
        self.Entry_feed_rate.configure(highlightcolor="black")
        self.Entry_feed_rate.configure(insertbackground="#c0c0c0")
        self.Entry_feed_rate.configure(justify='center')
        self.Entry_feed_rate.configure(selectbackground="#c4c4c4")
        self.Entry_feed_rate.configure(selectforeground="black")
        self.Entry_feed_rate.configure(textvariable=Serration_magic_page_support.feed_rate)

        self.Labeltoolnumber_9 = tk.Label(top)
        self.Labeltoolnumber_9.place(relx=-0.017, rely=0.782, height=23
                , width=131)
        self.Labeltoolnumber_9.configure(activebackground="#000000")
        self.Labeltoolnumber_9.configure(activeforeground="white")
        self.Labeltoolnumber_9.configure(activeforeground="#c0c0c0")
        self.Labeltoolnumber_9.configure(background="#000000")
        self.Labeltoolnumber_9.configure(disabledforeground="#a3a3a3")
        self.Labeltoolnumber_9.configure(font="-family {Segoe UI} -size 9")
        self.Labeltoolnumber_9.configure(foreground="#c0c0c0")
        self.Labeltoolnumber_9.configure(highlightbackground="#d9d9d9")
        self.Labeltoolnumber_9.configure(highlightcolor="black")
        self.Labeltoolnumber_9.configure(justify='left')
        self.Labeltoolnumber_9.configure(text='''Size of Serration:''')

        self.Label_od = tk.Label(top)
        self.Label_od.place(relx=0.017, rely=0.844, height=23, width=31)
        self.Label_od.configure(activebackground="#000000")
        self.Label_od.configure(activeforeground="white")
        self.Label_od.configure(activeforeground="#c0c0c0")
        self.Label_od.configure(background="#000000")
        self.Label_od.configure(disabledforeground="#a3a3a3")
        self.Label_od.configure(font="-family {Segoe UI} -size 9")
        self.Label_od.configure(foreground="#c0c0c0")
        self.Label_od.configure(highlightbackground="#d9d9d9")
        self.Label_od.configure(highlightcolor="black")
        self.Label_od.configure(justify='left')
        self.Label_od.configure(text='''OD''')

        self.Label_id = tk.Label(top)
        self.Label_id.place(relx=0.233, rely=0.844, height=23, width=21)
        self.Label_id.configure(activebackground="#000000")
        self.Label_id.configure(activeforeground="white")
        self.Label_id.configure(activeforeground="#c0c0c0")
        self.Label_id.configure(background="#000000")
        self.Label_id.configure(disabledforeground="#a3a3a3")
        self.Label_id.configure(font="-family {Segoe UI} -size 9")
        self.Label_id.configure(foreground="#c0c0c0")
        self.Label_id.configure(highlightbackground="#d9d9d9")
        self.Label_id.configure(highlightcolor="black")
        self.Label_id.configure(justify='left')
        self.Label_id.configure(text='''ID''')

        self.Entry_od = tk.Entry(top)
        self.Entry_od.place(relx=0.017, rely=0.905,height=20, relwidth=0.142)
        self.Entry_od.configure(background="#000000")
        self.Entry_od.configure(disabledforeground="#a3a3a3")
        self.Entry_od.configure(font="-family {Consolas} -size 10")
        self.Entry_od.configure(foreground="#c0c0c0")
        self.Entry_od.configure(highlightbackground="#d9d9d9")
        self.Entry_od.configure(highlightcolor="black")
        self.Entry_od.configure(insertbackground="#c0c0c0")
        self.Entry_od.configure(justify='center')
        self.Entry_od.configure(selectbackground="#c4c4c4")
        self.Entry_od.configure(selectforeground="black")
        self.Entry_od.configure(textvariable=Serration_magic_page_support.od)

        self.Entry_id = tk.Entry(top)
        self.Entry_id.place(relx=0.233, rely=0.905,height=20, relwidth=0.142)
        self.Entry_id.configure(background="#000000")
        self.Entry_id.configure(disabledforeground="#a3a3a3")
        self.Entry_id.configure(font="-family {Consolas} -size 10")
        self.Entry_id.configure(foreground="#c0c0c0")
        self.Entry_id.configure(highlightbackground="#d9d9d9")
        self.Entry_id.configure(highlightcolor="black")
        self.Entry_id.configure(insertbackground="#c0c0c0")
        self.Entry_id.configure(justify='center')
        self.Entry_id.configure(selectbackground="#c4c4c4")
        self.Entry_id.configure(selectforeground="black")
        self.Entry_id.configure(textvariable=Serration_magic_page_support.id)

        self.Entry_pitch = tk.Entry(top)
        self.Entry_pitch.place(relx=0.433, rely=0.905, height=20, relwidth=0.142)

        self.Entry_pitch.configure(background="#000000")
        self.Entry_pitch.configure(disabledforeground="#a3a3a3")
        self.Entry_pitch.configure(font="-family {Consolas} -size 10")
        self.Entry_pitch.configure(foreground="#c0c0c0")
        self.Entry_pitch.configure(highlightbackground="#d9d9d9")
        self.Entry_pitch.configure(highlightcolor="black")
        self.Entry_pitch.configure(insertbackground="#c0c0c0")
        self.Entry_pitch.configure(justify='center')
        self.Entry_pitch.configure(selectbackground="#c4c4c4")
        self.Entry_pitch.configure(selectforeground="black")
        self.Entry_pitch.configure(textvariable=Serration_magic_page_support.pitch)

        self.Label_pitch = tk.Label(top)
        self.Label_pitch.place(relx=0.417, rely=0.844, height=23, width=51)
        self.Label_pitch.configure(activebackground="#000000")
        self.Label_pitch.configure(activeforeground="white")
        self.Label_pitch.configure(activeforeground="#c0c0c0")
        self.Label_pitch.configure(background="#000000")
        self.Label_pitch.configure(disabledforeground="#a3a3a3")
        self.Label_pitch.configure(font="-family {Segoe UI} -size 9")
        self.Label_pitch.configure(foreground="#c0c0c0")
        self.Label_pitch.configure(highlightbackground="#d9d9d9")
        self.Label_pitch.configure(highlightcolor="black")
        self.Label_pitch.configure(justify='left')
        self.Label_pitch.configure(text='''Pitch''')

        self.Label_depth = tk.Label(top)
        self.Label_depth.place(relx=0.633, rely=0.844, height=23, width=81)
        self.Label_depth.configure(activebackground="#000000")
        self.Label_depth.configure(activeforeground="white")
        self.Label_depth.configure(activeforeground="#c0c0c0")
        self.Label_depth.configure(background="#000000")
        self.Label_depth.configure(disabledforeground="#a3a3a3")
        self.Label_depth.configure(font="-family {Segoe UI} -size 9")
        self.Label_depth.configure(foreground="#c0c0c0")
        self.Label_depth.configure(highlightbackground="#d9d9d9")
        self.Label_depth.configure(highlightcolor="black")
        self.Label_depth.configure(justify='left')
        self.Label_depth.configure(text='''Cut Depth''')

        self.Entry_depth = tk.Entry(top)
        self.Entry_depth.place(relx=0.65, rely=0.905,height=20, relwidth=0.142)
        self.Entry_depth.configure(background="#000000")
        self.Entry_depth.configure(disabledforeground="#a3a3a3")
        self.Entry_depth.configure(font="-family {Consolas} -size 10")
        self.Entry_depth.configure(foreground="#c0c0c0")
        self.Entry_depth.configure(highlightbackground="#d9d9d9")
        self.Entry_depth.configure(highlightcolor="black")
        self.Entry_depth.configure(insertbackground="#c0c0c0")
        self.Entry_depth.configure(justify='center')
        self.Entry_depth.configure(selectbackground="#c4c4c4")
        self.Entry_depth.configure(selectforeground="black")
        self.Entry_depth.configure(textvariable=Serration_magic_page_support.depth)

        self.do_it_button = tk.Button(top)
        self.do_it_button.place(relx=0.833, rely=0.802, height=80, width=81)
        self.do_it_button.configure(activebackground="#f9f9f9")
        self.do_it_button.configure(activeforeground="black")
        self.do_it_button.configure(background="#000000")
        self.do_it_button.configure(command=Serration_magic_page_support.magic)
        self.do_it_button.configure(disabledforeground="#a3a3a3")
        self.do_it_button.configure(font="-family {Segoe UI} -size 9")
        self.do_it_button.configure(foreground="#c0c0c0")
        self.do_it_button.configure(highlightbackground="#d9d9d9")
        self.do_it_button.configure(highlightcolor="black")
        self.do_it_button.configure(pady="0")
        self.do_it_button.configure(text='''Magic''')



if __name__ == '__main__':
    vp_start_gui()





