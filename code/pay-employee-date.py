def payEmployee(employeeId, hours, today):
  connectionId = 12332

  weekday = today.isoweekday() # 1 for Monday, 7 for Sunday

  if weekday == 7:
    r = paySundayTime(connectionId, employeeId, hours)
  else:
    r = payNormalTime(connectionId, employeeId, hours)
  return r
