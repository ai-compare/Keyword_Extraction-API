# Keyword Extraction - Eden AI API
## Description
This repositery provides code to implement Eden AI Keyword Extraction API. Eden AI Keyword Extraction API allows to call Keyword Extraction APIs from multpile keyword extraction providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is AI-Compare ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your IAM [here](https://app.edenai.run/admin/user).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://dev-api.edenai.run/v1/pretrained/text/keyword_extraction'
```
### Select parameters 
Set your text, the language, the attempted result, and providers APIs you want to run :
```python
payload = {'providers': '[\'ibm\', \'microsoft\', \'aws\']','text':'I am angry today', 'keywords_to_find': 'angry','language': 'en-US'}
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
<details>
<summary>

```json
{"result": [{"solution_name": "Ibm","execution_time": "1.648558","result": {"text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.","keywords": ["score of a document","much emotional content","magnitude of a document","overall emotion of a document","sentiment","value","document","length of the document"],"importances": [0.972786,0.763659,0.702109,0.68792,0.668512,0.569036,0.566432,0.301408]},"api_response": {"usage": {"text_units": 1,"text_characters": 257,"features": 1},"language": "en","keywords": [{"text": "score of a document","sentiment": {"score": -0.694655,"label": "negative"},"relevance": 0.972786,"emotion": {"sadness": 0.052462,"joy": 0.437899,"fear": 0.142496,"disgust": 0.00665,"anger": 0.152501},"count": 1},
```

</summary>

```


{
  "result": [
    {
      "solution_name": "Ibm",
      "execution_time": "1.648558",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "keywords": [
          "score of a document",
          "much emotional content",
          "magnitude of a document",
          "overall emotion of a document",
          "sentiment",
          "value",
          "document",
          "length of the document"
        ],
        "importances": [
          0.972786,
          0.763659,
          0.702109,
          0.68792,
          0.668512,
          0.569036,
          0.566432,
          0.301408
        ]
      },
      "api_response": {
        "usage": {
          "text_units": 1,
          "text_characters": 257,
          "features": 1
        },
        "language": "en",
        "keywords": [
          {
            "text": "score of a document",
            "sentiment": {
              "score": -0.694655,
              "label": "negative"
            },
            "relevance": 0.972786,
            "emotion": {
              "sadness": 0.052462,
              "joy": 0.437899,
              "fear": 0.142496,
              "disgust": 0.00665,
              "anger": 0.152501
            },
            "count": 1
          },
          {
            "text": "much emotional content",
            "sentiment": {
              "score": 0.393384,
              "label": "positive"
            },
            "relevance": 0.763659,
            "emotion": {
              "sadness": 0.051703,
              "joy": 0.42684,
              "fear": 0.037096,
              "disgust": 0.004724,
              "anger": 0.069528
            },
            "count": 1
          },
          {
            "text": "magnitude of a document",
            "sentiment": {
              "score": 0.393384,
              "label": "positive"
            },
            "relevance": 0.702109,
            "emotion": {
              "sadness": 0.051703,
              "joy": 0.42684,
              "fear": 0.037096,
              "disgust": 0.004724,
              "anger": 0.069528
            },
            "count": 1
          },
          {
            "text": "overall emotion of a document",
            "sentiment": {
              "score": -0.694655,
              "label": "negative"
            },
            "relevance": 0.68792,
            "emotion": {
              "sadness": 0.052462,
              "joy": 0.437899,
              "fear": 0.142496,
              "disgust": 0.00665,
              "anger": 0.152501
            },
            "count": 1
          },
          {
            "text": "sentiment",
            "sentiment": {
              "score": -0.38908,
              "mixed": "1",
              "label": "negative"
            },
            "relevance": 0.668512,
            "emotion": {
              "sadness": 0.045589,
              "joy": 0.531764,
              "fear": 0.053137,
              "disgust": 0.003094,
              "anger": 0.087609
            },
            "count": 2
          },
          {
            "text": "value",
            "sentiment": {
              "score": 0.393384,
              "label": "positive"
            },
            "relevance": 0.569036,
            "emotion": {
              "sadness": 0.051703,
              "joy": 0.42684,
              "fear": 0.037096,
              "disgust": 0.004724,
              "anger": 0.069528
            },
            "count": 1
          },
          {
            "text": "document",
            "sentiment": {
              "score": 0.393384,
              "label": "positive"
            },
            "relevance": 0.566432,
            "emotion": {
              "sadness": 0.045589,
              "joy": 0.531764,
              "fear": 0.053137,
              "disgust": 0.003094,
              "anger": 0.087609
            },
            "count": 1
          },
          {
            "text": "length of the document",
            "sentiment": {
              "score": 0.393384,
              "label": "positive"
            },
            "relevance": 0.301408,
            "emotion": {
              "sadness": 0.051703,
              "joy": 0.42684,
              "fear": 0.037096,
              "disgust": 0.004724,
              "anger": 0.069528
            },
            "count": 1
          }
        ]
      },
      "found_keywords": 1
    },
    {
      "solution_name": "Microsoft Azure",
      "execution_time": "0.345353",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "keywords": [
          "The score",
          "The magnitude",
          "document's sentiment indicates the overall emotion",
          "much emotional content is present within the document",
          "this value is often proportional to the length"
        ],
        "importances": [
          null,
          null,
          null,
          null,
          null
        ]
      },
      "api_response": {
        "documents": [
          {
            "id": "1",
            "keyPhrases": [
              "The score",
              "The magnitude",
              "document's sentiment indicates the overall emotion",
              "much emotional content is present within the document",
              "this value is often proportional to the length"
            ]
          }
        ],
        "errors": []
      },
      "found_keywords": 0
    },
    {
      "solution_name": "Amazon Web Services",
      "execution_time": "0.333118",
      "result": {
        "text": "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document.",
        "keywords": [
          "The score",
          "a document's sentiment",
          "the overall emotion",
          "a document",
          "The magnitude",
          "a document's sentiment",
          "emotional content",
          "the document",
          "this value",
          "the length",
          "the document"
        ],
        "importances": [
          0.9999992847442627,
          0.9999998807907104,
          0.9999999403953552,
          1,
          0.9999998211860657,
          0.9999992251396179,
          0.9995884895324707,
          1,
          0.999997615814209,
          1,
          0.9999987483024597
        ]
      },
      "api_response": {
        "KeyPhrases": [
          {
            "Score": 0.9999992847442627,
            "Text": "The score",
            "BeginOffset": 0,
            "EndOffset": 9
          },
          {
            "Score": 0.9999998807907104,
            "Text": "a document's sentiment",
            "BeginOffset": 13,
            "EndOffset": 35
          },
          {
            "Score": 0.9999999403953552,
            "Text": "the overall emotion",
            "BeginOffset": 46,
            "EndOffset": 65
          },
          {
            "Score": 1,
            "Text": "a document",
            "BeginOffset": 69,
            "EndOffset": 79
          },
          {
            "Score": 0.9999998211860657,
            "Text": "The magnitude",
            "BeginOffset": 81,
            "EndOffset": 94
          },
          {
            "Score": 0.9999992251396179,
            "Text": "a document's sentiment",
            "BeginOffset": 98,
            "EndOffset": 120
          },
          {
            "Score": 0.9995884895324707,
            "Text": "emotional content",
            "BeginOffset": 140,
            "EndOffset": 157
          },
          {
            "Score": 1,
            "Text": "the document",
            "BeginOffset": 176,
            "EndOffset": 188
          },
          {
            "Score": 0.999997615814209,
            "Text": "this value",
            "BeginOffset": 194,
            "EndOffset": 204
          },
          {
            "Score": 1,
            "Text": "the length",
            "BeginOffset": 230,
            "EndOffset": 240
          },
          {
            "Score": 0.9999987483024597,
            "Text": "the document",
            "BeginOffset": 244,
            "EndOffset": 256
          }
        ],
        "ResponseMetadata": {
          "RequestId": "03d4d457-3b63-4c18-9156-dc800a34dd42",
          "HTTPStatusCode": 200,
          "HTTPHeaders": {
            "x-amzn-requestid": "03d4d457-3b63-4c18-9156-dc800a34dd42",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "916",
            "date": "Tue, 10 Mar 2020 08:58:37 GMT"
          },
          "RetryAttempts": 0
        }
      },
      "found_keywords": 0
    }
  ]
}


```

</details>

## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](https://github.com/ai-compare/Speech_to_text-API/blob/ba9d4f1668d8758141f24240d1287640b4211c63/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)
