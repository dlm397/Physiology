do "Data/dataGet.do" daily_data

generate date = daily(substr(timestamp, 1, 10), "YMD")
format date %td
drop timestamp
order date
tsset date

regress energy L.sleep L(1/2).energy /*steps ages  oxygen respiration skin_temp stress heart_rate */

do "Data/dataGet.do" sleep_events

describe
summarize
