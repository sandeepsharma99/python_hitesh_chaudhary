
def load_data():
    pass

def list_all_video(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube video")
        print("2. Add a you tube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = input("Enter your choice")

match choice:
    case "1":
        list_all_video(videos)
    case "2":
            add_video(videos)
    case "3":
        update_video(videos)
    case "4":
        delete_video(videos)
    case "5":
        break
    case _:
        print("Invalid choice")

if __name__ == "__main__":
    main()