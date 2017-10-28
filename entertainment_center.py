import media
import fresh_tomatoes

#Movie() args are in format title, storyline, poster url, and youtube url

annie_hall = media.Movie("Annie Hall",
							" Neurotic New York comedian Alvy Singer falls in love with the ditzy Annie Hall.",
							"https://sc-events.s3.amazonaws.com/4181858/main.jpg",
							"https://www.youtube.com/watch?v=OqVgCfZX-yE")

kill_bill = media.Movie("Kill Bill Vol 1 & Vol 2",
						"The Bride wakens from a four-year coma. The child she carried in her womb is gone. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.",
						"https://i.pinimg.com/736x/64/82/ef/6482ef51ce0b437986ec477e0d46f30c--quentin-tarantino-tarantino-movies.jpg",
						"https://www.youtube.com/watch?v=ot6C1ZKyiME")



arsenic_and_old_lace = media.Movie("Arsenic and Old Lace", 
									"A drama critic learns on his wedding day that his beloved maiden aunts are homicidal maniacs, and that insanity runs in his family.", 
									"http://avalonlibrary.org/wp-content/uploads/2014/04/arsenic-and-old-lace.jpg", 
									"https://www.youtube.com/watch?v=GCWBDwkhGN0")


movies_list = [annie_hall, kill_bill, arsenic_and_old_lace]


fresh_tomatoes.open_movies_page(movies_list)