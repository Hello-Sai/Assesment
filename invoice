print("Book1 - Introduction to Python Programming : Rs 499.00\nBook2 - Python Libraries Cookbook : Rs. 855.00\nBook3 - Data Science in Python : Rs. 645.00\n")
dic = {
    1 : 499.00,
    2 : 855.00,
    3 : 645.00
}

def books_amt(book1, book2, book3):
    total_books_value = dic[1]*book1+dic[2]*book2+dic[3]*book3
    if total_books_value == 0:
        print("Invalid input please check again")
        exit(0)
    delivery_charges = 250.00
    gst = total_books_value * 0.12
    final_price = total_books_value + gst +delivery_charges
    print("===============================================")
    print("The total invoice amount is: {}".format(final_price))
if _name== '__main_':
    try:
        book1=int(input("Book1 how many books you need: "))
        book2=int(input("Book2 how many books you need: "))
        book3=int(input("Book3 how many books you need: "))
    except Exception as e:
        print("***************************************************")
        print("Plese enter number of books you want(integer value)")
        exit(0)
    books_amt(book1, book2,book3)
