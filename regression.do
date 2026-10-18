import delimited "Data/datasets/daily_data.csv", clear varnames(1)

generate date = daily(substr(timestamp, 1, 10), "YMD")
format date %td
drop timestamp
order date
tsset date

regress energy L.sleep L(1/2).energy /*steps ages  oxygen respiration skin_temp stress heart_rate */

save "Data/datasets/daily_data.dta", replace