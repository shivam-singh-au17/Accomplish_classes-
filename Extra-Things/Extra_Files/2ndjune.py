def dayCal(today, days):
  d = ['mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun']

  c = d.index(today)
  
  return(d [(c + days) % 7])

  # for i in range(days):
  #   c += 1
  #   if c > 6 :
  #     c = 0  
  # return (d[c])

print(dayCal('wed',8))