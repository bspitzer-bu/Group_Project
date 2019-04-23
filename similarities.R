library(magrittr)

readr::read_csv("rmsd.csv") %>%
  tibble::column_to_rownames(var = "X1") %>%
  base::as.matrix() %>%
  dfrtopics::gather_matrix() %>%
  magrittr::set_colnames(base::c("gpcr1", "gpcr2", "rmsd")) %>%
  readr::write_csv("similarities.csv")
