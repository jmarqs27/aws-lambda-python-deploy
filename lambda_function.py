import json
import log 

def lambda_handler(event, context):
    log.funcLog("Retornando um log: %s" % event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from BeOnUP!'),
        'Headers': json.dumps({"Content-Type": "application/json"}),
    }
