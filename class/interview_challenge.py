word_list = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

def alphabetize_list(list):
  list.sort()

  for word in list:
    print(word)

alphabetize_list(word_list)