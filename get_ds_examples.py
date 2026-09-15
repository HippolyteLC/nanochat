from tasks.smoltalk import SmolTalk
from tasks.gsm8k import GSM8K
from tasks.mmlu import MMLU

def get_ds_examples(n_examples, ds_list):
    for ds in ds_list:
        print(f"CURRENT DS: {ds}\n")
        for i in range(n_examples):
            print(f"Example {i+1}\n")
            print(ds.get_example(i), "\n")

if __name__ == "main":
    n_examples = 3
    ds_list = [
        SmolTalk(split='test', stop=n_examples), 
        GSM8K(split='test', stop=n_examples, subset='main'), 
        MMLU(split='test', stop=n_examples, subset='all')
    ]
    get_ds_examples(n_examples,ds_list)
