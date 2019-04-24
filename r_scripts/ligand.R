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
  dplyr::select(id, ligand_id, ligand_name, ligand_formula, ligand_molecular_weight,
                in_ch_i_key) %>%
  dplyr::rename(name = ligand_name) %>%
  dplyr::rename(formula = ligand_formula) %>%
  dplyr::rename(molecular_weight = ligand_molecular_weight) %>%
  dplyr::rename(inchi_key = in_ch_i_key) %>%
  dplyr::mutate_if(base::is.character, stringr::str_to_upper) %>%
  dplyr::distinct() %>%
  readr::write_csv("ligand.csv", na = "")
