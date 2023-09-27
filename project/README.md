# Song and Youtube Search

## Video Demo:
https://youtu.be/BvstoRLgdY0

## Description:

    My Final Project for Harvard's CS50P

    The program begins with asking the user,

    INPUT1 - **"What song would you like to search today?"**

    Everything is acceptable as an input here. (Let,s assume user enters 'buddy')

    INPUT2 - **"Do you know the name of the artist?**

    Everything is acceptable as an input here. ('None' or only spaces will not be accepted if answer to the first questions is the same.) (Let's assume user enters 'weezer')

    Based on the user's input the program will display results for the search parameters utilizing the iTunes API. (No auth required)

    Example (maximum number of searches in the script is 15):

       _1 Buddy by Musiq Soulchild
        2 Buddy by Adam Sandler
        3 B.U.D.D.Y. by Musiq Soulchild
        4 Buddy by Willie Nelson
        5 Buddy (feat. Jungle Brothers A Tribe Called Quest, Queen Latifah & Monie Love) by De La Soul
        6 Buddy Holly by Weezer
        7 Say It Ain't So by Weezer
        8 Undone - The Sweater Song by Weezer
        9 My Name Is Jonas by Weezer
        10 Holiday by Weezer_

    INPUT3 - **Please select the number that matches your song.**

    User may select any number from 1 to 10 (as per the example) which will identify their song.

    Using the unique identifier, the program will provide a YouTube link with few details on the song.

    Example (If user enters 6):

       _Youtube Link: https://www.youtube.com/watch?v=kemivUKb4f4&pp=ygUVQnVkZHkgSG9sbHkgYnkgV2VlemVy
        Song: Buddy Holly
        Artist: Weezer
        Genre: Pop
        Release date: 1994-01-01

        Enjoy!_

    A few corner cases are also mentioned in the video and how the program handles the exceptions or input errors. They are:

    1. The user enters None or only spaces for both artist and song.
    2. Search result is empty where user will be notified that no results were found and the program restarts.
    3. The user selects a number that is not in the search result.
    4. Program asks user to rerun the script or exit the program.