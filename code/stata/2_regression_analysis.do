* Import data
use "data/derived/tender_data_analysis.dta", clear

* Keep only tenders with a single winning country
keep if strlen(win_country_code) == 2

* Create a variable that shows whether winning country is the same as the issuing country
// gen same_country = 0
// replace same_country = 1 if iso_country_code == win_country_code 

gen same_country = (iso_country_code == win_country_code)

* Tabulate frequency
tabulate same_country

*Now we also want to look at multi-country tenders
use "data/derived/tender_data_analysis.dta", clear

// if error drop country_*

*We wanna check whether the issuing country is contained in the winning countries

gen same_country = strpos(win_country_cod, iso_country_code) // yields starting index of win_country_code
replace same_country = 1 if same_country > 1


* Do the same things but differently
gen same_country2 = 0

split win_country_code, parse("---") generate(country_)

forvalues i = 1/ `r(k_new)' {
	replace same_country2 = 1 if iso_country_code == country_`i'
	drop country_`i'
}

* Check if they did the same.
assert same_country == same_country2

* Does the value of the tender differ if home firm win?
regress award_value_euro same_country

* In logs
regress ln_award_value_euro same_country

di exp(_b[same_country])-1

*Merge country info
merge m:1 iso_country_code using "data/derived/country_codes"

