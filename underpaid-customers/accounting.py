MELON_COST = 1.00

def underpaid(filename):

    for line in open(filename):
        _, customer_name, customer_melons, customer_paid = line.rstrip().split('|')
        customer_paid = float(customer_paid)
        customer_expected = float(customer_melons) * MELON_COST
        print(f"{customer_name} paid ${customer_paid:.2f},",
            f"expected ${customer_expected:.2f}")
        if customer_expected < customer_paid:
            print(f"{customer_name} has overpaid for their melons.")
        elif customer_expected > customer_paid:
            print(f"{customer_name} has underpaid for their melons.")

underpaid('customer-orders.txt')