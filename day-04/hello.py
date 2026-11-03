import anthropic

client = anthropic.Anthropic()

msg = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=60,
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ],
)

print(msg.content[0].text)
print("Input tokens:", msg.usage.input_tokens)
print("Output tokens:", msg.usage.output_tokens)