import wolframalpha

input = raw_input("Q: ")
app_id = "YOUR APP ID"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer
