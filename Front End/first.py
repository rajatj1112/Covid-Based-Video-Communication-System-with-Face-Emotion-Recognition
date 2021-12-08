list1 = []
def count_char(text):
  for i in range(len(text)):
    
    if len(text) == 0:
      break;
    ch = text[0]
    if ch == ' ' or ch == '\t':
      continue
    #print(ch + " - ", text.count(ch))
    if(text.count(ch)==1):
        list1.append(ch)
    text = text.replace(ch, '').strip()
  
input1 = input()
count_char(input1)
print(list1[0])