from project import list_songs, details_song, yt_link

def test_list_songs():

    s = ["buddy", "weezer"]

    assert list_songs(s) == ['1 Buddy by Musiq Soulchild',
                              '2 Buddy by Adam Sandler',
                              '3 B.U.D.D.Y. by Musiq Soulchild',
                              '4 Buddy by Willie Nelson',
                              '5 Buddy (feat. Jungle Brothers, A Tribe Called Quest, Queen Latifah & Monie Love) by De La Soul',
                              '6 Buddy Holly by Weezer',
                              "7 Say It Ain't So by Weezer",
                              '8 Undone - The Sweater Song by Weezer',
                              '9 My Name Is Jonas by Weezer',
                              '10 Holiday by Weezer']

def test_yt_link():

    j = "6 Buddy Holly by Weezer"

    assert yt_link(j)[0:32] == "https://www.youtube.com/watch?v="

def test_details_song():

    d = "1 Uptown Funk (feat. Bruno Mars) by Mark Ronson"

    assert details_song(d) == ("Song: Uptown Funk (feat. Bruno Mars)\n"+
                                "Artist: Mark Ronson\n"+
                                "Genre: Pop\n"+
                                "Release date: 2014-11-10")



