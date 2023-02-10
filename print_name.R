# author: Tiffany Timbers
# date: 2020-04-25

"Takes preferred name and surname arguments,
concatenates them and prints the name.

Usage: print_name.R <preferred_name> --surname=<surname>

Options:
<preferred_name>       Preferred name
--surname=<surname>    Surname
" -> doc

library(docopt)

opt <- docopt(doc)
name <- paste(opt$preferred_name, opt$surname)
print(name)