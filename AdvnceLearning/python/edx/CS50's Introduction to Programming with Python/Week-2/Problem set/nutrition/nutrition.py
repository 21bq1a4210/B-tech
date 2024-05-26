fruits_data = {
    "apple": 130,
    "avocado": 50,
    "banana": 105,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 80,
    "honeydew melon": 50,
    "kiwifruit": 90,  # Added Kiwifruit with correct capitalization
    "mango": 100,
    "nectarine": 60,
    "orange": 60,
    "papaya": 55,
    "peach": 60,
    "pear": 100,  # Updated calorie count for pear
    "pineapple": 80,
    "plums": 70,
    "raspberries": 60,
    "strawberries": 50,
    "tangerine": 50,
    "watermelon": 46,
    "sweet cherries": 100,  # Added Sweet Cherries
}

def get_calories(fruit):
  """
  Gets the number of calories in a fruit (case-insensitively).

  Args:
      fruit: The name of the fruit (string).

  Returns:
      The number of calories in one serving of the fruit (integer),
      or None if the fruit is not found.
  """
  fruit_lower = fruit.lower()
  return fruits_data.get(fruit_lower)

def main():
  """Prompts the user for a fruit and outputs its calorie count."""
  fruit = input("Enter a fruit (case-insensitive): ")
  calories = get_calories(fruit)
  if calories:
    print(calories)  # Print only the calorie count

if __name__ == "__main__":
  main()
