from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    help = 'Load initial movie data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing movies
        Movie.objects.all().delete()
        
        movies_data = [
            {
                'title': 'The Shawshank Redemption',
                'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg',
                'release_year': 1994,
                'genres': 'Drama, Crime',
                'rating': 9.3,
                'language': 'English',
                'cast': 'Tim Robbins, Morgan Freeman'
            },
            {
                'title': 'The Godfather',
                'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg',
                'release_year': 1972,
                'genres': 'Drama, Crime',
                'rating': 9.2,
                'language': 'English',
                'cast': 'Marlon Brando, Al Pacino'
            },
            {
                'title': 'The Dark Knight',
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
                'release_year': 2008,
                'genres': 'Action, Crime, Drama, Thriller',
                'rating': 9.0,
                'language': 'English',
                'cast': 'Christian Bale, Heath Ledger'
            },
            {
                'title': 'Pulp Fiction',
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
                'release_year': 1994,
                'genres': 'Crime, Drama, Thriller',
                'rating': 8.9,
                'language': 'English',
                'cast': 'John Travolta, Uma Thurman, Samuel L. Jackson'
            },
            {
                'title': 'Forrest Gump',
                'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg',
                'release_year': 1994,
                'genres': 'Drama, Romance',
                'rating': 8.8,
                'language': 'English',
                'cast': 'Tom Hanks, Robin Wright'
            },
            {
                'title': 'Inception',
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg',
                'release_year': 2010,
                'genres': 'Action, Science Fiction, Thriller',
                'rating': 8.8,
                'language': 'English',
                'cast': 'Leonardo DiCaprio, Joseph Gordon-Levitt'
            },
            {
                'title': 'The Matrix',
                'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
                'release_year': 1999,
                'genres': 'Action, Science Fiction',
                'rating': 8.7,
                'language': 'English',
                'cast': 'Keanu Reeves, Laurence Fishburne'
            },
            {
                'title': 'Interstellar',
                'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
                'release_year': 2014,
                'genres': 'Adventure, Drama, Science Fiction',
                'rating': 8.6,
                'language': 'English',
                'cast': 'Matthew McConaughey, Anne Hathaway'
            },
            {
                'title': 'Goodfellas',
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife and his partners in crime.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg',
                'release_year': 1990,
                'genres': 'Drama, Crime',
                'rating': 8.7,
                'language': 'English',
                'cast': 'Robert De Niro, Ray Liotta, Joe Pesci'
            },
            {
                'title': 'The Silence of the Lambs',
                'description': 'A young FBI cadet must receive the help of an incarcerated cannibal killer to catch another serial killer.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/uS9m8OBk1A8eM9I042bx8XXpqAq.jpg',
                'release_year': 1991,
                'genres': 'Crime, Drama, Thriller',
                'rating': 8.6,
                'language': 'English',
                'cast': 'Jodie Foster, Anthony Hopkins'
            },
            {
                'title': 'Saving Private Ryan',
                'description': 'Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/uqx37cS8cpHg8U35f9U5IBlrCV3.jpg',
                'release_year': 1998,
                'genres': 'Drama, War, Action',
                'rating': 8.6,
                'language': 'English',
                'cast': 'Tom Hanks, Matt Damon'
            },
            {
                'title': 'The Green Mile',
                'description': 'The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/velWPhVMQeQKcxggNEU8YmIo52R.jpg',
                'release_year': 1999,
                'genres': 'Fantasy, Drama, Crime',
                'rating': 8.6,
                'language': 'English',
                'cast': 'Tom Hanks, Michael Clarke Duncan'
            },
            {
                'title': 'Parasite',
                'description': 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg',
                'release_year': 2019,
                'genres': 'Comedy, Thriller, Drama',
                'rating': 8.6,
                'language': 'Korean',
                'cast': 'Song Kang-ho, Lee Sun-kyun'
            },
            {
                'title': 'The Lion King',
                'description': 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg',
                'release_year': 1994,
                'genres': 'Animation, Drama, Adventure',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Matthew Broderick, James Earl Jones'
            },
            {
                'title': 'The Departed',
                'description': 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in Boston.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/nT97ifVT2J1yMQmeq20Qblg61T.jpg',
                'release_year': 2006,
                'genres': 'Drama, Thriller, Crime',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Leonardo DiCaprio, Matt Damon'
            },
            {
                'title': 'Whiplash',
                'description': 'A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/7fn624j5lj3xTme2SgiLCeuedmO.jpg',
                'release_year': 2014,
                'genres': 'Drama, Music',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Miles Teller, J.K. Simmons'
            },
            {
                'title': 'The Prestige',
                'description': 'After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/tRNlZbgNCNOpLpbPEz5L8G8A0JN.jpg',
                'release_year': 2006,
                'genres': 'Drama, Mystery, Thriller',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Christian Bale, Hugh Jackman'
            },
            {
                'title': 'Gladiator',
                'description': 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg',
                'release_year': 2000,
                'genres': 'Action, Drama, Adventure',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Russell Crowe, Joaquin Phoenix'
            },
            {
                'title': 'The Avengers',
                'description': 'Earth\'s mightiest heroes must come together and learn to fight as a team to stop an alien invasion.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg',
                'release_year': 2012,
                'genres': 'Action, Adventure, Science Fiction',
                'rating': 8.0,
                'language': 'English',
                'cast': 'Robert Downey Jr., Chris Evans'
            },
            {
                'title': 'Spider-Man: Into the Spider-Verse',
                'description': 'Teen Miles Morales becomes Spider-Man and must join with others from different dimensions to stop a threat.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg',
                'release_year': 2018,
                'genres': 'Action, Adventure, Animation, Science Fiction',
                'rating': 8.4,
                'language': 'English',
                'cast': 'Shameik Moore, Jake Johnson'
            },
            {
                'title': 'Toy Story',
                'description': 'A cowboy doll is profoundly threatened when a new spaceman figure supplants him as top toy in a boy\'s room.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg',
                'release_year': 1995,
                'genres': 'Animation, Comedy, Adventure',
                'rating': 8.3,
                'language': 'English',
                'cast': 'Tom Hanks, Tim Allen'
            },
            {
                'title': 'WALL-E',
                'description': 'In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg',
                'release_year': 2008,
                'genres': 'Animation, Science Fiction, Romance',
                'rating': 8.4,
                'language': 'English',
                'cast': 'Ben Burtt, Elissa Knight'
            },
            {
                'title': 'Finding Nemo',
                'description': 'After his son is captured in the Great Barrier Reef, a timid clownfish sets out on a journey to bring him home.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg',
                'release_year': 2003,
                'genres': 'Animation, Adventure, Comedy',
                'rating': 8.1,
                'language': 'English',
                'cast': 'Albert Brooks, Ellen DeGeneres'
            },
            {
                'title': 'Coco',
                'description': 'Aspiring musician Miguel embarks on an extraordinary journey to the magical land of his ancestors.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg',
                'release_year': 2017,
                'genres': 'Animation, Adventure, Comedy, Fantasy',
                'rating': 8.4,
                'language': 'English',
                'cast': 'Anthony Gonzalez, Gael García Bernal'
            },
            {
                'title': 'The Shining',
                'description': 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/b6ko0IKC8MdYBmPYHEKHXZFP7jP.jpg',
                'release_year': 1980,
                'genres': 'Horror, Thriller',
                'rating': 8.4,
                'language': 'English',
                'cast': 'Jack Nicholson, Shelley Duvall'
            },
            {
                'title': 'Get Out',
                'description': 'A young African-American visits his white girlfriend\'s parents for the weekend, where his simmering uneasiness becomes real.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg',
                'release_year': 2017,
                'genres': 'Horror, Thriller, Mystery',
                'rating': 7.7,
                'language': 'English',
                'cast': 'Daniel Kaluuya, Allison Williams'
            },
            {
                'title': 'A Quiet Place',
                'description': 'In a post-apocalyptic world, a family is forced to live in silence while hiding from monsters with ultra-sensitive hearing.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg',
                'release_year': 2018,
                'genres': 'Horror, Drama, Science Fiction',
                'rating': 7.5,
                'language': 'English',
                'cast': 'Emily Blunt, John Krasinski'
            },
            {
                'title': 'La La Land',
                'description': 'While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg',
                'release_year': 2016,
                'genres': 'Romance, Drama, Comedy, Music',
                'rating': 8.0,
                'language': 'English',
                'cast': 'Ryan Gosling, Emma Stone'
            },
            {
                'title': 'Titanic',
                'description': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg',
                'release_year': 1997,
                'genres': 'Drama, Romance',
                'rating': 7.9,
                'language': 'English',
                'cast': 'Leonardo DiCaprio, Kate Winslet'
            },
            {
                'title': 'The Notebook',
                'description': 'A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/qom1SZSENdmHFNZBXbtJAU0WTlC.jpg',
                'release_year': 2004,
                'genres': 'Romance, Drama',
                'rating': 7.9,
                'language': 'English',
                'cast': 'Ryan Gosling, Rachel McAdams'
            },
            {
                'title': 'Superbad',
                'description': 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg',
                'release_year': 2007,
                'genres': 'Comedy',
                'rating': 7.6,
                'language': 'English',
                'cast': 'Jonah Hill, Michael Cera'
            },
            {
                'title': 'The Grand Budapest Hotel',
                'description': 'A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/eWdyYQreja6JGCzqHWXpWHDrrPo.jpg',
                'release_year': 2014,
                'genres': 'Comedy, Drama',
                'rating': 8.1,
                'language': 'English',
                'cast': 'Ralph Fiennes, F. Murray Abraham'
            },
            {
                'title': 'The Hangover',
                'description': 'Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/wwjuraFQK70icIDc0Y86wNUX7Y8.jpg',
                'release_year': 2009,
                'genres': 'Comedy',
                'rating': 7.7,
                'language': 'English',
                'cast': 'Bradley Cooper, Ed Helms, Zach Galifianakis'
            },
            {
                'title': 'Blade Runner 2049',
                'description': 'A young blade runner\'s discovery of a long-buried secret leads him to track down former blade runner Rick Deckard.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg',
                'release_year': 2017,
                'genres': 'Science Fiction, Drama',
                'rating': 8.0,
                'language': 'English',
                'cast': 'Ryan Gosling, Harrison Ford'
            },
            {
                'title': 'Arrival',
                'description': 'A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg',
                'release_year': 2016,
                'genres': 'Drama, Science Fiction, Mystery',
                'rating': 7.9,
                'language': 'English',
                'cast': 'Amy Adams, Jeremy Renner'
            },
            {
                'title': 'Mad Max: Fury Road',
                'description': 'In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/hA2ple9q4qnwxp3hKVNhroipsir.jpg',
                'release_year': 2015,
                'genres': 'Action, Adventure, Science Fiction',
                'rating': 8.1,
                'language': 'English',
                'cast': 'Tom Hardy, Charlize Theron'
            },
            {
                'title': 'John Wick',
                'description': 'An ex-hit-man comes out of retirement to track down the gangsters that killed his dog and took everything from him.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E3Bev.jpg',
                'release_year': 2014,
                'genres': 'Action, Thriller',
                'rating': 7.4,
                'language': 'English',
                'cast': 'Keanu Reeves, Michael Nyqvist'
            },
            {
                'title': 'Mission: Impossible - Fallout',
                'description': 'Ethan Hunt and his team race against time after a mission gone wrong.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/AkJQpZp9WoNdj7pLYSj1L0RcMMN.jpg',
                'release_year': 2018,
                'genres': 'Action, Adventure, Thriller',
                'rating': 7.7,
                'language': 'English',
                'cast': 'Tom Cruise, Henry Cavill'
            },
            {
                'title': 'Se7en',
                'description': 'Two detectives hunt a serial killer who uses the seven deadly sins as his motives.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVUO.jpg',
                'release_year': 1995,
                'genres': 'Crime, Mystery, Thriller',
                'rating': 8.6,
                'language': 'English',
                'cast': 'Brad Pitt, Morgan Freeman'
            },
            {
                'title': 'Zodiac',
                'description': 'A cartoonist becomes obsessed with tracking down the Zodiac Killer.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/6YmeO4pB7XFpUYRV515xWR99J3i.jpg',
                'release_year': 2007,
                'genres': 'Crime, Drama, Mystery, Thriller',
                'rating': 7.7,
                'language': 'English',
                'cast': 'Jake Gyllenhaal, Robert Downey Jr.'
            },
            {
                'title': 'Gone Girl',
                'description': 'With his wife\'s disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/gdiLTof3rbPDAmPaCf4g6op46bj.jpg',
                'release_year': 2014,
                'genres': 'Mystery, Thriller, Drama',
                'rating': 8.1,
                'language': 'English',
                'cast': 'Ben Affleck, Rosamund Pike'
            },
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'description': 'A meek Hobbit and companions set out to destroy a powerful ring and save Middle-earth.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
                'release_year': 2001,
                'genres': 'Adventure, Fantasy, Action',
                'rating': 8.8,
                'language': 'English',
                'cast': 'Elijah Wood, Ian McKellen'
            },
            {
                'title': 'Harry Potter and the Sorcerer\'s Stone',
                'description': 'An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself and his destiny.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/wuMc08IPKEatf9rnMNXvIDxqP4W.jpg',
                'release_year': 2001,
                'genres': 'Adventure, Fantasy',
                'rating': 7.6,
                'language': 'English',
                'cast': 'Daniel Radcliffe, Emma Watson'
            },
            {
                'title': 'Pan\'s Labyrinth',
                'description': 'In the Falangist Spain of 1944, a girl living with her stepfather in a military outpost enters a magical world.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/k0qd6Tu8sCayECfK1sVqeW4D0tJ.jpg',
                'release_year': 2006,
                'genres': 'Fantasy, Drama, War',
                'rating': 8.2,
                'language': 'Spanish',
                'cast': 'Ivana Baquero, Sergi López'
            },
            {
                'title': 'Dunkirk',
                'description': 'Allied soldiers from Belgium, the British Commonwealth and Empire, and France are surrounded by the German Army.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/cUqEgoP6kj8ykfNjJx3Tl5zHCcN.jpg',
                'release_year': 2017,
                'genres': 'War, Action, Drama, History',
                'rating': 7.9,
                'language': 'English',
                'cast': 'Fionn Whitehead, Tom Hardy'
            },
            {
                'title': 'Apocalypse Now',
                'description': 'A U.S. Army officer is sent into the jungle to assassinate a renegade colonel who has set himself up as a god.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/gQB8Y5RCMkv2zwzFHbUJX3kAhvA.jpg',
                'release_year': 1979,
                'genres': 'Drama, War',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Martin Sheen, Marlon Brando'
            },
            {
                'title': 'Schindler\'s List',
                'description': 'In German-occupied Poland, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg',
                'release_year': 1993,
                'genres': 'Drama, History, War',
                'rating': 9.0,
                'language': 'English',
                'cast': 'Liam Neeson, Ralph Fiennes'
            },
            {
                'title': 'The Pianist',
                'description': 'A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto of World War II.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/2hFvxCCWrTmCYwfy7yum0GKRi3Y.jpg',
                'release_year': 2002,
                'genres': 'Drama, War',
                'rating': 8.5,
                'language': 'English',
                'cast': 'Adrien Brody, Thomas Kretschmann'
            },
            {
                'title': 'Life is Beautiful',
                'description': 'When an Italian father is sent to a concentration camp, he uses his imagination to shield his son from the horrors.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/74hLDKjD5aGYOotO6esUVaeISa2.jpg',
                'release_year': 1997,
                'genres': 'Comedy, Drama, Romance, War',
                'rating': 8.6,
                'language': 'Italian',
                'cast': 'Roberto Benigni, Nicoletta Braschi'
            },
            {
                'title': 'Amélie',
                'description': 'Amélie is an innocent and naive girl who decides to help those around her and discovers love along the way.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/nSxDa3M9aMvGVLoItzWTepQ5h5d.jpg',
                'release_year': 2001,
                'genres': 'Comedy, Romance',
                'rating': 8.3,
                'language': 'French',
                'cast': 'Audrey Tautou, Mathieu Kassovitz'
            },
            {
                'title': 'City of God',
                'description': 'In the slums of Rio, two kids\' paths diverge as one struggles to become a photographer and the other a kingpin.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/k7eYdGvlEMp4bFrnUdpC6KCDGYQ.jpg',
                'release_year': 2002,
                'genres': 'Drama, Crime',
                'rating': 8.6,
                'language': 'Portuguese',
                'cast': 'Alexandre Rodrigues, Leandro Firmino'
            },
            {
                'title': 'Oldboy',
                'description': 'After being kidnapped and imprisoned for fifteen years, a man is released, only to find that he must find his captor.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/pWDtjs568ZfOTMbURQBYuT4Qwd7.jpg',
                'release_year': 2003,
                'genres': 'Action, Drama, Mystery, Thriller',
                'rating': 8.4,
                'language': 'Korean',
                'cast': 'Choi Min-sik, Yoo Ji-tae'
            },
            {
                'title': 'Spirited Away',
                'description': 'During her family\'s move, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits.',
                'poster_url': 'https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg',
                'release_year': 2001,
                'genres': 'Animation, Adventure, Fantasy',
                'rating': 8.6,
                'language': 'Japanese',
                'cast': 'Rumi Hiiragi, Miyu Irino'
            },
        ]
        
        created_count = 0
        for movie_data in movies_data:
            Movie.objects.create(**movie_data)
            created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {created_count} movies into the database.')
        )
