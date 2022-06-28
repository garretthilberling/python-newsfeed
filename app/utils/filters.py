def format_date(date):
    # strftime method converts to string, %m/%d/%y specifies format
    return date.strftime('%m/%d/%y')

def format_url(url):
    # replace() behaves like split() in js
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word
