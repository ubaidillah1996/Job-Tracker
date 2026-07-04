import json

# =========================
# LOAD DATA FROM JSON FILE
# =========================

try:
    # Cuba baca data dari file JSON
    with open("data.json", "r") as file:
        applications = json.load(file)

except:
    # Kalau file tak wujud atau kosong
    applications = []


# =========================
# MAIN PROGRAM LOOP
# =========================

while True:

    print("\n=== JOB APPLICATION TRACKER ===")
    print("1. Add New Application")
    print("2. View Applications")
    print("3. Exit")

    choice = input("Choose an option: ")

    # =========================
    # ADD APPLICATION
    # =========================
    if choice == "1":
        print("\nAdd application selected.")

        company = input("Enter company name: ")
        position = input("Enter position: ")

        application = {
            "company": company,
            "position": position,
            "status": "Pending"
        }

        applications.append(application)

        # Save ke JSON file
        with open("data.json", "w") as file:
            json.dump(applications, file, indent=4)

        print("Application saved!")

    # =========================
    # VIEW APPLICATIONS
    # =========================
    elif choice == "2":
        print("\n--- All Applications ---")

        if len(applications) == 0:
            print("No applications yet.")

        else:
            for index, app in enumerate(applications, start=1):
                print(f"{index}. {app['company']} - {app['position']} - {app['status']}")

    # =========================
    # EXIT PROGRAM
    # =========================
    elif choice == "3":
        print("Goodbye!")
        break

    # =========================
    # INVALID INPUT
    # =========================
    else:
        print("Invalid option")