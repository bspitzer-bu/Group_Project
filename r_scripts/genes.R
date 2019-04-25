readr::read_csv("cvs_files/gpcr.csv") %>%
  dplyr::select(id, gene_name) %>%
  dplyr::distinct() %>%
  readr::write_csv("cvs_files/genes.csv")
