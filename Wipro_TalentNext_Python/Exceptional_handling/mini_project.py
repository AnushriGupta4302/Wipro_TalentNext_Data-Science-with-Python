'''
Ques1. You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time.

Sample Input 1.
Purchase-Tibet
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5
Sample output 1:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

Sample input 2:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup Free
(blank line)
Discount 80
Sample output 2:
Enter the file name: Purchase-1
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405
'''
def process_purchase_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        purchase_items = []
        free_items = []
        discount = 0
        section = 'purchase'
        for line in lines:
            line = line.strip()
            if line == "":
                if section == 'purchase':
                    section = 'free'
                elif section == 'free':
                    section = 'discount'
                continue
            if section == 'purchase':
                parts = line.split()
                if len(parts) != 2 or not parts[1].isdigit():
                    continue
                item, price = parts[0], int(parts[1])
                purchase_items.append((item, price))
            elif section == 'free':
                parts = line.split()
                if len(parts) == 2 and parts[1].lower() == "free":
                    free_items.append(parts[0])
            elif section == 'discount':
                parts = line.split()
                if len(parts) == 2 and parts[0].lower() == "discount":
                    if parts[1].isdigit():
                        discount = int(parts[1])
        amount_to_pay = sum(price for item, price in purchase_items)
        final_amount = amount_to_pay - discount
        print("No of items purchased:", len(purchase_items))
        print("No of free items:", len(free_items))
        print("Amount to pay:", amount_to_pay)
        print("Discount given:", discount)
        print("Final amount paid:", final_amount)
    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    except Exception as e:
        print("An error occurred:", e)
        
filename = input("Enter the file name: ")
if not filename.endswith('.txt'):
    filename += '.txt'
process_purchase_file(filename)