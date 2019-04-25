library(magrittr)

pdbids <-
  base::list.files("src/media/fastas/") %>%
  stringr::str_remove_all(".fasta") %>%
  stringr::str_c(collapse = ",")

customReportColumns <-
  base::c(
    "structureId",
    "structureTitle",
    "experimentalTechnique",
    "resolution",
    "depositionDate",
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
  dplyr::select(pdb_id, gpcr_name, family, subfamily, uniprot_id, species,
                reference) %>%
  dplyr::rename(gpcr_class = family)

gpcr <-
  dplyr::full_join(customReport, gpcrExpData) %>%
  dplyr::mutate(id = NA_character_) %>%
  dplyr::select(id, pdb_id, gpcr_name, gpcr_class, subfamily, uniprot_id, species, description,
                method, resolution, pubmed_id, deposition_date, reference) %>%
  dplyr::mutate_if(base::is.character, stringr::str_to_upper)

uniprot_ids <-
  magrittr::use_series(gpcr, uniprot_id) %>%
  base::unique() %>%
  base::paste(collapse = ' ')

gene_names <-
  httr::POST(
    url = "https://www.uniprot.org/uploadlists/",
    body = list(
      from = 'ID',
      to = 'GENENAME',
      format = 'tab',
      query = uniprot_ids
    )
  ) %>%
  httr::content(
    type = 'text/tab-separated-values',
    col_names = TRUE,
    col_types = NULL,
    encoding = "UTF-8"
  )

dplyr::mutate(gpcr, gene_name = plyr::mapvalues(uniprot_id, gene_names$From, gene_names$To)) %>%
  dplyr::mutate(raw_pdb_file = base::paste0("raw_pdbs/", pdb_id, ".pdb")) %>%
  dplyr::mutate(mapping_pdb_file = base::paste0("mapped_pdb/", pdb_id, "_atlas.pdb")) %>%
  dplyr::mutate(fasta = base::paste0("fastas/", pdb_id, ".fasta")) %>%
  dplyr::mutate(gpcr_class = dplyr::case_when(
    gpcr_class == "CLASS A" ~ "a",
    gpcr_class == "CLASS F" ~ "f",
    gpcr_class == "CLASS B" ~ "b",
    gpcr_class == "CLASS C" ~ "c"
  )) %>%
  dplyr::mutate(method = dplyr::case_when(
    method == "X-RAY DIFFRACTION" ~ "x",
    method == "SOLUTION NMR" ~ "n",
    method == "SOLID-STATE NMR" ~ "s",
    method == "ELECTRON MICROSCOPY" ~ "e"
  )) %>%
  readr::write_csv("cvs_files/gpcr.csv", na = "")
