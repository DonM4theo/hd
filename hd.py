import socket
import os
import fnmatch
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image, ImageGrab
from tkinter import *
import tkinter.ttk as ttk
from pyhooked import Hook, KeyboardEvent
import subprocess
import shutil
import tkinter.filedialog as tkf
from tkinter import messagebox
import unidecode
from tkinter import _setit

################################################################################################################################################
path = "/HD/prts/"
################################################################################################################################################
#czyści folder ze ścieżki path po restarcie aplikacji
for the_file in os.listdir(path):
    file_path = os.path.join(path, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)

    except Exception as e:
        print(e)
#################################################################################################################################################

r_address = []

to_him = open("src/send_to.dat", "r", encoding='utf8')
rows = to_him.readlines()
to_him.close()

to_him = open("src/send_to.dat", "r", encoding='utf8')
for el in rows:
    r_address.append(to_him.readline().rstrip())

to_him.close()

key_tab = []

f = open('src/hkeys.dat')
for line in f:
    key_tab.append(str(line).strip('\n'))

# key_tab = []
#
# shortcut = open("src/hkeys.dat", "r", encoding='utf8')
# place = shortcut.readlines()
# shortcut.close()
#
# shortcut = open("src/hkeys.dat", "r", encoding='utf8')
# for x in place:
#     key_tab.append(shortcut.readline().rstrip())
#
# shortcut.close()
#
# print(shortcut)

################################################################################################################################################
host_name = socket.gethostname()
user_name = os.getenv('username')
##################################################################################################################################################
text_save = []
counter = []
read_tab = []
tmp = []
tmp2 = []
count_x = []

def_branch = []

branch = open("src/default_branch.dat", "r", encoding='utf8')
lines = branch.readlines()
branch.close()

branch = open("src/default_branch.dat", "r", encoding='utf8')

for line in lines:
    def_branch.append(branch.readline().rstrip())

branch.close()

issues_list = []

z = open("src/issues_list.dat", "r", encoding='utf8')
m = z.readlines()
z.close()

z = open("src/issues_list.dat", "r", encoding='utf8')

for line in m:
    issues_list.append(z.readline().rstrip())

z.close()


def add_pop():
    tmp.append(1)
    s = 0
    pop = Toplevel()
    pop.wm_title("Dodawanie")
    pop.configure(background="#474747")
    pop.geometry("300x150")
    pop.resizable(0, 0)
    popW = pop.winfo_reqwidth()
    popH = pop.winfo_reqheight()
    posR = int(pop.winfo_screenwidth() / 2 - popW / 2)
    posD = int(pop.winfo_screenheight() / 2 - popH - 50)
    pop.geometry("+{}+{}".format(posR, posD))

    window.attributes("-topmost", False)
    pop.attributes("-topmost", True)
    pop.focus_force()

    def add_prt():
        pop_up = Toplevel()
        pop_up.geometry("150x100")
        pop_up.wm_attributes("-transparentcolor", "brown")
        pop_up.configure(bg="brown")
        pop_up.overrideredirect(1)
        pop.attributes("-topmost", False)
        pop.iconify()
        pop_up.attributes("-topmost", True)
        pop.attributes('-disabled', True)
        button_up = Button(pop_up, image=catch_p, border=0, activebackground="brown", bg="brown", command=lambda: back_to())
        windowWidth = pop_up.winfo_reqwidth()
        windowHeight = pop_up.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        positionRight = int(pop_up.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(pop_up.winfo_screenheight() / 2 + windowHeight + 150)
        pop_up.geometry("+{}+{}".format(positionRight, positionDown))
        button_up.place(relx=0.5, rely=0.5, anchor=CENTER)
        subprocess.Popen('C:\WINDOWS\system32\SnippingTool.exe', shell=True)
        window.iconify()

        def after_prt():
            pop_up.destroy()
            window.deiconify()
            # window.attributes("-topmost", True)
            window.focus_force()

        pop_up.protocol("WM_DELETE_WINDOW", after_prt)

        def back_to():
            count_x.append(1)
            pop_up.destroy()
            pop.destroy()
            window.deiconify()
            window.focus_force()
            # window.attributes("-topmost", True)
            subprocess.call('taskkill /IM SnippingTool.exe', shell=True)
            im = ImageGrab.grabclipboard()
            x = len(count_x)
            im.save('C:/HD/prts/prt' + str(x) + '.png')
            print("Zapisano atywny screen")

    def callback():
        pop.destroy()
        window.attributes("-topmost", True)

    label = Label(pop, text="Załączniki (max:3)", font="Tahoma 14", bg="#474747", fg="#eef1ea")
    label.place(anchor=N, relx=0.5)
    load = Button(pop, text="z pliku...", bg="#3d3d3d", fg="#f2e5dc", command=lambda: copy())
    load.place(relx=0.25, rely=0.6, anchor=CENTER)
    catch = Button(pop, text="przechwyć", bg="#3d3d3d", fg="#f2e5dc", command=add_prt)
    catch.place(relx=0.75, rely=0.6, anchor=CENTER)
    for el in tmp:
        s = s + el
    if s > 5:
        pop.destroy()
    pop.protocol("WM_DELETE_WINDOW", callback)

    def copy():
        pop.destroy()

        filename = tkf.askopenfilenames(initialdir="C:/Users/" + user_name + "/Desktop/", title="Wybierz pliki", filetypes=(
            ("Image Files", ("*.jpg", "*.jpeg", "*.bmp", "*png")),
            ("All", "*.*")

        ))
        lst = list(filename)
        print(lst)
        if len(lst) <= 3:
            for path in lst:
                path = str(path).replace("/", "\\")
                print(path)
                shutil.copy(path, 'C:\HD\prts\\')
            print("Done")
            pop.destroy()

            window.attributes("-topmost", True)
        else:

            messagebox.showerror("Limit error", "Przekraczasz limit : 3")

            pop.destroy()
            window.attributes("-topmost", True)


def refresh():
    os.execv(sys.executable, ['hd.py'] + sys.argv)
    key_tab.clear()


def edit():
    subprocess.Popen(r'explorer /open,"C:\HD\prts\"')


def next():
    g = str(var2.get())
    cp = 0
    path = "/HD/prts/"

    for filename in os.listdir(path):
        cp = cp + 1
    if int(cp) > 3:
        messagebox.showerror("Błąd załącznika", "Wejdź w opcję \"Edytuj\", zweryfikuj ilość plików.\nMaxymalna ilość to: 3")
        return
    elif int(cp) != int(g) and int(cp) <= 3:
        messagebox.showinfo("Załaduj załącznik", "Kliknij ikonę \"strzałki\", obok paska postępu.")
        return

    window.iconify()
    sender = Toplevel()
    sender.wm_title("Formularz zgłoszeniowy")
    sender.configure(bg="#474747")
    sender.geometry("300x600")
    sender.resizable(0, 0)
    sender.attributes("-topmost", True)
    senderW = window.winfo_reqwidth()
    senderH = window.winfo_reqheight()
    positR = int(sender.winfo_screenwidth() / 2 - senderW / 2)
    positD = int(sender.winfo_screenheight() / 2 - senderH - 130)
    sender.geometry("+{}+{}".format(positR, positD))

    def back_method():
        sender.destroy()
        window.deiconify()
        print("Lista składowa", read_tab)
        read_tab.clear()

    if "EP-NS" in def_branch[0]:
        ch_var1.set(True)
        ch_var2.set(False)
    elif "EP-BB" in def_branch[0]:
        ch_var1.set(False)
        ch_var2.set(True)
    elif "EP" in def_branch[0]:
        ch_var1.set(False)
        ch_var2.set(False)

    choice_ns = Checkbutton(sender, text="EP-NS", font="Tahoma 12", bg="#474747", fg="WHITE", activebackground="#474747", activeforeground="#2c7cff",
                            selectcolor="#474747", variable=ch_var1)

    choice_bb = Checkbutton(sender, text="EP-BB", font="Tahoma 12", bg="#474747", fg="WHITE", activebackground="#474747", activeforeground="#2c7cff",
                            selectcolor="#474747", variable=ch_var2)

    choice_ns.place(relx=0.25, rely=0.15, anchor=N)
    choice_bb.place(relx=0.75, rely=0.15, anchor=N)

    def send():
        fromaddr = "hdesk@electropoli.pl"
        toaddr = r_address

        br1 = ch_var1.get()
        br2 = ch_var2.get()

        if br1 == True and br2 == True:
            read_tab.append("NS-BB")
        elif br1 == True and br2 == False:
            read_tab.append("NS")
        elif br1 == False and br2 == True:
            read_tab.append("BB")
        elif br1 == False and br2 == False:
            messagebox.showerror("Brak oddziału", "Wybierz jeden z oddziałów firmy,bądź oba.")
            read_tab.clear()
            return

        br3 = str(user_entry.get())
        if len(br3) > 7:
            read_tab.append(br3)
        else:
            messagebox.showerror("Brak w polu 'Zgłaszający'", "Uzupełnij pole 'Zgłaszający'.")
            read_tab.clear()
            return
        br4 = str(issue_var.get())
        if "--" in br4:
            messagebox.showerror("Brak w polu 'Problem'",
                                 "Wybierz z listy odpowiedni temat problemu\nlub wybierz pozycję: 'inny',\n"
                                 "gdy pozycję z listy nie są związane z problemem.")
            read_tab.clear()
            return
        else:
            read_tab.append(br4)

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = ", ".join(toaddr)
        msg['Subject'] = (read_tab[0] + "-" + host_name + "-" + read_tab[1] + "-" + read_tab[2])

        description = str(opis_entry.get("1.0", END))
        if len(description) <= 5:
            messagebox.showerror("Brak opisu", "Uzupełnij opis zgłaszanego problemu.")
            return
        else:
            body = str(description + "\n\n\n\n\n\n\n\n\nWysłano z aplikacji hd.\nAktualnie zalogowany:" + user_name)
            msg.attach(MIMEText(body, 'plain'))

        path = "/HD/prts/"

        cf = 0

        for filename in os.listdir(path):
            cf = cf + 1
        print("Licz_cf:", cf)
        k = 0

        if int(cf) > 0:

            if int(g) == int(cf) and int(cf) <= 3:

                for filename in os.listdir(path):
                    attachment = open(path + filename, "rb")
                    name = str("A" + str(k) + "-" + "[" + str(filename).split('.')[1] + "]" + ".png")
                    filename = name
                    print(filename)
                    part = MIMEBase('application', 'png')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)
                    k += 1
        sender.attributes("-topmost", False)
        result = messagebox.askquestion("Potwierdzenie", "Czy chcesz wysłać zgłoszenie do działu IT w "
                                        + str(read_tab[0]) +".\nIlość załączników: " + g + ".")
        if result == 'no':
            print("Przerwano")
            read_tab.clear()
            return
        else:
            print("Poszedł, jak kuna w agrest")

            server = smtplib.SMTP('smtp.electropoli.pl', 587)
            # server.starttls()
            server.login(fromaddr, "mISiHgP#t04")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            messagebox.showinfo("Wysyłanie", "Zgłoszenie zostało wysłane")

            refresh()

    address = []
    list_c = []

    def secret_pass():

        sender.attributes("-topmost", False)
        password = Toplevel()
        password.attributes("-topmost", True)
        password.wm_title("Password")
        password.configure(bg="#474747")
        password.geometry("250x200")
        password.resizable(0, 0)
        password.focus_force()

        passwordW = password.winfo_reqwidth()
        passwordH = password.winfo_reqheight()
        poR = int(password.winfo_screenwidth() / 2 - passwordW / 2 + 25)
        poD = int(password.winfo_screenheight() / 2 - passwordH - 10)
        password.geometry("+{}+{}".format(poR, poD))

        pass_lab = Label(password, bg="#474747", text="PASSWORD:", font="Tahoma 10 bold", fg="WHITE")
        pass_in = Entry(password, width=20, bg="#f2e5dc", font="Tahoma 10 ", fg="BLACK", show="*")
        enter = Button(password, bg="#3d3d3d", text="Enter", font="Tahoma 10 bold", fg="ORANGE", border=0, activebackground="#474747",
                       command=lambda: secret_method())
        enter.configure(activebackground="YELLOW")

        pass_lab.place(relx=0.5, rely=0.1, anchor=N)
        pass_in.place(relx=0.5, rely=0.25, anchor=N)
        enter.place(relx=0.5, rely=0.55, anchor=N)

        def interrupt():
            password.destroy()
            sender.attributes("-topmost", True)

        password.protocol("WM_DELETE_WINDOW", interrupt)

        def secret_method():
            if pass_in.get() != "it8800":
                pass_in.delete(0, 'end')
                messagebox.showerror("Niepoprawne hasło", "Wprowadź poprawne hasło lub zrezygnuj")
            else:
                password.destroy()
                sender.destroy()

                def zaczytaj():
                    read_address = open("src/address_list.dat", "r", encoding='utf8')
                    liness = read_address.readlines()
                    read_address.close()

                    read_address = open("src/address_list.dat", "r", encoding='utf8')
                    address.clear()
                    for el in liness:
                        address.append(read_address.readline().rstrip())

                    read_address.close()

                zaczytaj()
                print("Ołłłł yeah")
                secret = Toplevel()
                secret.wm_title("Wyślij do")
                secret.configure(bg="#474747")
                secret.geometry("320x600")
                secret.resizable(0, 0)

                secretW = secret.winfo_reqwidth()
                secretH = secret.winfo_reqheight()
                pR = int(secret.winfo_screenwidth() / 2 - secretW / 2 - 10)
                pD = int(secret.winfo_screenheight() / 2 - secretH - 130)
                secret.geometry("+{}+{}".format(pR, pD))

                def send_pro():
                    k = 0
                    recipient = []
                    body = ""

                    fromaddr = "hdesk@fdgfd.pl"

                    msg = MIMEMultipart()

                    msg['From'] = fromaddr
                    for id in range(list_tmp.size()):
                        recipient.append(str(list_tmp.get(id)))
                    print("recipient:", recipient)
                    toaddr = recipient
                    msg['To'] = ", ".join(toaddr)

                    msg['Subject'] = (host_name + "-" + title_var.get())

                    for lin in text_save:
                        body = body + lin + "\n"
                    body = (body + "\n\n\n\n\n\n\n\n\nWysłano z aplikacji hd.\nAktualnie zalogowany:" + user_name)
                    print("body:\n", body)
                    msg.attach(MIMEText(body, 'plain'))

                    path = "/HD/prts/"

                    def get_size(start_path=path):
                        total_size = 0
                        for dirpath, dirnames, filenames in os.walk(start_path):
                            for f in filenames:
                                fp = os.path.join(dirpath, f)
                                total_size += os.path.getsize(fp)
                        return total_size

                    if get_size() <= 11534336:
                        print("rozmiar załącznika:", get_size())
                        for filename in os.listdir(path):
                            attachment = open(path + filename, "rb")
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload((attachment).read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                            msg.attach(part)
                            k += 1

                    else:
                        print("o chopie", get_size())
                        messagebox.showerror("Za duży załącznik", "Limit na załączane pliki to: 11MB (sumarycznie)."
                                                                  "\nPrzejdź do edycji i sprawdź wielkość załączanych plików")
                        return

                    if len(recipient) == 0:
                        messagebox.showerror("Brak adresata", "Dodaj conajmniej jednego adresata")
                        return

                    weight = (get_size()/1024)

                    if weight < 1024:
                        weight = float(get_size()/1024)
                        weight_str = (str(round(weight, 2)) + "KB")
                    elif weight >= 1024:
                        weight = weight/1024
                        weight_str = (str(round(weight, 2)) + "MB")
                    secret.attributes("-topmost", False)
                    result_pro = messagebox.askquestion("Potwierdzenie", "Czy chcesz wysłać wiadomość do: " + str(recipient) + "\n\nZaładowano: "
                                                        + weight_str + " załącznika.\nDługość wiadomości tekstowej to: "
                                                        + str(len(text_save)) + " linii/e")
                    if result_pro == 'no':
                        print("Przerwano")
                        return
                    else:
                        print("Poszedł, jak kuna w agrest")

                    server = smtplib.SMTP('smtp.electropoli.pl', 587)
                    server.login(fromaddr, "mISiHgP#t04")
                    text = msg.as_string()
                    server.sendmail(fromaddr, toaddr, text)
                    server.quit()
                    messagebox.showinfo("Wiadomość", "Wiadomość została wysłana")

                    # for filename in os.listdir(path):
                    #     os.remove(path + filename)
                    refresh()

                def reload():
                    os.system('cls')
                    list_tmp.delete(0, 'end')
                    for item in list_c:
                        print("IDDDDD:", list_c.index(item), "--", item)
                        list_tmp.insert(list_c.index(item), item)

                    for i in range(0, list_tmp.size(), 1):
                        print("Dodano--", list_tmp.get(i))

                    return

                def get_in():
                    check_address = address_var.get()
                    if check_address in list_c:
                        return
                    elif "--" in check_address:
                        return
                    else:
                        list_c.append(check_address)
                        reload()

                ends = ["pl", "com", "org", "net", "info", "de", "fr"]

                def ok_new(value):
                    address_var.set(value)

                def fresh_up():
                    address.clear()
                    read_current = open("src/address_list.dat", "r", encoding='utf8')
                    lin = read_current.readlines()
                    read_current.close()
                    read_current = open("src/address_list.dat", "r", encoding='utf8')
                    for l in lin:
                        address.append(read_current.readline().rstrip())
                    read_current.close()


                def get_in2():
                    check_address = unidecode.unidecode(new_entry.get())
                    if check_address in list_c:
                        return
                    ch_ad = str(check_address).split(' ')
                    zx2 = str(ch_ad).split('@')
                    zx = str(zx2[-1]).split('.')

                    if ".." in check_address:
                        messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\n(np. JanKowalski@firma.pl")
                    elif ".@" in check_address:
                        messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\n(np. JanKowalski@firma.pl")
                    elif "@." in check_address:
                        messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\n(np. JanKowalski@firma.pl")
                    else:
                        if len(ch_ad) > 1:
                            messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\n(np. JanKowalski@firma.pl")
                            return
                        else:
                            if "@" in check_address and "." in check_address:
                                if len(zx2) == 2 and "." in zx2[-1]:

                                    if len(zx) > 1 and zx[-1][:-2] in ends:            ######################BreakPoint

                                        if ch_var3.get() == True:
                                            if str(unidecode.unidecode(new_entry.get())).lower() in str(address).lower():
                                                messagebox.showinfo("Dodawanie kontaktu", "Kontakt znajduje się już na liście adresowej.")
                                                new_entry.delete(0, 'end')
                                                ch_var3.set(False)
                                                return
                                            else:
                                                with open("src/address_list.dat", "a", encoding='utf8') as file:
                                                    file.write("\n" + str(unidecode.unidecode(new_entry.get())))
                                                    list_c.append(check_address)

                                                    file.close()
                                                    ch_var3.set(False)
                                                    fresh_up()
                                                    address.append(check_address)
                                                    fresh_up()
                                                    receiver_add['menu'].insert('end', 'command', label=check_address,
                                                                                command=_setit(address_var, check_address, ok_new(check_address)))

                                        else:
                                            list_c.append(check_address)

                                        reload()
                                        new_entry.delete(0, 'end')
                                    else:
                                        messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\nDopuszczalne rozszerzenia:\n"
                                                                                    "(.pl, .com, .org, .net, .info, .de, .fr)")
                                        return
                                else:
                                    messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\n(np. JanKowalski@firma.pl")
                                    return
                            else:
                                messagebox.showerror("Błędny adres e-mail", "Podaj prawidłowy adres e-mail.\n(np. JanKowalski@firma.pl")
                                return

                    print("zx:", zx, "\nzx[-1]:", zx[-1])
                    print(address)
                    print("lista_c", list_c)

                def get_out():

                    selection = list_tmp.curselection()
                    print("Lista selection - ", selection)
                    pos = 0
                    for i in selection:
                        idx = int(i) - pos
                        rem = list_tmp.get(idx)
                        print("Pacjent do usunięcia z list_c", rem)
                        list_c.remove(rem)
                        print("Usunięto pomyślnie:", rem)
                        list_tmp.delete(idx, idx)
                        pos = pos + 1

                    print("Ile niedobitków:", list_tmp.size())

                def add_message():

                    secret.attributes("-topmost", False)
                    mess = Toplevel()
                    mess.attributes("-topmost", True)
                    mess.wm_title("Wiadomość")
                    mess.configure(bg="#474747")
                    mess.geometry("300x450")
                    mess.resizable(0, 0)
                    mess.focus_force()

                    messW = mess.winfo_reqwidth()
                    messH = mess.winfo_reqheight()
                    positiR = int(mess.winfo_screenwidth() / 2 - messW / 2)
                    positiD = int(mess.winfo_screenheight() / 2 - messH - 50)
                    mess.geometry("+{}+{}".format(positiR, positiD))

                    labb1 = Label(mess, text="Tytuł:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
                    labb2 = Label(mess, text="Wiadomość:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
                    entry1 = Entry(mess, width=34, bg="#f2e5dc", font="Tahoma 10 ", fg="BLACK", textvariable=title_var)
                    text1 = Text(mess, height=12, width=30, bg="#f2e5dc", font="Times 12", wrap=WORD)
                    butt2 = Button(mess, text="Zapisz", font="Tahoma 16 bold", bg="#3d3d3d", fg="GREEN", border=0, activebackground="#474747",
                                   command=lambda: save())
                    butt2.configure(activeforeground="YELLOW")
                    scroll = Scrollbar(mess)
                    text1.config(yscrollcommand=scroll.set)
                    scroll.config(command=text1.yview)

                    labb1.place(relx=0.08, rely=0.05, anchor=NW)
                    entry1.place(relx=0.05, rely=0.1, anchor=NW)
                    labb2.place(relx=0.08, rely=0.15, anchor=NW)
                    text1.place(relx=0.05, rely=0.20, anchor=NW)
                    scroll.place(in_=text1, relx=1.0, relheight=1.0, bordermode="outside")
                    butt2.place(relx=0.5, rely=0.9, anchor=S)

                    print("counter1:", len(counter))
                    counter.append(1)
                    print("counter2:", len(counter))

                    if len(counter) > 1:
                        print("counter3(if):", len(counter))
                        for el in text_save:
                            text1.insert(END, str(el) + "\n")

                    def save():
                        text_save.clear()
                        title_var.set(entry1.get())
                        clip = str(text1.get("1.0", END)).split("\n")
                        print(clip)
                        for el in clip:
                            text_save.append(el)
                        print(text_save)
                        mess.destroy()
                        secret.deiconify()
                        secret.attributes("-topmost", True)

                    def to_secret():
                        mess.destroy()
                        secret.deiconify()
                        secret.attributes("-topmost", False)

                    mess.protocol("WM_DELETE_WINDOW", to_secret)

                lab_admin = Label(secret, text="Wysyłanie - admin:", font="Tahoma 16 bold", fg="WHITE", bg="#474747")
                lab1 = Label(secret, text="Wybierz z listy:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
                receiver_add = OptionMenu(secret, address_var, *address[1::])
                receiver_add.configure(width=34, border=0, bg="#f2e5dc")

                address_var.set(address[0])
                add = Button(secret, text="+", font="Tahoma 20 bold", fg="GREEN", bg="#474747", activebackground="#474747", border=0, command=get_in)
                add.configure(activeforeground="YELLOW")
                add2 = Button(secret, text="+", font="Tahoma 20 bold", fg="GREEN", bg="#474747", activebackground="#474747", border=0,
                              command=get_in2)
                add2.configure(activeforeground="YELLOW")
                sub = Button(secret, text="-", font="Tahoma 24 bold", fg="RED", bg="#474747", activebackground="#474747", border=0, command=get_out)
                sub.configure(activeforeground="YELLOW")
                lab2 = Label(secret, text="Spoza listy:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
                check_save = Checkbutton(secret, text="Zapisz kontakt", font="Tahoma 10 ", fg="WHITE", bg="#474747", variable=ch_var3,
                                         activebackground="#474747", activeforeground="#2c7cff", selectcolor="#474747")
                list_tmp = Listbox(secret, width=34, height=12, bg="#f2e5dc", font="Tahoma 10 ", fg="BLACK", selectmode='multiple')
                new_entry = Entry(secret, width=34, bg="#f2e5dc", font="Tahoma 10 ", fg="BLACK")
                attach = Button(secret, text="Dodaj", font="Tahoma 10 bold", bg="#3d3d3d", fg="GREEN", border=0, activebackground="#474747",
                                command=add_pop)
                attach.configure(activeforeground="YELLOW")
                editt = Button(secret, text="Edytuj", font="Tahoma 10 bold", bg="#3d3d3d", fg="ORANGE", border=0, activebackground="#474747",
                               command=edit)
                editt.configure(activeforeground="YELLOW")
                send_out = Button(secret, text="Dodaj", font="Tahoma 10 bold", bg="#474747", fg="WHITE", image=send_p, border=0,
                                  activebackground="#474747", command=send_pro)
                lab3 = Label(secret, text="Adresat:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
                lab4 = Label(secret, text="Załączniki:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
                bt = Button(secret, text="+ Dodaj wiadomość", font="Tahoma 10 bold", bg="#3d3d3d", fg="GREEN", border=0, activebackground="#474747",
                            command=lambda: add_message())
                bt.configure(activeforeground="YELLOW")
                ################################################################################################################################################

                ################################################################################################################################################
                lab_admin.place(relx=0.5, anchor=N)
                lab1.place(relx=0.05, rely=0.1, anchor=NW)
                receiver_add.place(relx=0.08, rely=0.15, anchor=NW)
                add.place(relx=0.855, rely=0.125, anchor=NW)
                lab2.place(relx=0.05, rely=0.22, anchor=NW)
                check_save.place(relx=0.09, rely=0.31, anchor=NW)
                new_entry.place(relx=0.08, rely=0.27, anchor=NW)
                add2.place(relx=0.855, rely=0.24, anchor=NW)
                lab3.place(relx=0.05, rely=0.4, anchor=NW)
                list_tmp.place(relx=0.08, rely=0.45, anchor=NW)
                sub.place(relx=0.855, rely=0.57, anchor=NW)
                lab4.place(relx=0.2, rely=0.9, anchor=S)
                attach.place(relx=0.05, rely=0.97, anchor=SW)
                editt.place(relx=0.3, rely=0.97, anchor=S)
                send_out.place(relx=0.95, rely=0.972, anchor=SE)
                bt.place(relx=0.08, rely=0.85, anchor=SW)

                def to_main():
                    secret.destroy()
                    window.deiconify()
                    list_c.clear()

                secret.protocol("WM_DELETE_WINDOW", to_main)

    ################################################################################################################################################

    branch_label = Label(sender, text="Oddział:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
    user_label = Label(sender, text="Zgłaszający (Imię Nazwisko):", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
    topic_label = Label(sender, text="Problem:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")
    opis_label = Label(sender, text="Opis:", font="Tahoma 10 bold", fg="#0099CC", bg="#474747")

    choice_issue = OptionMenu(sender, issue_var, *issues_list[1::])
    choice_issue.configure(width=34, border=0, bg="#f2e5dc")
    issue_var.set(issues_list[0])
    opis_entry = Text(sender, height=12, width=30, bg="#f2e5dc", font="Times 12", wrap=WORD)
    user_entry = Entry(sender, bg="#f2e5dc", font="Times 12", justify=LEFT, width=30)
    back_button = Button(sender, text="Back", bg="#474747", border=0, activebackground="#474747", image=back_p, command=back_method)
    send_button = Button(sender, text="Send", bg="#474747", border=0, activebackground="#474747", image=send_p, command=send)
    send_label = Label(sender, text="Wypełnij formularz zgłoszeniowy", font="Tahoma 14", bg="#474747", fg="WHITE")
    attached = Label(sender, text="Ilość załączników:   ", font="Tahoma 10 bold", bg="#474747", fg="WHITE")
    secret = Button(sender, text=g, font="Tahoma 10 bold", bg="#474747", fg="WHITE", activebackground="#474747", border=0, command=secret_pass)
    secret.configure(activeforeground="WHITE")
    scrollbar = Scrollbar(sender)
    opis_entry.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=opis_entry.yview)

    attached.place(relx=0.5, rely=0.98, anchor=CENTER)
    secret.place(relx=0.7, rely=0.98, anchor=CENTER)
    scrollbar.place(in_=opis_entry, relx=1.0, relheight=1.0, bordermode="outside")
    opis_label.place(relx=0.05, rely=0.465, anchor=NW)
    opis_entry.place(relx=0.08, rely=0.51, anchor=NW)
    topic_label.place(relx=0.05, rely=0.35, anchor=NW)
    choice_issue.place(relx=0.08, rely=0.4, anchor=NW)
    branch_label.place(relx=0.05, rely=0.1, anchor=NW)
    user_label.place(relx=0.05, rely=0.25, anchor=NW)
    user_entry.place(relx=0.08, rely=0.30, anchor=NW)
    send_label.place(relx=0.5, anchor=N)
    back_button.place(relx=0.05, rely=0.97, anchor=SW)
    send_button.place(relx=0.95, rely=0.97, anchor=SE)

    sender.protocol("WM_DELETE_WINDOW", back_method)


step = {'0': '0', '1': '33', '2': '66', '3': '98.99'}


def upload():
    f_count = 0

    tab = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    for el in tab:
        f = len(fnmatch.filter(os.listdir('C:\HD\prts'), el))
        print(f)
        f_count = f_count + f
    print("Ilość załączników:", f_count)

    if f_count <= 3:
        var2.set(f_count)
        t = str(var2.get())
        var.set(step[t])
        amount_bar.step()
    else:
        messagebox.showerror("Limit error", "Przekraczasz limit : 3\nPrzejdź do zakładki: 'Edytuj'")

    style.configure('text.Horizontal.TProgressbar',
                    text='{:g} / 3'.format(var2.get()))  # update label

    window.after(200)


################################################################################################################################################
# Pierwsze okno

window = Tk()
window.title("Zgłoszenie do IT")
window.configure(bg="#474747")
window.geometry("300x300")
window.resizable(0, 0)
windowW = window.winfo_reqwidth()
windowH = window.winfo_reqheight()
positionR = int(window.winfo_screenwidth() / 2 - windowW / 2)
positionD = int(window.winfo_screenheight() / 2 - windowH - 100)
window.geometry("+{}+{}".format(positionR, positionD))
window.attributes("-topmost", True)

next_p = PhotoImage(file="icon/arrow.png")
cancel_p = PhotoImage(file="icon/cancel.png")
refresh_p = PhotoImage(file="icon/refresh.png")
upload_p = PhotoImage(file="icon/upload.png")
back_p = PhotoImage(file="icon/back.png")
send_p = PhotoImage(file="icon/send.png")
catch_p = PhotoImage(file="icon/red_confirm.png")


################################################################################################################################################

window.protocol("WM_DELETE_WINDOW", refresh)
################################################################################################################################################


style = ttk.Style(window)
style.layout('text.Horizontal.TProgressbar',
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}),
              ('Horizontal.Progressbar.label', {'sticky': ''})])

style.configure('text.Horizontal.TProgressbar', text='0 / 3')

var = IntVar()
var2 = IntVar()
ch_var1 = BooleanVar()
ch_var2 = BooleanVar()
issue_var = StringVar()
address_var = StringVar()
ch_var3 = BooleanVar()
title_var = StringVar()

amount_bar = ttk.Progressbar(window, length="200", variable=var, style='text.Horizontal.TProgressbar', orient="horizontal",
                             mode="determinate")

prt_label = Label(window, text="Załączniki", font="Tahoma 16", width="300", fg="#0099CC", bg="#3d3d3d")

amount_bar_label = Label(window, text="Ilość dodanych załączników:", font="Tahoma 10", bg="#474747", fg="#eef1ea")
add_button = Button(window, width="11", text="Dodaj nowy", font="Tahoma 10", command=add_pop)
edit_button = Button(window, width="11", text="Edytuj", font="Tahoma 10", command=edit)
next_button = Button(window, border=0, text="Dalej", bg="#474747", activebackground="#474747", image=next_p, command=next)
cancel_button = Button(window, border=0, text="Exit", bg="#474747", activebackground="#474747", image=cancel_p, command=refresh)
refresh_button = Button(window, text="Restart", bg="#474747", border=0, activebackground="#474747", image=refresh_p, command=refresh)
upload_button = Button(window, text="Upload", bg="#474747", border=0, activebackground="#474747", image=upload_p, command=upload)

################################################################################################################################################

prt_label.place(relx=0.5, rely=0.1, anchor=N)
amount_bar.place(relx=0.5, rely=0.65, anchor=CENTER)
amount_bar_label.place(relx=0.44, rely=0.57, anchor=CENTER)
upload_button.place(relx=0.92, rely=0.636, anchor=CENTER)

add_button.place(relx=0.25, rely=0.4, anchor=CENTER)
edit_button.place(relx=0.75, rely=0.4, anchor=CENTER)
next_button.place(relx=0.95, rely=0.95, anchor=SE)
cancel_button.place(relx=0.05, rely=0.95, anchor=SW)
refresh_button.place(relx=0.5, rely=0.95, anchor=S)

################################################################################################################################################


def handle_events(args):
    key0 = str(key_tab[0])
    key1 = str(key_tab[1])

    if isinstance(args, KeyboardEvent):
        if args.current_key == '1' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print("Host name:", host_name, "\nUser name:", user_name)

        elif args.current_key == key1 and args.event_type == 'key down' and key0 in args.pressed_key:
            window.mainloop()
            hk.stop()


hk = Hook()  # make a new instance of PyHooked
hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
hk.hook()  # hook into the events, and listen to the presses
