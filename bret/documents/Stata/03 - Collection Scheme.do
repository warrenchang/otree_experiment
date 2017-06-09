clear
set more off

* import data set
* import excel using <some_file.xls>, firstrow case(lower)
* import delimited using <some_file.csv>, delimiter(";")

* only keep variables of interest
keep player*
renpfix player
drop id_in_group role


/* **************************************************************************   
   Note that processing the collection scheme for all players might take
   some time. Depending on the number of boxes, iteratively assinging
   values to the box variables may take up to 10-20 seconds per subject. 
   ************************************************************************** */

* set number of rows (`m') and columns (`n')
local m = 10
local n = 10

	
* ---------------------------------------------------------------------------- *
* --- processing of collection scheme --- *
* ---------------------------------------------------------------------------- *
quietly {
  local N = `m'*`n'
  local K = `N'-1
  local J = `K'-1
  local P = _N

  replace boxes_scheme = subinstr(boxes_scheme,"},{","};{",.)
  replace boxes_scheme = substr(boxes_scheme,2,length(boxes_scheme)-2)

  qui sum boxes_collected
  local cb_max = r(max)

  // create box variables <box_`m'_'n'>
  forvalues i = 1 (1) `m' {
	  forvalues j = 1 (1) `n' {
      gen box_`i'_`j' = .
    }
  }

  // define locals with collected boxes per player
  forvalues p = 1 (1) `P' {
    local cb_max_`p' = boxes_collected[`p']
    dis `cb_max_`p''
  }

  // destring oTree scheme variable to format <`m',`n'>
  split boxes_scheme, parse(;) gen(cb_)
  forvalues k = 1 (1) `cb_max' {
    replace  cb_`k' = subinstr(cb_`k', `"{"row":"', "", .)
    replace  cb_`k' = subinstr(cb_`k', `""col":"', "", .)
    replace  cb_`k' = usubinstr(cb_`k', "}", "", .)
  }

  // set box variable to 1 if box is part of player's scheme
  forvalues p = 1 (1) `P' {
    forvalues i = 1 (1) `m' {
      forvalues j = 1 (1) `n' {
          forvalues k = 1 (1) `cb_max_`p'' {
          split cb_`k', parse(",") gen(cb_`k'_) 
          local cur_row = cb_`k'_1[`p']
          local cur_col = cb_`k'_2[`p']
          drop  cb_`k'_*
          replace box_`cur_row'_`cur_col' = 1 if `p' == _n
        }
      }
    }
  }
  drop boxes_scheme cb_*
}


// tabulate sum of cells in matrix format
quietly {
  collapse (sum) box_*
  forvalues j = 1 (1) `n' {
    gen col_`j' = .
    label variable col_`j' "Column `j'"
  }

  set obs `m'

  forvalues i = 1 (1) `m' {
    forvalues j = 1 (1) `n' {
		  replace col_`j' = box_`i'_`j'[1] if `i' == _n
    }
  }

	drop box_*
}
list

// reshape data for graph
quietly{
  gen row = _n
  reshape long col_, i(row)
  rename _j col
  rename col_ box_sum
}


* ---------------------------------------------------------------------------- *
* --- graph of total number of boxes selected --- *
* ---------------------------------------------------------------------------- *

quietly{
  sum box_sum
  gen cc = round((box_sum - r(min))/(r(max)-r(min))*255)
  levelsof cc, local(colors)

  local ln = `n'-1
  local l = 0.5
  while `l' < `ln' {
    local l = `l'+1
    local xl `xl'  `l'
  }
  local ln = `m'-1
  local l = 0.5
  while `l' < `ln' {
    local l = `l'+1
    local yl `yl'  `l'
  }


  local g
  foreach c of local colors {
    #delimit ;
    loc g `g' || scatter row col if cc==`c',
	               ms(S) msize(huge) mc("200 `c' 100")
							   xlabel(1(1)`n') ylabel(1(1)`m');
	  #delimit cr
  }

  #delimit ;
  local g `g' || scatter row col,
                 msymbol(i) mlabel(box_sum)
				  			 mlabcol(white) mlabp(0);
							 
  local g `g'    yscale(reverse noline) xscale(alt noline)
                 plotregion(margin(4.5 4.5 4.5 4.5) 
					  		 lcolor(gs12) lwidth(medium)) leg(off)
						  	 xline(`xl', lc(gs12))
                 yline(`yl', lc(gs12))
						  	 xtitle("") ytitle("");
							 
  local g `g'    ylabel(, labsize(small) labcolor(gray) 
                 angle(horizontal) labgap(small) noticks);

  local g `g'    xlabel(, labsize(small) labcolor(gray) 
                 angle(horizontal) labgap(vsmall) noticks);

  twoway  `g'    scheme(s1mono) xsize(3) ysize(3);
  #delimit cr

  drop cc
}
