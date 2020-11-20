def rev_string(s):
  if s =="":
    return ""
  else:
    return s[-1] + rev_string(s[:-1])