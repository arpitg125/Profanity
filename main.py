def degree_of_profanity(comment_file,bad_word_list):
  txt_file = open(comment_file)
  profanity_index=[]
  for line in txt_file:
    words = line.split()
    index=0
    for i in range(len(bad_word_list)):
      for j in range(len(words)):
        if bad_word_list[i]==words[j]:
          index +=1
    profanity_index.append(index)
  return profanity_index
