clear
set more off

* import data set
* import excel using <some_file.xls>, firstrow case(lower)
* import delimited using <some_file.csv>, delimiter(";")

* only keep variables of interest
keep player*
renpfix player
drop id_in_group role boxes_scheme



* set number of rows (`n') and columns (`m') of BRET
local m = 10
local n = 10


* ---------------------------------------------------------------------------- *
* --- iterative solution for risk aversion coefficient r --- *
* ---------------------------------------------------------------------------- *
local N = `m'*`n'
local K = `N'-1
local J = `K'-1

// determine lower and upper bound of r iteratively
local r = 0
forvalues k = 1 (1) `K' {
  local d = .
	
  while `d' > 0.00001 {
    local r = `r' + 0.00001*`k'
    local d = (`k'-1)^`r' * (`N'-`k'+1)/`N' - ///
              (`k')  ^`r' * (`N'-`k')  /`N'

    if `d' < 0.00001 {
      local j = `k'-1
      local r_`k'_l = `r'
      local r_`j'_u = `r'-0.0001
    }
  }
}

// compute mean r value of range
forvalues j = 0 (1) `J' {
  local k = `j'+1
  if `j' != `J' {
    local r_`k'_m = (`r_`k'_l' + `r_`k'_u') / 2
  }
}

qui gen r_l = .   // lower bound risk aversion coefficient r
qui gen r_u = .   // upper bound risk aversion coefficient r
qui gen r_m = .   // mean risk aversion coefficient r


// assign iteratively determined coefficients
forvalues k = 1 (1) `J' {
  qui replace r_l = `r_`k'_l' if boxes_collected == `k'
  qui replace r_u = `r_`k'_u' if boxes_collected == `k'
  qui replace r_m = `r_`k'_m' if boxes_collected == `k'
}

