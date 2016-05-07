import wikipedia
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        #wolframalpha
        app_id = "YOUR APP ID"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        #wikipedia
        print wikipedia.summary(input)
