def main():
  """Prompts user for names and prints a farewell message."""

  names = []
  while True:
    try:
      name = input("Name: ").strip()
      names.append(name)
    except EOFError:
      break

  if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
  elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
  else:
    # Use comma and "and" for the last two names
    last_two = f"and {names[-1]}"
    # Join all other names with commas
    other_names = ", ".join(names[:-1])
    print(f"Adieu, adieu, to {other_names}, {last_two}")

if __name__ == "__main__":
  main()
