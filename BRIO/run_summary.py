import json

jsonl_file = "../data/test-20news.jsonl"
texts = []
with open(jsonl_file, "r") as file:
    for line in file:
        json_obj = json.loads(line)
        text = json_obj["text"]
        texts.append(text)

from transformers import BartTokenizer, PegasusTokenizer
from transformers import BartForConditionalGeneration, PegasusForConditionalGeneration

IS_CNNDM = True # whether to use CNNDM dataset or XSum dataset
LOWER = False
# Load brio model checkpoints
if IS_CNNDM:
    model = BartForConditionalGeneration.from_pretrained('Yale-LILY/brio-cnndm-uncased')
    tokenizer = BartTokenizer.from_pretrained('Yale-LILY/brio-cnndm-uncased')
else:
    model = PegasusForConditionalGeneration.from_pretrained('Yale-LILY/brio-xsum-cased')
    tokenizer = PegasusTokenizer.from_pretrained('Yale-LILY/brio-xsum-cased')

max_length = 256 if IS_CNNDM else 512

summarys = []
for i in range(0, len(texts)):
    inputs = tokenizer([texts[i]], max_length=max_length, return_tensors="pt", truncation=True)
    # Generate Summary
    summary_ids = model.generate(inputs["input_ids"])
    summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    summarys.append(summary)

    #if (i+1)%100 == 0:
    #    print("The number of completed articles is：",i)

with open("../20news_brio_summary.txt", "w") as files:
    files.write("\n".join(summarys))
    print("Successfully saved!")
