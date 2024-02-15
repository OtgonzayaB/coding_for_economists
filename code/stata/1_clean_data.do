* Load data
import delimited "data/raw/european_commission/ted-sample.csv", clear

* Only keep relevant variables
keep iso_country_code win_country_code award_value_euro

* Summarize award_value_zero
summarize award_value_euro, detail 
// display "Number of observations: `r(N)'"
// display "mean: `r(mean)'"

* Drop outliers
// drop if award_value_euro > `r(p95)'

* Plot the distribution of award_value_euro
hist award_value_euro // large outliers

* Create a logged variable
gen ln_award_value_euro = ln(award_value_euro)
hist ln_award_value_euro

* Let's generate an indicator: 1 (above mean), 0 otherwise
generate above_mean = (award_value_euro > `r(p50)')

save "data/derived/tender_data_analysis.dta", replace

* Import country codes and save as .dta
import delimited using "data/raw/country_codes/country_codes.csv", clear

* Little excursion: Looping in Stata
forvalues i = 0/10 {
	display `i'
}

* foreach
foreach vegetable in paprika aubergine carrot {
	display 'vegetable'
}

*foreach (2)
foreach var in varlist iso_country_code win_country_code {
	count if strlen(`var') > 2 
}
