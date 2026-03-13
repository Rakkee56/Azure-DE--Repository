add_gst = lambda amount: amount * 5

print(add_gst(5000))

calc_total = lambda amount,gst_rate : amount + (amount*gst_rate)

print(calc_total(1000,1))

# Sorting list of dicts by amount!
claims = [
    {"id": "CLM-001", "amount": 50000},
    {"id": "CLM-002", "amount": 15000},
    {"id": "CLM-003", "amount": 75000},
]

print(claims)

sorted_claims = sorted(claims, key = lambda x : x['amount'])
print(sorted_claims)

for i in sorted_claims:
    print(i)



get_gst = lambda amount,gst : amount + (amount * 0.18)

print(get_gst(1000,0.18))


is_approved = lambda status : status.upper() == 'APPROVED'

print(is_approved('Approved'))

upper_case = lambda city : city.upper()

print(upper_case('chennai'))


claims = [
    {"id":"CLM-001", "amount":50000},
    {"id":"CLM-002", "amount":15000},
    {"id":"CLM-003", "amount":75000},
    {"id":"CLM-004", "amount":30000},
]

sorted_values = sorted(claims,key = lambda x : x['amount'],reverse=True)
print(sorted_values)

sorted_values_asc = sorted(claims,key = lambda x : x['amount'],reverse=False)
print(sorted_values_asc)

for i in sorted_values:
    print(i)

for i in sorted_values_asc:
    print(i)

amounts = [50000, 75000, 30000, 90000, 15000]

a = []
for amount in amounts:
    a.append (amount*2)

print(a)

get_list = list(map(lambda x : x * 2, amounts))

print(get_list)

amounts = [50000, 75000, 30000, 90000, 15000]

get_gst = list(map(lambda x : x * 0.18,amounts))
print(get_gst)

total = list(map(lambda x : x + (x*0.18), amounts))
print(total)

cities = ["chennai", "mumbai",
          "delhi", "bangalore"]

upp_city = list(map(lambda x : x.upper(),cities))
print(upp_city)

amounts = [50000, 75000, 30000, 90000, 15000]
cities  = ["chennai", "mumbai",
           "delhi",   "bangalore"]
statuses = ["approved", "pending",
            "REJECTED", "Approved"]


fees = list(map(lambda x : x*0.02,amounts))
print(fees)

pre_city = list(map(lambda x : 'CITY - ' + x, cities))
print(pre_city)

upp_status = list(map(lambda x : x.upper(),statuses))
print(upp_status)

net_amount = list(map(lambda x : x - (x*0.18), amounts))
print(net_amount)

amounts  = [50000, 75000, 30000,
            90000, 15000, 45000]
statuses = ["APPROVED", "PENDING",
            "REJECTED", "APPROVED",
            "PENDING",  "APPROVED"]
cities   = ["Chennai", "Mumbai",
            "Chennai", "Delhi",
            "Bangalore", "Chennai"]
names    = ["Rakesh", "Raam",
            "Priya",  "Arjun",
            "Rishi",  "Deepa"]

high = list(filter(lambda x : x > 40000, amounts))
print(high)

rejected = list(filter(lambda x : x == 'REJECTED', statuses))
print(rejected)

chennai_claims = list(filter(lambda x : x == 'Chennai', cities))
print(chennai_claims)

mid_range = list(filter(lambda x : x >= 30000 and x <= 80000, amounts))
print(mid_range)

long = list(filter(lambda x : len(x) > 4, names))
print(long)


amounts = [50000, 75000, 30000, 90000, 15000]

high = [x + x * 2 for x in amounts if x > 30000]
print(high)

claims = [
    {"id":"CLM-001","amount":50000,
     "status":"APPROVED"},
    {"id":"CLM-002","amount":75000,
     "status":"PENDING"},
    {"id":"CLM-003","amount":30000,
     "status":"approved"}
]


high2 = [c['amount'] for c in claims if c['status'].upper() == 'APPROVED']
print(high2)


amounts  = [50000, 75000, 30000, 90000, 15000]
statuses = ["APPROVED", "PENDING",
            "REJECTED", "approved", "PENDING"]

high3 = [x for x in amounts if statuses[amounts.index(x)].upper() == 'APPROVED']
print(high3)
ids = [c['id'] for c in claims]
print(ids)

amounts  = [50000, 75000, 30000,
            90000, 15000, 45000]
cities   = ["chennai", "mumbai",
            "chennai", "delhi",
            "bangalore", "chennai"]
claims   = [
    {"id":"CLM-001","amount":50000,
     "status":"APPROVED","city":"Chennai"},
    {"id":"CLM-002","amount":75000,
     "status":"PENDING","city":"Mumbai"},
    {"id":"CLM-003","amount":30000,
     "status":"APPROVED","city":"Chennai"},
    {"id":"CLM-004","amount":90000,
     "status":"REJECTED","city":"Delhi"},
    {"id":"CLM-005","amount":15000,
     "status":"APPROVED","city":"Chennai"},
    {"id":"CLM-006","amount":45000,
     "status":"PENDING","city":"Mumbai"},
]

totals = [x + x * 0.18 for x in amounts]
print(totals)

upp_cities = [x.upper() for x in cities]
print(upp_cities)

high = [x for x in amounts if x > 40000]
print(high)

ids = [c['id'] for c in claims]
print(ids)

app_ids = [c['id'] for c in claims if c['status'] == 'APPROVED']
print(app_ids)

chennai_amounts = [c['amount'] for c in claims if c['city'] == "Chennai"]
print(chennai_amounts)

app_gst = [c['amount'] * 0.18 for c in claims if c['status'] == 'APPROVED']
print(app_gst)

