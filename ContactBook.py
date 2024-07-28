from tkinter import *
from tkinter import messagebox, simpledialog

# Initialization of main window
root = Tk()
root.geometry("925x500+300+200")
root.title("Contact Book")
root.configure(bg='navajowhite')
root.resizable(False, False)

contacts = []

def add_contact():
    name = name_entry.get()
    phone = number_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone and email and address:
        contacts.append({"name": name, "phone no": phone, "email id": email, "address": address})
        update_contact_list()
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please provide all information")

def update_contact_list():
    listbox.delete(0, END)
    for contact in contacts:
        listbox.insert(END, f"{contact['name']} - {contact['phone no']}")

def view_contacts():
    selected = listbox.curselection()
    if selected:
        contact = contacts[selected[0]]
        messagebox.showinfo("Contact Details", f"Name: {contact['name']}\nPhone: {contact['phone no']}\nEmail: {contact['email id']}\nAddress: {contact['address']}")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to view.")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
    if query:
        results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone no']]
        if results:
            listbox.delete(0, END)
            for contact in results:
                listbox.insert(END, f"{contact['name']} - {contact['phone no']}")
        else:
            messagebox.showinfo("Search Result", "No matching contacts found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a search query.")

def update_contact():
    selected = listbox.curselection()
    if selected:
        contact = contacts[selected[0]]
        name = simpledialog.askstring("Input", "Enter contact name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Input", "Enter contact phone number:", initialvalue=contact['phone no'])
        email = simpledialog.askstring("Input", "Enter contact email:", initialvalue=contact['email id'])
        address = simpledialog.askstring("Input", "Enter contact address:", initialvalue=contact['address'])
        
        if name and phone and email and address:
            contacts[selected[0]] = {"name": name, "phone no": phone, "email id": email, "address": address}
            update_contact_list()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        contacts.pop(selected[0])
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Listbox to display contacts
listbox = Listbox(root, height=30, width=40, bg='white')
listbox.pack(side=LEFT)

# Scrollbar for the Listbox
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)

# Labels and entry widgets for contact details
name_label = Label(root, text='Name:', fg='black', bg='navajowhite', font=('Microsoft YaHei UI Light', 14, 'bold'))
name_label.place(x=450, y=10)
name_entry = Entry(root, width=30, bg='white')
name_entry.place(x=520, y=20)

number_label = Label(root, text='Phone no:', fg='black', bg='navajowhite', font=('Microsoft YaHei UI Light', 14, 'bold'))
number_label.place(x=450, y=60)
number_entry = Entry(root, width=30, bg='white')
number_entry.place(x=560, y=70)

email_label = Label(root, text='Email:', fg='black', bg='navajowhite', font=('Microsoft YaHei UI Light', 14, 'bold'))
email_label.place(x=450, y=110)
email_entry = Entry(root, width=30, bg='white')
email_entry.place(x=520, y=120)

address_label = Label(root, text='Address:', fg='black', bg='navajowhite', font=('Microsoft YaHei UI Light', 14, 'bold'))
address_label.place(x=450, y=160)
address_entry = Entry(root, width=30, bg='white')
address_entry.place(x=540, y=170)

# Buttons for different operations
add_button = Button(root, text="Add Contact",bg='royalblue',activebackground='royalblue', activeforeground='black', command=add_contact)
add_button.place(x=450, y=220)

view_button = Button(root, text="View Contacts",bg='royalblue',activebackground='royalblue', activeforeground='black', command=view_contacts)
view_button.place(x=550, y=220)

search_button = Button(root, text="Search Contact",bg='royalblue',activebackground='royalblue', activeforeground='black', command=search_contact)
search_button.place(x=650, y=220)

update_button = Button(root, text="Update Contact",bg='royalblue',activebackground='royalblue', activeforeground='black', command=update_contact)
update_button.place(x=450, y=270)

delete_button = Button(root, text="Delete Contact",bg='royalblue',activebackground='royalblue', activeforeground='black', command=delete_contact)
delete_button.place(x=550, y=270)

root.mainloop()