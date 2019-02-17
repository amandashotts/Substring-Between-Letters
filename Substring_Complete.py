

def substring_between_letters(word, start, end):
  starting_ind = word.find(start) +1
  ending_ind = word.find(end)

  if ending_ind != -1:
  	return word[starting_ind: ending_ind]
  else:
    return word

  
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
