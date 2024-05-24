#  There is a JAR full of candies for sale at a mall counter. JAR has the capacity N, that is JAR can contain maximum N candies when JAR is full. At any point of time. JAR can have M number of Candies where M<=N. Candies are served to the customers. JAR never remains empty as when the last k candies are left. JAR is refilled with new candies in such a way that JAR get full. Write a code to implement the above scenario. Display JAR at the counter with the available number of candies. Input should be the number of candies one customer can order at a point of time. Update the JAR after each purchase and display JAR at Counter.

def candy_jar(min_candies,jar_capacity,customer_order):
    jar_candies = jar_capacity
    if customer_order <= 0:
        return "Invalid Input.."
    if customer_order > jar_candies:
        return "Invalid Input"
    jar_candies -= customer_order
    if jar_candies <= min_candies:
        refill_amount = jar_capacity - jar_candies
        jar_candies = jar_capacity

    print (f"NUMBER OF CANDIES SOLD: {customer_order}\n"
          f"NUMBER OF CANDIES AVAILABLE: {jar_candies}")


jar_capacity = 10
min_candies = 5
customer_order = int(input("Enter the number of candies you want: "))
candy_jar(jar_capacity,min_candies,customer_order)