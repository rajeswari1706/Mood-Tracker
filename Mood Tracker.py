from datetime import date
moods = []

def add_mood():
    mood = input("How do you feel today? ")
    moods.append(f"{date.today()} - {mood}")

def view_moods():
    print("\nMood History:")
    for m in moods:
        print(m)

def main():
    while True:
        print("\n1.Add Mood 2.View Moods 3.Exit")
        choice = input("Choice: ")
        if choice=="1":
            add_mood()
        elif choice=="2":
            view_moods()
        elif choice=="3":
            break
        else:
            print("Invalid")

if __name__=="__main__":
    main()
