import json
import decimalencoder
import todoList
import boto3


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])

    if item:
        translate = boto3.client('translate')
        language = event['pathParameters']['language']
        translation = translate.translate_text(item['text'],
                                               SourceLanguageCode="auto",
                                               TargetLanguageCode=language)
        item['text'] = str(translation['TranslatedText'])
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
