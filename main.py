# list untuk simpan semua permohonan kerja
applications = []  # Senarai untuk menyimpan permohonan kerja

#Ulang program sehingga user pilih untuk keluar
while True:

#Display Tajuk Projek
    print("=== Job Application Tracker === ")

#Display Menu
    print("1. Add New Application")
    print("2. View Applications")
    print("3. Exit")

    #Pilihan dari User
    choice = input("Choose an option: ")

    #Display apa yang user pilih
    print("You selected:", choice)

    #Kalau user pilih 1 (Added Application)
    if choice == "1":
        print("Add application selected.")

        #Ambil maklumat permohonan kerja dari user
        company = input("Enter company name: ")
        position = input("Enter position: ")

        #Simpan maklumat permohonan kerja dalam dictionary
        application = {
            "company": company,
            "position": position,
            "status": "Pending"
        }
        #Masukkan permohonan kerja ke dalam senarai list
        #"append" bermaksud tambah ke dalam senarai list
        applications.append(application)

        #Savekan permohonan tadi
        print("Application saved!")

    #Kalau user pilih 2 (View Applications)
    elif choice == "2":
        print("All applications Selected.")

        #Check kalau senarai permohonan kerja ada atau tak
        if len(applications) == 0:
            print("No applications yet.")
        else:
            #Loop / Listkan semua permohonan kerja yang ada dalam senarai
            # view data 
            #Enumerate bagi list nombor secara automatik (tersusun ikut index)
            #Untuk akses dictionary, guna app['company'] untuk akses company, app['position'] untuk akses position, app['status'] untuk akses status
            for index, app in enumerate(applications):
                print(f"{index}.{app['company']},{app['position']},{app['status']}")

    #Kalau user pilih 3 (Exit)
    elif choice == "3":
        print("Goodbye!")
        break # untuk keluar dari loop 

    #Kalau input salah
    else:
        print("Invalid option")