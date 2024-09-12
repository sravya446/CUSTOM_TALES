from tkinter import *

root = Tk()
root.title("Mad Libs Generator")
root.geometry('360x300')
root.configure(background='Gainsboro')
root.resizable(False, False)

Label(root, font=("ALGERIAN", 16), text='*Mad Libs Generator*').place(x=70, y=7)
Label(root, font=("ALGERIAN", 16), text='Have fun!!!!').place(x=130, y=35)


def first_madlib(win):
    def finish_madlib(tl: Toplevel, animal, insect, spouse, favourite, movement, preposition):
        text = f'''
        In a bustling city, there lived a lovely couple: the {animal} and his adventurous {spouse}. They were known for their exciting escapades and joyful nature.

One fine day, they decided to visit their favorite {favourite}. They packed their things and set off in their {movement}. The journey was delightful, with the sun shining and a gentle breeze accompanying them. As they were returning from their wonderful outing, an unexpected accident happened. The {animal} and the {insect} were startled when their {movement} suddenly veered off course. They crashed into something, and the {animal} got badly wounded. However, the {insect} miraculously escaped without a scratch.

The reason for the {insect}'s good fortune was that it had taken precautions. The {insect} was wearing a special helmet and had safety gear that protected it from the impact. This careful preparation ensured that the {insect} remained unharmed, {preposition} the {animal} suffered some injuries. The {animal} was taken to the hospital for treatment, while the {insect} stayed by its side, offering comfort and support. The accident was a wake-up call for them both, reminding them of the importance of safety and preparation.

From then on, the {animal} and the {insect} made sure to always travel with the right safety measures, learning from their experience and continuing their adventures with greater caution and care.

And thus, they lived happily ever after, sharing their tale of adventure and the valuable lesson they learned. The end..'''
        for widget in tl.winfo_children():
            widget.destroy()
        tl.geometry('800x600')
        Label(tl, text='Your Story:', font=("Sitka Subheading Semibold", 13, 'bold'), background='Gold', wraplength=tl.winfo_width()).grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        Label(tl, text=text, font=("Sitka Subheading Semibold", 13), background='Gold', wraplength=tl.winfo_width()).grid(row=1, column=0,
                                                                                                      padx=10, pady=10,
                                                                                                      sticky='w')

    ml1_wn = Toplevel(win, bg='Gold')
    ml1_wn.title("The Ant Accident")
    ml1_wn.geometry('800x600')
    ml1_wn.resizable(False, False)

    Label(ml1_wn, text='The Ant Accident', font=("Helvetica", 20, 'bold'), bg='Gold').grid(row=0, column=0, padx=10,
                                                                                           pady=10)

    Label(ml1_wn, text='An animal:', font=("Times", 15), bg='Gold').grid(row=1, column=0, padx=10, sticky='w')
    Label(ml1_wn, text='An insect:', font=("Times", 15), bg='Gold').grid(row=2, column=0, padx=10, sticky='w')
    Label(ml1_wn, text='Choose your spouse:', font=("Times", 15), bg='Gold').grid(row=3, column=0, padx=10, sticky='w')
    Label(ml1_wn, text='Choose a favourite:', font=("Times", 15), bg='Gold').grid(row=4, column=0, padx=10, sticky='w')
    Label(ml1_wn, text='Choose a movement:', font=("Times", 15), bg='Gold').grid(row=5, column=0, padx=10, sticky='w')
    Label(ml1_wn, text='Choose a preposition:', font=("Times", 15), bg='Gold').grid(row=6, column=0, padx=10,
                                                                                    sticky='w')

    animal_entry = Entry(ml1_wn, width=30)
    animal_entry.grid(row=1, column=1, padx=10, pady=5)
    insect_entry = Entry(ml1_wn, width=30)
    insect_entry.grid(row=2, column=1, padx=10, pady=5)

    spouse = ['wife', 'husband']
    favourite = ['movie', 'garden', 'mall', 'store', 'playground']
    preposition = ['but', 'and']
    movement = ['cycle', 'bike']

    spouse_opt = StringVar(ml1_wn)
    spouse_opt.set(spouse[0])
    OptionMenu(ml1_wn, spouse_opt, *spouse).grid(row=3, column=1, padx=10, pady=5, sticky='w')

    favourite_opt = StringVar(ml1_wn)
    favourite_opt.set(favourite[0])
    OptionMenu(ml1_wn, favourite_opt, *favourite).grid(row=4, column=1, padx=10, pady=5, sticky='w')

    movement_opt = StringVar(ml1_wn)
    movement_opt.set(movement[0])
    OptionMenu(ml1_wn, movement_opt, *movement).grid(row=5, column=1, padx=10, pady=5, sticky='w')

    preposition_opt = StringVar(ml1_wn)
    preposition_opt.set(preposition[0])
    OptionMenu(ml1_wn, preposition_opt, *preposition).grid(row=6, column=1, padx=10, pady=5, sticky='w')

    submit_btn = Button(ml1_wn, text="Submit", background="SteelBlue", font=('Times', 12),
                        command=lambda: finish_madlib(ml1_wn, animal_entry.get(), insect_entry.get(),
                                                      spouse_opt.get(), favourite_opt.get(),
                                                      movement_opt.get(), preposition_opt.get()))
    submit_btn.grid(row=7, column=0, columnspan=2, pady=20)

    ml1_wn.mainloop()


def second_madlib(win):
    def finish_madlib(tl: Toplevel, Yourname, Friendname, Drink, Food, Passion):
        text = f'''
        {Yourname} & {Friendname} are two friends who are {Passion}, visited a restaurant & ordered {Drink}. They don't order anything to eat as they have {Food} in their briefcases which was bought from outside. The two friends take out their {Food} and started eating. The waiter comes & says you are not allowed to eat your own {Food}. The smart friends look at each other & laugh & exchanged their {Food}.'''
        for widget in tl.winfo_children():
            widget.destroy()
        tl.geometry('800x600')
        Label(tl, text='Your Story:', font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='RoyalBlue2').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='RoyalBlue2').grid(row=1, column=0,
                                                                                                    padx=10, pady=10,
                                                                                                    sticky='w')

    ml2_wn = Toplevel(win, bg='RoyalBlue2')
    ml2_wn.title("The Night Dinner")
    ml2_wn.geometry('800x600')
    ml2_wn.resizable(True, True)

    Label(ml2_wn, text='The Night Dinner', font=("Times", 17, 'bold'), bg='RoyalBlue2').grid(row=0, column=0, padx=10,
                                                                                         pady=10)
    Label(ml2_wn, text='Yourname:', font=("Times", 15), bg='RoyalBlue2').grid(row=1, column=0, padx=10, sticky='w')
    Label(ml2_wn, text='Friendname:', font=("Times", 15), bg='RoyalBlue2').grid(row=2, column=0, padx=10, sticky='w')
    Label(ml2_wn, text='Choose a Drink:', font=("Times", 15), bg='RoyalBlue2').grid(row=3, column=0, padx=10,
                                                                                    sticky='w')
    Label(ml2_wn, text='Choose a Food:', font=("Times", 15), bg='RoyalBlue2').grid(row=4, column=0, padx=10, sticky='w')
    Label(ml2_wn, text='Choose Passion:', font=("Times", 15), bg='RoyalBlue2').grid(row=5, column=0, padx=10,
                                                                                    sticky='w')

    Yourname_entry = Entry(ml2_wn, width=30)
    Yourname_entry.grid(row=1, column=1, padx=10, pady=5)
    Friendname_entry = Entry(ml2_wn, width=30)
    Friendname_entry.grid(row=2, column=1, padx=10, pady=5)

    Drink = ['coke', 'pepsi', 'Thumbs Up', 'Maaza', 'Pulpy Orange']
    Food = ['Chicken Biryani', 'Mutton Biriyani', 'sandwich', 'Prawns', 'Crabs']
    Passion = ['doctor', 'engineer', 'Police', 'IAS', 'IPS']

    Drink_opt = StringVar(ml2_wn)
    Drink_opt.set(Drink[0])
    OptionMenu(ml2_wn, Drink_opt, *Drink).grid(row=3, column=1, padx=10, pady=5, sticky='w')

    Food_opt = StringVar(ml2_wn)
    Food_opt.set(Food[0])
    OptionMenu(ml2_wn, Food_opt, *Food).grid(row=4, column=1, padx=10, pady=5, sticky='w')

    Passion_opt = StringVar(ml2_wn)
    Passion_opt.set(Passion[0])
    OptionMenu(ml2_wn, Passion_opt, *Passion).grid(row=5, column=1, padx=10, pady=5, sticky='w')

    submit_btn = Button(ml2_wn, text="Submit", background="SteelBlue", font=('Times', 12),
                        command=lambda: finish_madlib(ml2_wn, Yourname_entry.get(), Friendname_entry.get(),
                                                      Drink_opt.get(), Food_opt.get(), Passion_opt.get()))
    submit_btn.grid(row=6, column=0, columnspan=2, pady=20)

    ml2_wn.mainloop()


def third_madlib(win):
    def finish_madlib(tl: Toplevel, boy1, boy2, girl1, girl2, animal, exclamation):
        text = f'''
        Once upon a time, there were two boys, {boy1} and {boy2}, and two girls, {girl1} and {girl2}. They decided to go on an adventure with their pet {animal}. Along the way, they encountered a magical creature that made them all shout "{exclamation}!"'''
        for widget in tl.winfo_children():
            widget.destroy()
        tl.geometry('800x600')
        Label(tl, text='Your Story:', font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='DarkOrange').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='DarkOrange').grid(row=1, column=0,
                                                                                                    padx=10, pady=10,
                                                                                                    sticky='w')

    ml3_wn = Toplevel(win, bg='DarkOrange')
    ml3_wn.title("The Friendship Story")
    ml3_wn.geometry('800x600')
    ml3_wn.resizable(True, True)

    Label(ml3_wn, text='The Friendship Story', font=("Times", 17, 'bold'), bg='DarkOrange').grid(row=0, column=0,
                                                                                                 padx=10, pady=10)
    Label(ml3_wn, text='A boy\'s name:', font=("Times", 15), bg='DarkOrange').grid(row=1, column=0, padx=10, sticky='w')
    Label(ml3_wn, text='Another boy\'s name:', font=("Times", 15), bg='DarkOrange').grid(row=2, column=0, padx=10,
                                                                                         sticky='w')
    Label(ml3_wn, text='A girl\'s name:', font=("Times", 15), bg='DarkOrange').grid(row=3, column=0, padx=10,
                                                                                    sticky='w')
    Label(ml3_wn, text='Another girl\'s name:', font=("Times", 15), bg='DarkOrange').grid(row=4, column=0, padx=10,
                                                                                          sticky='w')
    Label(ml3_wn, text='An animal:', font=("Times", 15), bg='DarkOrange').grid(row=5, column=0, padx=10, sticky='w')
    Label(ml3_wn, text='An exclamation:', font=("Times", 15), bg='DarkOrange').grid(row=6, column=0, padx=10,
                                                                                    sticky='w')

    boy1_name_entry = Entry(ml3_wn, width=30)
    boy1_name_entry.grid(row=1, column=1, padx=10, pady=5)
    boy2_name_entry = Entry(ml3_wn, width=30)
    boy2_name_entry.grid(row=2, column=1, padx=10, pady=5)
    girl1_name_entry = Entry(ml3_wn, width=30)
    girl1_name_entry.grid(row=3, column=1, padx=10, pady=5)
    girl2_name_entry = Entry(ml3_wn, width=30)
    girl2_name_entry.grid(row=4, column=1, padx=10, pady=5)
    animal_entry = Entry(ml3_wn, width=30)
    animal_entry.grid(row=5, column=1, padx=10, pady=5)
    exclamation_entry = Entry(ml3_wn, width=30)
    exclamation_entry.grid(row=6, column=1, padx=10, pady=5)

    submit_btn = Button(ml3_wn, text="Submit", background="SteelBlue", font=('Times', 12),
                        command=lambda: finish_madlib(ml3_wn, boy1_name_entry.get(), boy2_name_entry.get(),
                                                      girl1_name_entry.get(), girl2_name_entry.get(),
                                                      animal_entry.get(), exclamation_entry.get()))
    submit_btn.grid(row=7, column=0, columnspan=2, pady=20)

    ml3_wn.mainloop()


def fourth_madlib(win):
    def finish_madlib(tl: Toplevel, friend1, friend2, friend3, mode, payment, express):
        text = f'''
        {friend1}, {friend2}, and {friend3} went out for a night. They decided to travel by {mode}. When they reached the place, they realized they had forgotten their wallet! They had to find a way to pay for the drinks. Luckily, they found a way to use {payment} to cover the bill. At the end of the night, they were all very happy and exclaimed, "{express}!"'''
        for widget in tl.winfo_children():
            widget.destroy()
        tl.geometry('800x600')
        Label(tl, text='Your Story:', font=("Times", 13, 'bold'), wraplength=tl.winfo_width(), bg='LightSalmon').grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        Label(tl, text=text, font=("Times", 13), wraplength=tl.winfo_width(), bg='LightSalmon').grid(row=1, column=0,
                                                                                                     padx=10, pady=10,
                                                                                                     sticky='w')

    ml4_wn = Toplevel(win, bg='LightSalmon')
    ml4_wn.title("The Three Drunkers")
    ml4_wn.geometry('800x600')
    ml4_wn.resizable(True, True)

    Label(ml4_wn, text='The Three Drunkers', font=("Times", 17, 'bold'), bg='LightSalmon').grid(row=0, column=0,
                                                                                                padx=10, pady=10)
    Label(ml4_wn, text='First friend\'s name:', font=("Times", 15), bg='LightSalmon').grid(row=1, column=0, padx=10,
                                                                                           sticky='w')
    Label(ml4_wn, text='Second friend\'s name:', font=("Times", 15), bg='LightSalmon').grid(row=2, column=0, padx=10,
                                                                                            sticky='w')
    Label(ml4_wn, text='Third friend\'s name:', font=("Times", 15), bg='LightSalmon').grid(row=3, column=0, padx=10,
                                                                                           sticky='w')
    Label(ml4_wn, text='Choose way of mode:', font=("Times", 15), bg='LightSalmon').grid(row=4, column=0, padx=10,
                                                                                         sticky='w')
    Label(ml4_wn, text='Choose payment method:', font=("Times", 15), bg='LightSalmon').grid(row=5, column=0, padx=10,
                                                                                            sticky='w')
    Label(ml4_wn, text='Choose an express:', font=("Times", 15), bg='LightSalmon').grid(row=6, column=0, padx=10,
                                                                                        sticky='w')

    friend1_entry = Entry(ml4_wn, width=30)
    friend1_entry.grid(row=1, column=1, padx=10, pady=5)
    friend2_entry = Entry(ml4_wn, width=30)
    friend2_entry.grid(row=2, column=1, padx=10, pady=5)
    friend3_entry = Entry(ml4_wn, width=30)
    friend3_entry.grid(row=3, column=1, padx=10, pady=5)

    mode = ['car', 'bike', 'bus', 'train']
    payment = ['credit card', 'cash', 'mobile payment']
    express = ['awesome', 'fantastic', 'unbelievable']

    mode_opt = StringVar(ml4_wn)
    mode_opt.set(mode[0])
    OptionMenu(ml4_wn, mode_opt, *mode).grid(row=4, column=1, padx=10, pady=5, sticky='w')

    payment_opt = StringVar(ml4_wn)
    payment_opt.set(payment[0])
    OptionMenu(ml4_wn, payment_opt, *payment).grid(row=5, column=1, padx=10, pady=5, sticky='w')

    express_opt = StringVar(ml4_wn)
    express_opt.set(express[0])
    OptionMenu(ml4_wn, express_opt, *express).grid(row=6, column=1, padx=10, pady=5, sticky='w')

    submit_btn = Button(ml4_wn, text="Submit", background="SteelBlue", font=('Times', 12),
                        command=lambda: finish_madlib(ml4_wn, friend1_entry.get(), friend2_entry.get(),
                                                      friend3_entry.get(), mode_opt.get(), payment_opt.get(),
                                                      express_opt.get()))
    submit_btn.grid(row=7, column=0, columnspan=2, pady=20)

    ml4_wn.mainloop()


ml1 = Button(root, text='1. The Ant Accident', font=("vivaldi", 20), command=lambda: first_madlib(root),
             bg='yellow').place(x=20, y=70, height=50, width=320)
ml2 = Button(root, text='2. The Night Dinner', font=("vivaldi", 20), command=lambda: second_madlib(root),
             bg='green').place(x=20, y=130, height=50, width=320)
ml3 = Button(root, text='3. The Friendship Story', font=("vivaldi", 20), command=lambda: third_madlib(root),
             bg='RoyalBlue1').place(x=20, y=190, height=50, width=320)
ml4 = Button(root, text='4. The Three Drunkers', font=("vivaldi", 20), command=lambda: fourth_madlib(root),
             bg='red').place(x=20, y=250, height=50, width=320)

root.mainloop()
