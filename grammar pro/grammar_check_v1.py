import os
import openai

# openai.api_key = os.getenv("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")
openai.api_key = "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"

# message = "She no went to the market."
message = """Correct this to standard English:\n\nsir! i am C.D.BALAJI,  i am pursuing my M.com post graduation in SV university. 18 th december 2019 i participated consumerday district level elocution,
             i got first prize disrtict and state level also. 
             i have getten state level cash prize from ex.civil supply minister kodali nani sir. But district level cash prize 3000 rupees not received yet now , it is usefull for my educational expenses. 
             I kindly request you to please issue my prize money.                                            Thanking to you sir,"""
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message,
  temperature=0,
  max_tokens=3500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
# print(response)
print(response["choices"][0]["text"])