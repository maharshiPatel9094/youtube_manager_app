import json


def load_data():
    try:
        with open("youtube.txt","r") as file:   #r - read , w - write
            # converts the file into json and load the data 
            return json.load(file)
    except FileNotFoundError:
        return []
        
# def for saving the videos and then load in file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos,file)
        # dump() takes two parameters the data we want to write and where to write

def list_all_videos(videos):
    # enumerate( ) adds indexing to the values
    # indexing starts with 1
    for index, video in enumerate(videos,start=1):
        print(f"{index}. ")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass        

# entry point
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")      

# checks weather the name of function is main
if __name__ == "__main__":
    main()