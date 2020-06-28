#source: https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
import re

def natsort(l): 
    convert=lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l,key=alphanum_key)