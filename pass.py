import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "1234567890"
symbol = "@#$_&-+()/*':!;?~`|•√π÷×¶∆\}{=°^¥€¢£%©®™✓[]><" 

all=lower + upper + NUMBER + symbol 
length = 10
password= "".join(random.sample(all,length))
print(" The Password You Generated Is :",password)
