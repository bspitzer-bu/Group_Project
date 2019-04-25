library(magrittr)

rmsd_matrix <-
  readr::read_csv("cvs_files/rmsd.csv") %>%
  tibble::column_to_rownames(var = "X1") %>%
  base::as.matrix()

rmsd_matrix[lower.tri(rmsd_matrix, diag = TRUE)] <- NA

dfrtopics::gather_matrix(rmsd_matrix) %>%
  magrittr::set_colnames(base::c("gpcr1", "gpcr2", "rmsd")) %>%
  dplyr::mutate(id = NA_character_) %>%
  dplyr::mutate(sequence = NA_character_) %>%
  dplyr::select(id, gpcr1, gpcr2, rmsd, sequence) %>%
  dplyr::filter(!is.na(rmsd)) %>%
  readr::write_csv("cvs_files/similarities.csv", na = "")
