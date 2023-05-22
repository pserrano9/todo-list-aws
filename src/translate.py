import json
import decimalencoder
import todoList
import boto3


def getTranslated(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])

    if item:
        translate = boto3.client('translate')
        language = event['pathParameters']['language']
        item['text'] = translate.translate_text(Text=item['text'],
                                                SourceLanguageCode="auto",
                                                TargetLanguageCode=language)
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
