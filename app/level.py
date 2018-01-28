class Level:

    def __init__(self, number, question, answer, hint, image_url):
        self.number = number
        self.question = question
        self.answer = answer
        self.hint = hint
        self.image_url = image_url


    def get(level_number):
        return Level(
            level_number,
            "What's black, white and read all over?",
            "newspaper",
            "It's just one word",
            "https://media1.tenor.com/images/1cec9996b62a59813e973e271571e535/tenor.gif"
            )
