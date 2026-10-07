patients = []
doctors = []
appointment_times = []


def add_appointment():
    patient = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    time = input("Enter appointment time: ")

    patients.append(patient)
    doctors.append(doctor)
    appointment_times.append(time)

    print("Appointment booked successfully!")


def view_appointments():
    if len(patients) == 0:
        print("No appointments found.")
    else:
        print("\n===== APPOINTMENTS =====")

        for i in range(len(patients)):
            print(
                i + 1,
                "| Patient:", patients[i],
                "| Doctor:", doctors[i],
                "| Time:", appointment_times[i]
            )


def search_patient():
    name = input("Enter patient name: ")

    found = False

    for i in range(len(patients)):
        if patients[i].lower() == name.lower():
            print("\nAppointment Found")
            print("Patient:", patients[i])
            print("Doctor:", doctors[i])
            print("Time:", appointment_times[i])

            found = True

    if found == False:
        print("No appointment found for this patient.")


def cancel_appointment():
    if len(patients) == 0:
        print("No appointments available.")
        return

    view_appointments()

    number = int(input("Enter appointment number to cancel: "))

    if number >= 1 and number <= len(patients):

        index = number - 1

        patients.pop(index)
        doctors.pop(index)
        appointment_times.pop(index)

        print("Appointment cancelled successfully.")

    else:
        print("Invalid appointment number.")


while True:

    print("\n===== HOSPITAL APPOINTMENT SYSTEM =====")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Search Patient")
    print("4. Cancel Appointment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_appointment()

    elif choice == "2":
        view_appointments()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        cancel_appointment()

    elif choice == "5":
        print("Thank you for using Hospital Appointment System.")
        break

    else:
        print("Invalid choice.")
