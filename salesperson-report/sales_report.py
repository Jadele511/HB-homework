"""Generate sales report showing total melons each salesperson sold."""


report = {}

f = open('sales-report.txt')
for line in f:
    salesperson, _, melons = line.rstrip().split('|')
    melons = int(melons)
    if salesperson in report:
        report[salesperson] += melons
    else:
        report[salesperson] = melons

for salesperson, melons in report.items():
    print(f'{salesperson} sold {melons} melons')
