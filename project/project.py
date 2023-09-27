import sys, requests, json, re, os
from youtube_search import YoutubeSearch


# Main function to call all other fucntions performing parts of project.
def main():
    # Call a function to take song and artist input from user.
    var_list = coll_var()

    # Call a function to create a list of songs with artist name from iTunes API.
    search = list_songs(var_list)

    # Print all the songs collected from the API
    for i in search:
        print(i)

    print()

    # Collect a user input to select a song.
    while True:
        try:
            var3 = input("Please select the number that matches your song.\n").strip()

            # Accept only the numbers which are in the list.
            if not 0 < int(var3) < (len(search) + 1):
                print("Please enter a correct number")
            else:
                break

        # Catch ValueError in the case the user does not enter an integer.
        except ValueError:
            print("Please enter numbers only")
            continue

    print()

    # Find the element in the list that the user selected by serial number.
    for i in search:
        if re.search(r"^" + re.escape(var3), i):
            var4 = i
            break

    # Call function to return youtube link to the song selected by user and print.
    print(f"Youtube Link: {yt_link(var4)}")

    # Call function to reutnr few details on the song selected by user and print.
    print(details_song(var4))

    print("\nEnjoy!\n")


# Function to collect song and artist by user
def coll_var():
    var1 = input("What song would you like to search today? ").replace(" ", "").lower()

    var2 = input("Do you know the name of the artist? ").replace(" ", "").lower()

    # Check if atleast an artist name or song name was provided by the user or restart the script
    if var1 == "" and var2 == "":
        print("Please enter atleast one character")
        os.execv(sys.executable, ["python"] + ["project.py"])

    print()

    # Return var_list with strings song+artist, artist and song.
    var_list = [var1 + var2, var2, var1]
    return var_list


# Function to return maximum 15 matching songs fron iTunes API.
def list_songs(s):
    search = []

    # sr_No is used to assign a unique identifier to all objects in the list for the user.
    sr_no = 1

    for i in s:
        try:
            # n is used to print all 5 searches which are part of dictionary response.
            n = 0
            while n < 5:
                response = requests.get(
                    f"https://itunes.apple.com/search?entity=song&limit=5&term={i}"
                )
                o = response.json()["results"][n]
                song = f"{sr_no} {o['trackName']} by {o['artistName']}"
                search.append(song)
                n += 1
                sr_no += 1

        # IndexError are expected if there are less than 5 possible searches for a string. This catches the error.
        except IndexError:
            continue

    # User will be notified that no matches were found.
    if len(search) == 0:
        print(f"No matches were found")
        print()

    # User will be asked if they want to close the program or restart it if no matches were found.
    if len(search) == 0:
        while True:
            user_req = (
                input("Would you like to search again?(Please Answer in Yes/No)\n")
                .lower()
                .strip()
            )

            print()

            if user_req == "yes":
                os.execv(sys.executable, ["python"] + ["project.py"])
            elif user_req == "no":
                sys.exit("Thank you for using the application.")
            else:
                continue

    return search

#Function to return few details of the selected song by user
def details_song(d):

    #Since the limit is 15 searches, we need not worry about corner case for digits more than 2.
    #In that case the line below will required to be modified.
    trackName, artistName = d[2:].strip().lower().split(" by ")

    #The line below was placed in case the API link required spaces indicated explicitly.
    #However, the API search tool is powerful to not require spaces here.
    '''trackName = trackName.replace(" ", "%20")'''

    response = requests.get(
        f"https://itunes.apple.com/search?entity=song&limit=10&term={trackName}"
    )

    #An exact match is required for trackName and artistName to provide correct details.
    for result in response.json()["results"]:
        if result["artistName"].lower() == artistName:
            return (
                f"Song: {result['trackName']}\n"
                + f"Artist: {result['artistName']}\n"
                + f"Genre: {result['primaryGenreName']}\n"
                + f"Release date: {result['releaseDate'][0:10]}"
            )

#Function to return the Youtube link to first search element on youtube.
def yt_link(j):
    results = YoutubeSearch(f"{j[2:]}", max_results=10).to_dict()

    return "https://www.youtube.com" + results[0]["url_suffix"]


if __name__ == "__main__":
    main()
