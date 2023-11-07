import requests
import json
import sys

host = 'smoking-serving-env.eba-rfk3vyqz.us-west-1.elasticbeanstalk.com'
url_cloud = f'http://{host}:/predict'
url_local = f'http://localhost:9696/predict'

patient = {
    "age": 3.58351893845611,
    "height(cm)": 5.170483995038151,
    "weight(kg)": 4.030733340286331,
    "waist(cm)": 4.406719247264253,
    "eyesight(left)": 0.7884573603642702,
    "eyesight(right)": 0.6931471805599453,
    "hearing(left)": 0.6931471805599453,
    "hearing(right)": 0.6931471805599453,
    "systolic bp": 4.852030263919617,
    "diastolic bp": 4.204692619390966,
    "fasting blood sugar": 4.394449154672439,
    "Cholesterol": 5.151858133476067,
    "triglyceride": 5.90947179518496,
    "HDL": 4.127134385045092,
    "LDL": 4.584967478670572,
    "hemoglobin": 2.8213788864092133,
    "Urine protein": 0.6931471805599453,
    "serum creatinine": 0.6931471805599453,
    "AST": 3.4657359027997265,
    "ALT": 3.5263605246161616,
    "GGT": 4.553876891600541,
    "dental cavities": 0.6931471805599453
}

if len(sys.argv) > 1 and sys.argv[1] == "--local":
    print("Testing local")
    response = json.dumps(requests.post(url_local, json=patient).json())
else:
    print("Testing cloud")
    response = json.dumps(requests.post(url_cloud, json=patient).json())

print(response)
