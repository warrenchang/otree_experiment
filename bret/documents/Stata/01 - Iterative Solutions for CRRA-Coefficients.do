clear
set more off

* set number of rows (`n') and columns (`m') of BRET
local m = 10
local n = 10


* ---------------------------------------------------------------------------- *
* --- iterative solution for risk aversion coefficient r --- *
* ---------------------------------------------------------------------------- *
local N = `m'*`n'
local K = `N'-1
local J = `K'-1

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

forvalues j = 0 (1) `J' {
  local k = `j'+1
  if `j' != `J' {
    local r_`k'_m = (`r_`k'_l' + `r_`k'_u') / 2
    dis "if k = " %2.0f `k' ":  " %8.4f `r_`k'_l' ///
        " < r <"                  %8.4f `r_`k'_u' ///
        "       w\ mean ="        %8.4f `r_`k'_m'
  }
  else {
    dis "if k = " %2.0f `k' ":  " %8.4f `r_`k'_l' ///
        " < r"
  }
}
