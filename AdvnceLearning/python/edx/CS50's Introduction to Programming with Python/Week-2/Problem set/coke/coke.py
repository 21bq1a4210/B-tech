def main():
    price = 50
    accepted_coins = [25, 10, 5]
    amount_inserted = 0

    while amount_inserted < price:
        print(f"Amount Due: {price - amount_inserted}")
        coin = int(input("Insert coin: ").strip())

        if coin in accepted_coins:
            amount_inserted += coin

    change = amount_inserted - price
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
