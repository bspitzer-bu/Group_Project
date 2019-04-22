library(magrittr)

pdbids <-
  base::list.files("src/media/fastas") %>%
  stringr::str_remove_all(".fasta") %>%
  stringr::str_c(collapse = ",")

customReportColumns <-
  base::c(
    "structureId",
    "structureTitle",
    "experimentalTechnique",
    "resolution",
    "classification",
    "pubmedId"
  ) %>%
  stringr::str_c(collapse = ",")

customReport <-
  base::paste0("https://www.rcsb.org/pdb/rest/customReport.csv") %>%
  base::paste0("?pdbids=", pdbids) %>%
  base::paste0("&customReportColumns=", customReportColumns) %>%
  base::paste0("&primaryOnly=1") %>%
  base::paste0("&service=wsfile") %>%
  base::paste0("&format=csv") %>%
  readr::read_csv() %>%
  dplyr::rename_all(snakecase::to_snake_case) %>%
  dplyr::rename_all(stringr::str_to_lower) %>%
  dplyr::rename(pdb_id = structure_id) %>%
  dplyr::rename(description = structure_title) %>%
  dplyr::rename(method = experimental_technique)

pdb_ids <-
  base::list.files("src/media/fastas") %>%
  stringr::str_remove_all(".fasta")

gpcrExpData <-
  readr::read_tsv("https://tinyurl.com/y427aow2", na = "N/A") %>%
  dplyr::rename_all(stringr::str_replace_all, " ", "_") %>%
  dplyr::rename_all(stringr::str_to_lower) %>%
  dplyr::filter(pdb_id %in% pdb_ids) %>%
  dplyr::select(pdb_id, gpcr_name, family, subfamily, uniprot_id, species) %>%
  dplyr::rename(name = gpcr_name)

dplyr::full_join(customReport, gpcrExpData) %>%
  dplyr::select(pdb_id, name, description, species, classification, family,
                subfamily, method, resolution, uniprot_id, pubmed_id) %>%
  dplyr::mutate_if(base::is.character, stringr::str_to_upper) %>%
  readr::write_csv("gpcr.csv")
