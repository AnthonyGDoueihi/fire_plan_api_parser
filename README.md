# Fire Plan Api Parser Lambda

This is a part of the Fire Action Plan Alexa Skill. A Cloudwatch service will run this endpoint every 10 minutes. This will call the Nasa's Realtime Fire Database and alert nearby Fire Action Plan Skill users of their nearby fires.

* [Fire Plan Alexa Lambda](https://github.com/AnthonyGDoueihi/fire_plan)

Made durint the NASA Space Apps 2019 Hackathon. Need help improving the flow of this.

## Deployment
You will need AWS Account, a user account with admin role and the following params in your environment:
~~~bash
export AWS_REGION=us-west-2
export aws_access_key_id=......
aws_secret_access_key=...
~~~
1. Login to your AWS account and create a Lambda function with Python runtime, leave the code empty.
2. Go to the location of the project and type: 
~~~bash
zip -r lambda.zip ./*
aws lambda update-function-code --function-name <your_function_name> --zip-file fileb://lambda.zip
~~~
3. The function should contain your code now.

## Built With 

* [Alexa](https://developer.amazon.com/documentation/)
* [Lambda](https://docs.aws.amazon.com/lambda/index.html)
* [NASA's Realtime Fire Database](https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-txt)
* [AWS CloudWatch](https://docs.aws.amazon.com/cloudwatch/index.html)

## TODO List
- 
