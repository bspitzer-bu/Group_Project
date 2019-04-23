library(magrittr)

pdbids <-
  base::list.files("src/media/fastas") %>%
  stringr::str_remove_all(".fasta") %>%
  stringr::str_c(collapse = ",")

base::paste0("https://www.rcsb.org/pdb/rest/customReport.csv") %>%
  base::paste0("?pdbids=", pdbids) %>%
  base::paste0("&reportName=Ligands") %>%
  base::paste0("&service=wsfile") %>%
  base::paste0("&format=csv") %>%
  readr::read_csv() %>%
  dplyr::rename_all(snakecase::to_snake_case) %>%
  dplyr::filter(!base::is.na(ligand_id)) %>%
  dplyr::mutate(id = NA_character_) %>%
  dplyr::select(id, structure_id, ligand_id) %>%
  dplyr::rename(pdb_id = structure_id) %>%
  dplyr::distinct() %>%
  readr::write_csv("binds.csv", na = "")
