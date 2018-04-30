import Media
import fresh_tomatoes

avatar = Media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hunt_for_red_october = Media.Movie("Hunt for Red October",
                                   "Defecting Captian wants to give us a Nuculuar Submarine",
                                   "https://upload.wikimedia.org/wikipedia/en/3/36/The_Hunt_for_Red_October_movie_poster.png",
                                   "https://www.youtube.com/watch?v=kxL8uBmdulY")

prometheus = Media.Movie("Prometheus",
                                   "A mystery unfolds on an Alien world.",
                                   "https://upload.wikimedia.org/wikipedia/sco/a/a3/Prometheusposterfixed.jpg",
                                   "https://www.youtube.com/watch?v=nmJOO6D5RvA")

bourne_identity = Media.Movie("Bourne Identity",
                                   "A man struggles remembering his past.",
                                   "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                                   "https://www.youtube.com/watch?v=cD-uQreIwEk")

princess_bride = Media.Movie("Princess Bride",
                                   "A modern day fairytail",
                                   "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                                   "https://www.youtube.com/watch?v=njZBYfNpWoE")

ready_player_one = Media.Movie("Ready Player One",
                                   "A wild Adventure Set in VR and Reality",
                                   "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",
                                   "https://www.youtube.com/watch?v=cSp1dM2Vj48")

movies = [avatar, hunt_for_red_october, prometheus, bourne_identity, princess_bride, ready_player_one ]
#fresh_tomatoes.open_movies_page(movies)
print("Media Doc: ", Media.Movie.__doc__)
print("Media Name: ", Media.Movie.__name__)
print("Media Module: ", Media.Movie.__module__)


