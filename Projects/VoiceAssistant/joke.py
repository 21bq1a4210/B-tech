from random import randint
JOKE = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He'll stop at nothing to avoid them!",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? Because it had too many problems.",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why was the calendar always getting in trouble? Because it had too many dates!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
    "What did the left eye say to the right eye? Between you and me, something smells.",
    "How does a penguin build its house? Igloos it together!",
    "What do you call fake spaghetti? An impasta!",
    "What's orange and sounds like a parrot? A carrot!",
    "I used to play piano by ear, but now I use my hands.",
    "Why don’t some couples go to the gym? Because some relationships don't work out!",
    "What did the duck say when it bought lipstick? Put it on my bill!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What do you get when you cross a snowman and a dog? Frostbite!",
    "What's the best thing about Switzerland? I don't know, but their flag is a big plus!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? Because it had too many problems.",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why was the calendar always getting in trouble? Because it had too many dates!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
    "What did the left eye say to the right eye? Between you and me, something smells.",
    "How does a penguin build its house? Igloos it together!",
    "What do you call fake spaghetti? An impasta!",
    "What's orange and sounds like a parrot? A carrot!",
    "I used to play piano by ear, but now I use my hands.",
    "Why don’t some couples go to the gym? Because some relationships don't work out!",
    "What did the duck say when it bought lipstick? Put it on my bill!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What do you get when you cross a snowman and a dog? Frostbite!",
    "What's the best thing about Switzerland? I don't know, but their flag is a big plus!",
]

jokes_list = ["Why don't scientists trust atoms? Because they make up everything.", "Parallel lines have so much in common. It's a shame they'll never meet.", "I told my wife she was drawing her eyebrows too high. She seemed surprised.", "Why don't skeletons fight each other? They don't have the guts.", "I used to play piano by ear, but now I use my hands.", "Did you hear about the claustrophobic astronaut? He just needed a little space.", "Why don't oysters donate to charity? Because they're shellfish.", "I'm reading a book about anti-gravity. It's impossible to put down.", "What did one wall say to the other wall? I'll meet you at the corner.", "Why was the math book sad? It had too many problems."]


def tellMeJoke():
    return JOKE[randint(0,len(JOKE))]

if __name__ == "__main__":
    print(len((set(JOKE))))