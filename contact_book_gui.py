import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")
        
        self.contacts = {}  # Dictionary to store contact details

        # Labels and Entry Widgets for Contact Details
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.pack(pady=5)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack(pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.pack(pady=5)

        # Buttons for Different Actions
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root, width=40, height=10)
        self.contact_listbox.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name and phone and email and address:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact for {name} added successfully!")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")

    def search_contact(self):
        search_query = self.name_entry.get().strip()
        found = False
        self.contact_listbox.delete(0, tk.END)

        for name, details in self.contacts.items():
            if search_query.lower() in name.lower() or search_query == details["Phone"]:
                self.contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")
                found = True

        if not found:
            messagebox.showinfo("No Results", "No matching contacts found.")

    def update_contact(self):
        name = self.name_entry.get().strip()
        if name in self.contacts:
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
            address = self.address_entry.get().strip()

            if phone:
                self.contacts[name]["Phone"] = phone
            if email:
                self.contacts[name]["Email"] = email
            if address:
                self.contacts[name]["Address"] = address

            messagebox.showinfo("Success", f"Contact for {name} updated successfully!")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get().strip()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact for {name} deleted successfully!")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Initialize Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
