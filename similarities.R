library(magrittr)

readr::read_csv("rmsd.csv") %>%
  tibble::column_to_rownames(var = "X1") %>%
  base::as.matrix() %>%
  dfrtopics::gather_matrix() %>%
  magrittr::set_colnames(base::c("gpcr1", "gpcr2", "rmsd")) %>%
  dplyr::mutate(id = NA_character_) %>%
  dplyr::mutate(sequence = NA_character_) %>%
  dplyr::select(id, gpcr1, gpcr2, sequence) %>%
  readr::write_csv("similarities.csv", na = "")
