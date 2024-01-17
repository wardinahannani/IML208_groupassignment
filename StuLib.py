import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Student Library Login")
window.geometry('500x500')
window.configure(bg='#333333')

def login():
    username = "Ammar"
    password = "2022"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()
        class StudentLibraryApp:
            def __init__(self, root):
                self.root = root
                self.root.title("Welcome to Student Library")
                self.root.geometry("600x400")
                #self.root.state('zoomed')  # Maximize the window
                self.root.configure(bg='silver')
                
                image_path = "wallib.jpg"  # Replace with the path to your image
                self.background_image = Image.open(image_path)
                self.background_photo = ImageTk.PhotoImage(self.background_image)
        
                self.background_label = tk.Label(root, image=self.background_photo)
                self.background_label.place(relwidth=1, relheight=1)

                # Initialize the lists to store loaned books, interlibrary loans, and meeting room reservations
                self.loaned_books = []
                self.interlibrary_loans = []
                self.meeting_room_reservations = []

                # Title
                title_label = tk.Label(root, text=("Welcome to StuLib", username,"!"), bg='orange', font=("Helvetica", 20))
                title_label.pack(side=tk.TOP, pady=20)

                # Subtitle
                subtitle_label = tk.Label(root, text="Please choose an option below", bg='orange', font=("Helvetica", 16))
                subtitle_label.pack(side=tk.TOP, pady=10)

                # Buttons
                buttons_frame = tk.Frame(root, bg='brown')  # Create a frame to hold the buttons
                buttons_frame.pack(pady=20)

                book_loan_button = tk.Button(buttons_frame, text="Book Loan", bg='orange', command=self.book_loan_window)
                book_loan_button.pack(side=tk.LEFT, padx=10)

                interlibrary_loan_button = tk.Button(buttons_frame, text="Interlibrary Loan", bg='orange', command=self.interlibrary_loan_window)
                interlibrary_loan_button.pack(side=tk.LEFT, padx=10)

                meeting_room_reservation_button = tk.Button(buttons_frame, text="Meeting Room Reservation", bg='orange', command=self.meeting_room_reservation_window)
                meeting_room_reservation_button.pack(side=tk.LEFT, padx=10)

            def dummy_function(self):
                messagebox.showinfo("Not Implemented", "This feature is not implemented yet.")

            def book_loan_window(self):
                book_loan_window_due_date = datetime.now() + timedelta(days=14)  # Due date set to 14 days from today
                book_loan_window = tk.Toplevel(self.root)
                book_loan_window.title("Book Loan")
                book_loan_window.geometry("600x400")
                book_loan_window.configure(bg='silver')

                # Label and Entry widgets for user input
                tk.Label(book_loan_window, text="Please Insert the Required Information Below", bg='lime', font=("Helvetica", 14)).pack(pady=10)

                tk.Label(book_loan_window, bg='lime', text="Book Title").pack()
                book_title_entry = tk.Entry(book_loan_window, width=30)
                book_title_entry.pack(pady=5)

                tk.Label(book_loan_window, bg='lime', text="ISBN").pack()
                isbn_entry = tk.Entry(book_loan_window, width=30)
                isbn_entry.pack(pady=5)

                tk.Label(book_loan_window, bg='lime', text="Author").pack()
                author_entry = tk.Entry(book_loan_window, width=30)
                author_entry.pack(pady=5)

                # Create a DateEntry widge

                date_frame = tk.Frame(book_loan_window, bg='lime')
                date_frame.pack(pady=10)

                date_label = tk.Label(date_frame, text="Due Date", bg='lime')
                date_label.pack(pady=5)

                date_entry = DateEntry(date_frame, width=30, date_pattern="yyyy-mm-dd")
                date_entry.pack(pady=5)


                # Buttons
                register_button = tk.Button(book_loan_window, text="Register", bg='lime',
                                                command=lambda: self.register_book_data(book_loan_window, book_title_entry.get(), isbn_entry.get(), author_entry.get(), date_entry.get()))
                register_button.pack(pady=10)


                see_loaned_books_button = tk.Button(book_loan_window, text="See Currently Loaned Books", bg= 'lime', command=lambda: self.see_loaned_books())
                see_loaned_books_button.pack()

            def get_due_date(self, window, date_entry):
                try:
                    selected_date = date_entry.get_date()
                    messagebox.showinfo("Due Date Selected", f"Due Date selected: {selected_date}")
                except ValueError:
                    messagebox.showerror("Error", "Please select a due date.")
            
            def register_book_data(self, window, book_title, isbn, author, due_date):
                if book_title and isbn and author and due_date:
                    book_data = f"Book Title: {book_title} - ISBN: {isbn} - Author: {author} - Due Date: {due_date}"
                    self.loaned_books.append(book_data)
                    messagebox.showinfo("Registration Successful", "Data has been registered successfully.")
                    window.destroy()  # Close the registration window
                else:
                    messagebox.showerror("Error", "Please fill in all the required fields.")


            def interlibrary_loan_window(self):
                interlibrary_loan_window = tk.Toplevel(self.root)
                interlibrary_loan_window.title("Interlibrary Loan")
                interlibrary_loan_window.geometry("600x500")
                interlibrary_loan_window.configure(bg= 'silver')

                # Label and Entry widgets for user input
                tk.Label(interlibrary_loan_window, text="Please Insert the Required Information Below", bg= 'cyan', font=("Helvetica", 14)).pack(pady=10)

                tk.Label(interlibrary_loan_window, bg= 'cyan', text="Library Name").pack()
                library_name_entry = tk.Entry(interlibrary_loan_window, width=30)
                library_name_entry.pack(pady=5)

                tk.Label(interlibrary_loan_window, bg= 'cyan', text="State").pack()
                state_entry = tk.Entry(interlibrary_loan_window, width=30)
                state_entry.pack(pady=5)

                tk.Label(interlibrary_loan_window, bg= 'cyan', text="Country").pack()
                country_entry = tk.Entry(interlibrary_loan_window, width=30)
                country_entry.pack(pady=5)

                tk.Label(interlibrary_loan_window, bg= 'cyan', text="Book Title").pack()
                book_title_entry = tk.Entry(interlibrary_loan_window, width=30)
                book_title_entry.pack(pady=5)
                
                tk.Label(interlibrary_loan_window, bg= 'cyan', text="ISBN").pack()
                isbn_entry = tk.Entry(interlibrary_loan_window, width=30)
                isbn_entry.pack(pady=5)

                tk.Label(interlibrary_loan_window, bg= 'cyan', text="Author").pack()
                author_entry = tk.Entry(interlibrary_loan_window, width=30)
                author_entry.pack(pady=5)

                # Buttons
                register_button = tk.Button(interlibrary_loan_window, text="Register", bg= 'cyan', command=lambda: self.register_interlibrary_loan_data(interlibrary_loan_window, library_name_entry.get(), state_entry.get(), country_entry.get(), book_title_entry.get(), isbn_entry.get(), author_entry.get()))
                register_button.pack(pady=10)

                see_loaned_books_button = tk.Button(interlibrary_loan_window, text="See Currently Loaned Books", bg= 'cyan', command=lambda: self.see_interlibrary_loans())
                see_loaned_books_button.pack()

            def register_interlibrary_loan_data(self, window, library_name, state, country, book_title, isbn, author):
                interlibrary_loan_data = f"Library Name: {library_name} - State: {state} - Country: {country} - Book Title: {book_title} - ISBN: {isbn} - Author: {author}"
                self.interlibrary_loans.append(interlibrary_loan_data)
                messagebox.showinfo("Registration Successful", "Data has been registered successfully.")
                window.destroy()  # Close the registration window

            def see_interlibrary_loans(self):
                interlibrary_loans_window = tk.Toplevel(self.root)
                interlibrary_loans_window.title("Currently Loaned Interlibrary Books")
                interlibrary_loans_window.geometry("600x400")
                interlibrary_loans_window.configure(bg= "silver")

                tk.Label(interlibrary_loans_window, text="List of Currently Loaned Interlibrary Books", bg= 'cyan', font=("Helvetica", 14)).pack(pady=10)

                # Listbox to display interlibrary loans
                listbox = tk.Listbox(interlibrary_loans_window, bg= 'cyan', selectmode=tk.BROWSE)
                for item in self.interlibrary_loans:
                    listbox.insert(tk.END, item)

                listbox.pack(pady=10)
                listbox.bind("<Double-Button-1>", lambda event: self.show_options_window_interlibrary(listbox.get(tk.ACTIVE)))

            def show_options_window_interlibrary(self, selected_item):
                options_window = tk.Toplevel(self.root)
                options_window.title("What do you wish to do?")
                options_window.geometry("300x150")
                options_window.configure(bg= "silver")

                tk.Label(options_window, text="What do you wish to do?", bg= 'cyan', font=("Helvetica", 14)).pack(pady=10)

                edit_button = tk.Button(options_window, bg= 'cyan', text="Edit Data", command=lambda: self.edit_data_interlibrary(selected_item))
                edit_button.pack(pady=5)

                delete_button = tk.Button(options_window, bg= 'cyan', text="Delete Data", command=lambda: self.confirm_delete_interlibrary(selected_item))
                delete_button.pack(pady=5)

            def edit_data_interlibrary(self, selected_item):
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Data")
                edit_window.geometry("400x400")
                edit_window.configure(bg= "silver")

                data_parts = selected_item.split(" - ")

                tk.Label(edit_window, bg= 'cyan', text="Library Name").pack()
                library_name_var = tk.StringVar()
                library_name_var.set(data_parts[0].split(":")[1].strip())
                edited_library_name_entry = tk.Entry(edit_window, width=30, textvariable=library_name_var)
                edited_library_name_entry.pack(pady=5)


                tk.Label(edit_window, bg= 'cyan', text="State").pack()
                state_var = tk.StringVar()
                state_var.set(data_parts[1].split(":")[1].strip())
                edited_state_entry = tk.Entry(edit_window, width=30, textvariable=state_var)
                edited_state_entry.pack(pady=5)

                tk.Label(edit_window, bg= 'cyan', text="Country").pack()
                country_var = tk.StringVar()
                country_var.set(data_parts[2].split(":")[1].strip())
                edited_country_entry = tk.Entry(edit_window, width=30, textvariable=country_var)
                edited_country_entry.pack(pady=5)

                tk.Label(edit_window, bg= 'cyan', text="Book Title").pack()
                book_title_var = tk.StringVar()
                book_title_var.set(data_parts[3].split(":")[1].strip())
                edited_title_entry = tk.Entry(edit_window, width=30, textvariable=book_title_var)
                edited_title_entry.pack(pady=5)

                tk.Label(edit_window, bg= 'cyan', text="ISBN").pack()
                isbn_var = tk.StringVar()
                isbn_var.set(data_parts[4].split(":")[1].strip())
                edited_isbn_entry = tk.Entry(edit_window, width=30, textvariable=isbn_var)
                edited_isbn_entry.pack(pady=5)

                tk.Label(edit_window, bg= 'cyan', text="Author").pack()
                author_var = tk.StringVar()
                author_var.set(data_parts[5].split(":")[1].strip())
                edited_author_entry = tk.Entry(edit_window, width=30, textvariable=author_var)
                edited_author_entry.pack(pady=5)

                # Button to save changes
                save_button = tk.Button(edit_window, text="Done Editing", bg= 'cyan', command=lambda: self.save_edited_data_interlibrary(selected_item, library_name_var.get(), state_var.get(), country_var.get(), book_title_var.get(), isbn_var.get(), author_var.get()))
                save_button.pack(pady=10)

            def save_edited_data_interlibrary(self, old_data, edited_library_name, edited_state, edited_country, edited_title, edited_isbn, edited_author):
                edited_data = f"Library Name: {edited_library_name} - State: {edited_state} - Country: {edited_country} - Book Title: {edited_title} - ISBN: {edited_isbn} - Author: {edited_author}"
                self.interlibrary_loans.remove(old_data)
                self.interlibrary_loans.append(edited_data)
                messagebox.showinfo("Edit Successful", "Data has been edited successfully.")

            def confirm_delete_interlibrary(self, selected_item):
                confirm_delete_window = tk.Toplevel(self.root)
                confirm_delete_window.title("Confirm Deletion")
                confirm_delete_window.geometry("300x150")
                confirm_delete_window.configure(bg= "silver")

                tk.Label(confirm_delete_window, text=f"Are you sure you want to delete:\n{selected_item}?", bg= 'cyan', font=("Helvetica", 12)).pack(pady=10)

                yes_button = tk.Button(confirm_delete_window, text="Yes", bg= 'cyan', command=lambda: self.delete_data_interlibrary(selected_item))
                yes_button.pack(pady=5)

                no_button = tk.Button(confirm_delete_window, text="No", bg= 'cyan', command=confirm_delete_window.destroy)
                no_button.pack(pady=5)

            def delete_data_interlibrary(self, selected_item):
                self.interlibrary_loans.remove(selected_item)
                messagebox.showinfo("Deletion Successful", "Data has been deleted successfully.")


            def meeting_room_reservation_window(self):
                meeting_room_reservation_window = tk.Toplevel(self.root)
                meeting_room_reservation_window.title("Meeting Room Reservation")
                meeting_room_reservation_window.geometry("600x400")
                meeting_room_reservation_window.configure(bg= "silver")

                # Label and Entry widgets for user input
                tk.Label(meeting_room_reservation_window, text="Please Insert the Required Information Below", bg='Yellow',
                        font=("Helvetica", 14)).pack(pady=10)

                tk.Label(meeting_room_reservation_window, bg='Yellow', text="Date (Day/Month/Year)").pack()

                # Use the DateEntry widget for a calendar picker
                date_entry = DateEntry(meeting_room_reservation_window, width=30, date_pattern="dd/mm/yyyy")
                date_entry.pack(pady=5)

                tk.Label(meeting_room_reservation_window, bg='Yellow', text="Day").pack()
                day_var = tk.StringVar()
                day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                day_var.set(day_options[0])  # Default value
                day_menu = tk.OptionMenu(meeting_room_reservation_window, day_var, *day_options)
                day_menu.pack(pady=5)

                tk.Label(meeting_room_reservation_window, bg='Yellow', text="Duration").pack()
                duration_var = tk.StringVar()
                duration_options = ["1 hour", "2 hours", "3 hours"]
                duration_var.set(duration_options[0])  # Default value
                duration_menu = tk.OptionMenu(meeting_room_reservation_window, duration_var, *duration_options)
                duration_menu.pack(pady=5)

                tk.Label(meeting_room_reservation_window, bg='Yellow', text="Time of Reservation").pack()
                time_entry = tk.Entry(meeting_room_reservation_window, width=30)
                time_entry.pack(pady=5)

                tk.Label(meeting_room_reservation_window, bg='Yellow', text="Room").pack()
                room_var = tk.StringVar()
                room_options = ["Small Room (S-1)", "Small Room (S-2)", "Small Room (S-3)", "Small Room (S-4)", "Small Room (S-5)",
                                "Big Room (B-1)", "Big Room (B-2)", "Big Room (B-3)", "Big Room (B-4)", "Big Room (B-5)"]
                room_var.set(room_options[0])  # Default value
                room_menu = tk.OptionMenu(meeting_room_reservation_window, room_var, *room_options)
                room_menu.pack(pady=5)

                # Buttons
                register_button = tk.Button(meeting_room_reservation_window, text="Register", bg='Yellow',
                                            command=lambda: self.register_meeting_room_reservation_data(meeting_room_reservation_window,
                                                                                                    date_entry.get(),
                                                                                                    day_var.get(),
                                                                                                    duration_var.get(),
                                                                                                    time_entry.get(),
                                                                                                    room_var.get()))
                register_button.pack(pady=10)

                see_reservations_button = tk.Button(meeting_room_reservation_window, bg='Yellow',
                                                    text="See Current Reservations",
                                                    command=lambda: self.see_meeting_room_reservations())
                see_reservations_button.pack()

            def register_meeting_room_reservation_data(self, window, date, day, duration, time, room):
                meeting_room_data = f"Date: {date} - Day: {day} - Duration: {duration} - Time: {time} - Room: {room}"
                self.meeting_room_reservations.append(meeting_room_data)
                messagebox.showinfo("Registration Successful", "Data has been registered successfully.")
                window.destroy()  # Close the registration window

            def see_meeting_room_reservations(self):
                meeting_room_reservations_window = tk.Toplevel(self.root)
                meeting_room_reservations_window.title("Current Meeting Room Reservations")
                meeting_room_reservations_window.geometry("600x400")
                meeting_room_reservations_window.configure(bg= "silver")
            

                tk.Label(meeting_room_reservations_window, text="List of Currently Reserved Meeting Rooms", bg= 'Yellow', font=("Helvetica", 14)).pack(pady=10)

                # Listbox to display meeting room reservations
                listbox = tk.Listbox(meeting_room_reservations_window, bg= 'Yellow', selectmode=tk.BROWSE)
                for item in self.meeting_room_reservations:
                    listbox.insert(tk.END, item)

                listbox.pack(pady=10)
                listbox.bind("<Double-Button-1>", lambda event: self.show_options_window_meeting_room(listbox.get(tk.ACTIVE)))

            def show_options_window_meeting_room(self, selected_item):
                options_window = tk.Toplevel(self.root)
                options_window.title("What do you wish to do?")
                options_window.geometry("300x150")
                options_window.configure(bg= "silver")

                tk.Label(options_window, text="What do you wish to do?", bg= 'Yellow', font=("Helvetica", 14)).pack(pady=10)

                edit_button = tk.Button(options_window, text="Edit Data", bg= 'Yellow', command=lambda: self.edit_data_meeting_room(selected_item))
                edit_button.pack(pady=5)

                delete_button = tk.Button(options_window, text="Delete Data", bg= 'Yellow', command=lambda: self.confirm_delete_meeting_room(selected_item))
                delete_button.pack(pady=5)

            def edit_data_meeting_room(self, selected_item):
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Data")
                edit_window.geometry("400x600")
                edit_window.configure(bg= "silver")


                data_parts = selected_item.split(" - ")

                tk.Label(edit_window, bg= 'Yellow', text="Date").pack()
                date_var = tk.StringVar()
                date_var.set(data_parts[0].split(":")[1].strip())
                edited_date_entry = tk.Entry(edit_window, width=30, textvariable=date_var)
                edited_date_entry.pack(pady=5)

                tk.Label(edit_window, bg= 'Yellow', text="Day").pack()
                day_var = tk.StringVar()
                day_var.set(data_parts[1].split(":")[1].strip())
                edited_day_menu = tk.OptionMenu(edit_window, day_var, *["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
                edited_day_menu.pack(pady=5)

                tk.Label(edit_window, bg= 'Yellow', text="Duration").pack()
                duration_var = tk.StringVar()
                duration_var.set(data_parts[2].split(":")[1].strip())
                edited_duration_menu = tk.OptionMenu(edit_window, duration_var, *["1 hour", "2 hours", "3 hours"])
                edited_duration_menu.pack(pady=5)

                tk.Label(edit_window, bg= 'Yellow', text="Time").pack()
                time_var = tk.StringVar()
                time_var.set(data_parts[3].split(":")[1].strip())
                edited_time_entry = tk.Entry(edit_window, width=30, textvariable=time_var)
                edited_time_entry.pack(pady=5)

                tk.Label(edit_window, bg= 'Yellow', text="Room").pack()
                room_var = tk.StringVar()
                room_var.set(data_parts[4].split(":")[1].strip())
                edited_room_menu = tk.OptionMenu(edit_window, room_var, *["Small Room (S-1)", "Small Room (S-2)", "Small Room (S-3)", "Small Room (S-4)", "Small Room (S-5)",
                                                                        "Big Room (B-1)", "Big Room (B-2)", "Big Room (B-3)", "Big Room (B-4)", "Big Room         (B-5)"])
                edited_room_menu.pack(pady=5)

                # Button to save changes
                save_button = tk.Button(edit_window, text="Done Editing", bg= 'Yellow', command=lambda: self.save_edited_data_meeting_room(selected_item, date_var.get(), day_var.get(), duration_var.get(), time_var.get(), room_var.get()))
                save_button.pack(pady=10)

            def save_edited_data_meeting_room(self, old_data, edited_date, edited_day, edited_duration, edited_time, edited_room):
                edited_data = f"Date: {edited_date} - Day: {edited_day} - Duration: {edited_duration} - Time: {edited_time} - Room: {edited_room}"
                self.meeting_room_reservations.remove(old_data)
                self.meeting_room_reservations.append(edited_data)
                messagebox.showinfo("Edit Successful", "Data has been edited successfully.")

            def confirm_delete_meeting_room(self, selected_item):
                confirm_delete_window = tk.Toplevel(self.root)
                confirm_delete_window.title("Confirm Deletion")
                confirm_delete_window.geometry("300x150")
                confirm_delete_window.configure(bg= "silver")

                tk.Label(confirm_delete_window, text=f"Are you sure you want to delete:\n{selected_item}?", bg= 'Yellow', font=("Helvetica", 12)).pack(pady=10)

                yes_button = tk.Button(confirm_delete_window, text="Yes", bg= 'Yellow', command=lambda: self.delete_data_meeting_room(selected_item))
                yes_button.pack(pady=5)

                no_button = tk.Button(confirm_delete_window, text="No", bg= 'Yellow', command=confirm_delete_window.destroy)
                no_button.pack(pady=5)

            def delete_data_meeting_room(self, selected_item):
                self.meeting_room_reservations.remove(selected_item)
                messagebox.showinfo("Deletion Successful", "Data has been deleted successfully.")

            def see_loaned_books(self):
                loaned_books_window = tk.Toplevel(self.root)
                loaned_books_window.title("Currently Loaned Books")
                loaned_books_window.geometry("600x400")
                loaned_books_window.configure(bg= "silver")

                tk.Label(loaned_books_window, text="List of Currently Loaned Books", bg= 'lime', font=("Helvetica", 14)).pack(pady=10)

                # Listbox to display loaned books
                listbox = tk.Listbox(loaned_books_window, bg= 'lime', selectmode=tk.BROWSE)
                for item in self.loaned_books:
                    listbox.insert(tk.END, item)

                listbox.pack(pady=10)
                listbox.bind("<Double-Button-1>", lambda event: self.show_options_window(listbox.get(tk.ACTIVE)))

            
            def show_options_window(self, selected_item):
                options_window = tk.Toplevel(self.root)
                options_window.title("What do you wish to do?")
                options_window.geometry("300x150")
                options_window.configure(bg= "silver")

                tk.Label(options_window, text="What do you wish to do?", bg= 'lime', font=("Helvetica", 14)).pack(pady=10)

                edit_button = tk.Button(options_window, text="Edit Data", bg= 'lime', command=lambda: self.edit_data(selected_item))
                edit_button.pack(pady=5)

                delete_button = tk.Button(options_window, text="Delete Data", bg= 'lime', command=lambda: self.confirm_delete(selected_item))
                delete_button.pack(pady=5)

            def edit_data(self, selected_item):
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Data")
                edit_window.geometry("400x250")
                edit_window.configure(bg="silver")

                data_parts = selected_item.split(" - ")

                # Print statements for debugging
                print("Length of data_parts:", len(data_parts))
                print("Data parts:", data_parts)

                tk.Label(edit_window, bg='lime', text="Book Title").pack()
                book_title_var = tk.StringVar()

                # Add a check for the length of data_parts before accessing an index
                if len(data_parts) > 0:
                    book_title_var.set(data_parts[0].split(":")[1].strip())

                edited_book_title_entry = tk.Entry(edit_window, width=30, textvariable=book_title_var)
                edited_book_title_entry.pack(pady=5)

                tk.Label(edit_window, bg='lime', text="ISBN").pack()
                isbn_var = tk.StringVar()

                # Add a check for the length of data_parts before accessing an index
                if len(data_parts) > 1:
                    isbn_var.set(data_parts[1].split(":")[1].strip())

                edited_isbn_entry = tk.Entry(edit_window, width=30, textvariable=isbn_var)
                edited_isbn_entry.pack(pady=5)

                tk.Label(edit_window, bg='lime', text="Author").pack()
                author_var = tk.StringVar()

                # Add a check for the length of data_parts before accessing an index
                if len(data_parts) > 2:
                    author_var.set(data_parts[2].split(":")[1].strip())

                edited_author_entry = tk.Entry(edit_window, width=30, textvariable=author_var)
                edited_author_entry.pack(pady=5)

                tk.Label(edit_window, bg='lime', text="Due Date").pack()
                due_date_var = tk.StringVar()

                # Add a check for the length of data_parts before accessing an index
                if len(data_parts) > 3:
                    due_date_var.set(data_parts[3].split(":")[1].strip())

                edited_due_date_entry = tk.Entry(edit_window, width=30, textvariable=due_date_var)
                edited_due_date_entry.pack(pady=5)

                # Button to save changes
                save_button = tk.Button(edit_window, text="Done Editing", bg='lime', command=lambda: self.save_edited_data(selected_item, book_title_var.get(), isbn_var.get(), author_var.get()))
                save_button.pack(pady=10)


            def save_edited_data(self, old_data, edited_book_title, edited_isbn, edited_author):        # Here you can add code to save the edited data to your database or data structure.
                edited_data = f"Book Title: {edited_book_title} - ISBN: {edited_isbn} - Author: {edited_author}"
                self.loaned_books.remove(old_data)
                self.loaned_books.append(edited_data)
                messagebox.showinfo("Edit Successful", "Data has been edited successfully.")

            def confirm_delete(self, selected_item):
                confirm_delete_window = tk.Toplevel(self.root)
                confirm_delete_window.title("Confirm Deletion")
                confirm_delete_window.geometry("300x150")
                confirm_delete_window.configure(bg= "silver")

                tk.Label(confirm_delete_window, text=f"Are you sure you want to delete:\n{selected_item}?", bg= 'lime', font=("Helvetica", 12)).pack(pady=10)

                yes_button = tk.Button(confirm_delete_window, text="Yes", bg= 'lime', command=lambda: self.delete_data(selected_item))
                yes_button.pack(pady=5)

                no_button = tk.Button(confirm_delete_window, text="No", bg= 'lime', command=confirm_delete_window.destroy)
                no_button.pack(pady=5)

            def delete_data(self, selected_item, bg= 'lime'):
                self.loaned_books.remove(selected_item)
                messagebox.showinfo("Deletion Successful", "Data has been deleted successfully.")

        if __name__ == "__main__":
            root = tk.Tk()
            app = StudentLibraryApp(root)
            root.mainloop()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(frame, text="StuLib Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
