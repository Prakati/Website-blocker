from tkinter import *
import os

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Website Blocker")

# Set background color to black
root.configure(bg='#000000')

Label(root, text='Website Blocker', font='Arial 16 bold', bg='#000000', fg='white').pack()

host_path = r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

Label(root, text='Enter Website:', font=('Arial', 12), bg='#000000', fg='white').place(x=10, y=60)
website_entry = Entry(root, font=('Arial', 10), width=25)
website_entry.place(x=140, y=60)

def block_website():
    website = website_entry.get().strip()

    if not website:
        Label(root, text='Please enter a website', font=('Arial', 10), fg='red', bg='#000000',).place(x=140, y=100)
        return

    with open(host_path, 'a') as host_file:
        host_file.write(f'\n{ip_address} {website}')

    Label(root, text=f'Blocked {website}', font=('Arial', 10), fg='green', bg='#000000').place(x=140, y=100)

block_button = Button(root, text='Block Website', font=('Arial', 12, 'bold'), pady=5, command=block_website,
                      width=15, bg='white', activebackground='black', fg='black')
block_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add some space between the buttons
Label(root, text='', bg='#000000').pack()

def unblock_website():
    website = website_entry.get().strip()

    if not website:
        Label(root, text='Please enter a website', font=('Arial', 10), fg='red', bg='#000000').place(x=140, y=180)
        return

    with open(host_path, 'r') as host_file:
        lines = host_file.readlines()

    with open(host_path, 'w') as host_file:
        for line in lines:
            if f'{ip_address} {website}' not in line:
                host_file.write(line)

    Label(root, text=f'Unblocked {website}', font=('Arial', 10), fg='green', bg='#000000').place(x=140, y=180)

unblock_button = Button(root, text='Unblock Website', font=('Arial', 12, 'bold'), pady=5, command=unblock_website,
                        width=15, bg='white', activebackground='black', fg='black')
unblock_button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
