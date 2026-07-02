print("#"*60)
print(" Welcome to our Instant Discount System ".center(50,'#'))
print("#"*60)
purchase_price=float(input("Enter your purchase price: "))
if purchase_price < 100:
    print(f"your purchase price {purchase_price}, you are not eligible for a discount.")


elif purchase_price >= 100 and purchase_price < 500:
    print(f"your purchase price {purchase_price}, you are eligible for a 10% discount.")
    discount=purchase_price * 0.10
    print(f"discount amount is {discount}")
    final_price=purchase_price - discount
    print(f"Your final price after discount is {final_price}.")
    

elif purchase_price >= 500 :
    print(f"your purchase price {purchase_price}, you are eligible for a 20% discount.")
    discount=purchase_price * 0.20
    print(f"discount amount is {discount}")
    final_price=purchase_price - discount
    print(f"Your final price after discount is {final_price}.")     

