#Note: fresh_tomatoes uses var names title, poster_image_url and trailer_youtube_url
class Movie:
	def __init__(self, title_input, storyline_input, poster_image_input, youtube_trailer_input):
		self.title = title_input
		self.storyline = storyline_input
		self.poster_image_url = poster_image_input
		self.trailer_youtube_url = youtube_trailer_input