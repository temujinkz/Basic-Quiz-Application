def run_quiz(questions):
    score = 0
    for question, options, answer in questions:
        print("\n" + question)  # Add a new line for better formatting
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        try:
            user_answer = int(input("Your answer (1/2/3/4): "))
            if options[user_answer - 1] == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {answer}")
        except (IndexError, ValueError):
            print("Invalid input! Please enter a number between 1 and 4.")
    return score

# Massive list of questions covering many topics
questions = [
    # General Knowledge
    ("What is the capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris"),
    ("Which is the largest planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
    ("What is the chemical symbol for water?", ["HO", "H2O", "O2", "H2"], "H2O"),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "F. Scott Fitzgerald"], "Harper Lee"),
    ("Which year did World War II end?", ["1942", "1944", "1945", "1946"], "1945"),
    
    # Math and Science
    ("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
    ("What is the square root of 64?", ["6", "7", "8", "9"], "8"),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
    ("What is the speed of light?", ["299,792 km/s", "150,000 km/s", "200,000 km/s", "1,000,000 km/s"], "299,792 km/s"),
    ("What gas do plants absorb during photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Carbon Dioxide"),
    
    # History and Geography
    ("Who was the first president of the United States?", ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"], "George Washington"),
    ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "Thailand", "South Korea"], "Japan"),
    ("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Southern", "Pacific"], "Pacific"),
    ("In which year did the Titanic sink?", ["1912", "1920", "1905", "1930"], "1912"),
    ("Which country has the most pyramids?", ["Egypt", "Mexico", "Sudan", "Peru"], "Sudan"),
    
    # Technology
    ("Who is the founder of Microsoft?", ["Steve Jobs", "Mark Zuckerberg", "Bill Gates", "Elon Musk"], "Bill Gates"),
    ("Which programming language is primarily used for Android app development?", ["Python", "Java", "C#", "Swift"], "Java"),
    ("What does CPU stand for?", ["Central Processing Unit", "Control Processing Unit", "Computer Processing Unit", "Central Power Unit"], "Central Processing Unit"),
    ("Which social media platform was bought by Elon Musk in 2022?", ["Instagram", "Facebook", "TikTok", "Twitter"], "Twitter"),
    ("What does HTTP stand for?", ["HyperText Transfer Protocol", "HighText Transfer Protocol", "HyperTime Transfer Protocol", "Hyperlink Text Protocol"], "HyperText Transfer Protocol"),

    # Pop Culture
    ("Who played Iron Man in the Marvel Cinematic Universe?", ["Chris Evans", "Robert Downey Jr.", "Mark Ruffalo", "Chris Hemsworth"], "Robert Downey Jr."),
    ("What is the name of the fictional country in 'Black Panther'?", ["Wakanda", "Zamunda", "Narnia", "Gondor"], "Wakanda"),
    ("Which movie won the Oscar for Best Picture in 2020?", ["1917", "Joker", "Parasite", "Ford v Ferrari"], "Parasite"),
    ("Who is the author of the Harry Potter series?", ["J.K. Rowling", "Suzanne Collins", "George R.R. Martin", "Rick Riordan"], "J.K. Rowling"),
    ("Which artist sang 'Blinding Lights'?", ["The Weeknd", "Drake", "Post Malone", "Ed Sheeran"], "The Weeknd"),

    # Sports
    ("Which country hosted the 2016 Summer Olympics?", ["Brazil", "China", "United Kingdom", "Japan"], "Brazil"),
    ("Who holds the record for the most goals in World Cup history?", ["Lionel Messi", "Cristiano Ronaldo", "Marta", "Miroslav Klose"], "Miroslav Klose"),
    ("Which NBA player is known as 'The King'?", ["Stephen Curry", "Kobe Bryant", "LeBron James", "Shaquille O'Neal"], "LeBron James"),
    ("In tennis, how many Grand Slam titles did Roger Federer win?", ["15", "20", "18", "22"], "20"),
    ("Which country has won the most FIFA World Cup titles?", ["Germany", "Brazil", "Argentina", "Italy"], "Brazil"),

    # Literature
    ("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien"], "George Orwell"),
    ("Which book is known as 'The Great American Novel'?", ["The Catcher in the Rye", "Moby Dick", "The Great Gatsby", "To Kill a Mockingbird"], "The Great Gatsby"),
    ("Who is the author of 'Pride and Prejudice'?", ["Jane Austen", "Emily Brontë", "Charles Dickens", "Mark Twain"], "Jane Austen"),
    ("Which book series is authored by George R.R. Martin?", ["The Hunger Games", "The Wheel of Time", "A Song of Ice and Fire", "Percy Jackson"], "A Song of Ice and Fire"),
    ("Who wrote 'The Catcher in the Rye'?", ["F. Scott Fitzgerald", "J.D. Salinger", "William Faulkner", "Ernest Hemingway"], "J.D. Salinger"),

    # Science and Nature
    ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], "Diamond"),
    ("Which element is denoted by the symbol 'Fe'?", ["Lead", "Iron", "Fluorine", "Phosphorus"], "Iron"),
    ("How many bones are in the human body?", ["204", "205", "206", "207"], "206"),
    ("What is the tallest type of grass?", ["Bamboo", "Sugarcane", "Wheat", "Rice"], "Bamboo"),
    ("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Chloroplast", "Ribosome"], "Mitochondria"),

    # Movies
    ("Which movie is the highest-grossing film of all time?", ["Avatar", "Titanic", "Avengers: Endgame", "Star Wars: The Force Awakens"], "Avatar"),
    ("Who directed 'Inception'?", ["Steven Spielberg", "Quentin Tarantino", "Christopher Nolan", "Martin Scorsese"], "Christopher Nolan"),
    ("Which animated movie features a clownfish named Nemo?", ["The Little Mermaid", "Moana", "Finding Nemo", "Frozen"], "Finding Nemo"),
    ("Which movie features the quote 'May the Force be with you'?", ["Star Wars", "Star Trek", "The Matrix", "Harry Potter"], "Star Wars"),
    ("Which actor plays Captain Jack Sparrow in 'Pirates of the Caribbean'?", ["Orlando Bloom", "Johnny Depp", "Leonardo DiCaprio", "Matt Damon"], "Johnny Depp")
]

print("Welcome to the Quiz!")
total_score = run_quiz(questions)
print(f"\nYour final score is: {total_score}/{len(questions)}")
