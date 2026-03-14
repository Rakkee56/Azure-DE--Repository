with open('my_claims.txt','w') as f:
    f.write('CLM-001,HDFC,50000,APPROVED\n')
    f.write('CLM-002,ICICI,75000,PENDING\n')
    f.write('CLM-003,LIC,30000,APPROVED\n')
    f.write('CLM-005,ICICI,15000,APPROVED\n')
    f.write('CLM-004,HDFC,90000,REJECTED\n')

with open('my_claims.txt','r') as f:
    content = f.read()
    print(content)

with open('my_claims.txt','r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)

with open('my_claims.txt','r') as f:
    for line in f:
        print(f"Processing : {line.strip()}")

with open('my_claims.txt','a') as f:
    f.write('CLM-006,LIC,45000,PENDING\n')

with open('my_claims.txt','r') as f:
    for line in f:
        print(line.strip())

with open('my_claims.txt','r') as f:
    line3 = f.readlines()
    print(line3)


with open('my_new.csv','w') as f:
    f.write('rakesh')


with open('my_new.csv','r') as f:
    line4 = f.read()
    print(line4)

with open('warmup.txt','w') as f:
    f.write('CLM-001,HDFC,50000,APPROVED\n')
    f.write('CLM-002,ICICI,75000,PENDING\n')
    f.write('CLM-003,LIC,30000,APPROVED\n')

with open('warmup.txt','r') as f:
    content = f.read()
    print(content)

with open('warmup.txt','r') as f:
    for line in f:
        print(f"line: {line.strip()}")

import csv

with open('claims.csv','w',newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(['claimid','name','amount','status'])
    writer.writerow(['CLM-001','Rakesh',5000,'APPROVED'])
    writer.writerow(['CLM-002', 'Raam', 5000, 'PENDING'])


with open('claims.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row[0])
        print(row[2])
        print('=' * 50)

with open('claims.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['claimid'])
        print(row['amount'])

with open('insurance_claims.csv','w',newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(['claim_id', 'insurer', 'amount','status', 'city', 'claim_type'])
    writer.writerow(['CLM-001','HDFC',50000,'APPROVED','Chennai','MOTOR'])
    writer.writerow(['CLM-002','ICICI',75000,'PENDING','Mumbai','HEALTH'])
    writer.writerow(['CLM-003','LIC',30000,'APPROVED','Delhi','LIFE'])
    writer.writerow(['CLM-004','HDFC',90000,'REJECTED','Chennai','MOTOR'])
    writer.writerow(['CLM-005','ICICI','15000','APPROVED','Bangalore','HEALTH'])


with open('insurance_claims.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(f"row : {row}")


with open('insurance_claims.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['claim_id']} |"
              f"{row['insurer']} |"
              f"RS. {row['amount']} |"
              f"{row['status']}")

with open('insurance_claims.csv','r') as f:
    reader = csv.DictReader(f)
    approved = [row for row in reader if row['status'] == 'APPROVED']
    print(f"Approved Claims: {len(approved)}")
    for c in approved:
        print(c['claim_id'],c['amount'])

with open('approved_claims.csv','w',newline = "") as f:
    writer = csv.DictWriter(f,fieldnames = ['claim_id', 'insurer', 'amount','status', 'city', 'claim_type'])
    writer.writeheader()
    writer.writerows(approved)
    print("Approved claims written!")

with open('approved_claims.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


claim1 = {"claim_id":"CLM-001",
           "amount":"50000",
           "status":"APPROVED"}

claim2 = {"claim_id":"CLM-002",
           "amount":"INVALID",
           "status":"APPROVED"}

claim3 = {"claim_id":"CLM-003",
           "amount":"-5000",
           "status":"APPROVED"}

claim4 = {"claim_id":"CLM-004",
           "amount":"30000",
           "status":"UNKNOWN"}

VALID_STATUSES = ['APPROVED','PENDING','REJECTED']


def process_claim(claim):
    print(f"Processing {claim['claim_id']}....")
    try:
        amount = int(claim['amount'])

        if amount <=0:
            raise ValueError('ValueError: Amount must be positive!')

        if claim['status'] not in VALID_STATUSES:
            raise ValueError('INVALID STATUSES')

        print(f" valid claim!"
            f"Amount : Rs.{amount}")
        return claim

    except ValueError as e:
        print(f"ValueError : {e}")
        return None

    finally:
        print(f"Processing Attempt done\n")


process_claim(claim1)
process_claim(claim2)
process_claim(claim3)
process_claim(claim4)


class PipelineError(Exception):
    pass

class DataQualityError(PipelineError):
    pass

class FileNotReceivedError(PipelineError):
    pass

def validate_claims(claims):
    try:
        if claims is None:
            raise FileNotReceivedError("No claims data received!")

        if len(claims) == 0:
            raise DataQualityError('Empty Claims list!')

        null_ids = [c for c in claims if not c['claim_id']]
        if len(null_ids) > 0:
            raise DataQualityError ('Found null claim_ids !')

        rejected = [c for c in claims if c['status'] == 'REJECTED']
        rate = len(rejected)/len(claims) * 100
        if rate > 50:
            raise DataQualityError('Rejection rates too high')

        print('All validations passed')

    except FileNotReceivedError as e:
        print(f"FileNotReceivedError : {e}")

    except  DataQualityError as e:
        print(f"DataQualityError : {e}")



validate_claims(None)
validate_claims([])
validate_claims([ {"claim_id":"CLM-001","status":"APPROVED"},
    {"claim_id":"CLM-002","status":"APPROVED"},
    {"claim_id":"CLM-003","status":"REJECTED"},])
validate_claims([{"claim_id":"CLM-001","status":"REJECTED"},
    {"claim_id":"CLM-002","status":"REJECTED"},
    {"claim_id":"CLM-003","status":"APPROVED"},])
