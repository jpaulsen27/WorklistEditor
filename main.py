import editors.etoh

import editors.acidics

import editors.ultivotox

import editors.combined

import editors.bhp

import editors.functional

import editors.hcys

from os import listdir


def find_filenames(path_to_dir,  suffix=".csv"):
    worklists = listdir(path_to_dir)
    return [filename for filename in worklists if filename.endswith(suffix)]

#  File path set to only work on HERA instrument for testing will update in the future to be able to run universally.
#  Adding each file path possible is the working solution currently as a general directory search is too broad.


find_filenames(r"L:\Worklist Editor", suffix=".csv")
worklists = find_filenames(r"L:\Worklist Editor")
for name in worklists:
    if "ETOH_1_" in name:
        editors.etoh.etoh_1_build(name)
    if "ETOH_2_" in name:
        editors.etoh.etoh_2_build(name)
    if "ETOH_3_" in name:
        editors.etoh.etoh_3_build(name)
    if "ETOH_4_" in name:
        editors.etoh.etoh_4_build(name)
    if "ETOH_5_" in name:
        editors.etoh.etoh_5_build(name)
    if "ETOH_6_" in name:
        editors.etoh.etoh_6_build(name)
    if "ETOH_7_" in name:
        editors.etoh.etoh_7_build(name)
    if "ETOH_8_" in name:
        editors.etoh.etoh_8_build(name)
    if "ETOH_9_" in name:
        editors.etoh.etoh_9_build(name)
    if "ETOH_10_" in name:
        editors.etoh.etoh_10_build(name)
    if "ULTIVO_TOX_1_" in name:
        editors.ultivotox.ultivotox_1_build(name)
    if "ULTIVO_TOX_2_" in name:
        editors.ultivotox.ultivotox_2_build(name)
    if "ULTIVO_TOX_3_" in name:
        editors.ultivotox.ultivotox_3_build(name)
    if "ULTIVO_TOX_4_" in name:
        editors.ultivotox.ultivotox_4_build(name)
    if "ULTIVO_TOX_5_" in name:
        editors.ultivotox.ultivotox_5_build(name)
    if "ULTIVO_TOX_6_" in name:
        editors.ultivotox.ultivotox_6_build(name)
    if "ULTIVO_TOX_7_" in name:
        editors.ultivotox.ultivotox_7_build(name)
    if "ULTIVO_TOX_8_" in name:
        editors.ultivotox.ultivotox_8_build(name)
    if "ULTIVO_TOX_9_" in name:
        editors.ultivotox.ultivotox_9_build(name)
    if "ULTIVO_TOX_10_" in name:
        editors.ultivotox.ultivotox_10_build(name)
    if "ACIDIC_1_" in name:
        editors.acidics.acidics_1_build(name)
    if "ACIDIC_2_" in name:
        editors.acidics.acidics_2_build(name)
    if "ACIDIC_3_" in name:
        editors.acidics.acidics_3_build(name)
    if "ACIDIC_4_" in name:
        editors.acidics.acidics_4_build(name)
    if "ACIDIC_5_" in name:
        editors.acidics.acidics_5_build(name)
    if "ACIDIC_6_" in name:
        editors.acidics.acidics_6_build(name)
    if "ACIDIC_7_" in name:
        editors.acidics.acidics_7_build(name)
    if "ACIDIC_8_" in name:
        editors.acidics.acidics_8_build(name)
    if "ACIDIC_9_" in name:
        editors.acidics.acidics_9_build(name)
    if "ACIDIC_10_" in name:
        editors.acidics.acidics_10_build(name)
    if "COMBINED_1_" in name:
        editors.combined.combined_1_build(name)
    if "COMBINED_2_" in name:
        editors.combined.combined_2_build(name)
    if "COMBINED_3_" in name:
        editors.combined.combined_3_build(name)
    if "COMBINED_4_" in name:
        editors.combined.combined_4_build(name)
    if "COMBINED_5_" in name:
        editors.combined.combined_5_build(name)
    if "COMBINED_6_" in name:
        editors.combined.combined_6_build(name)
    if "COMBINED_7_" in name:
        editors.combined.combined_7_build(name)
    if "COMBINED_8_" in name:
        editors.combined.combined_8_build(name)
    if "COMBINED_9_" in name:
        editors.combined.combined_9_build(name)
    if "COMBINED_10_" in name:
        editors.combined.combined_10_build(name)
    if "BHP_1_" in name:
        editors.bhp.bhp_1_build(name)
    if "BHP_2_" in name:
        editors.bhp.bhp_2_build(name)
    if "BHP_3_" in name:
        editors.bhp.bhp_3_build(name)
    if "BHP_4_" in name:
        editors.bhp.bhp_4_build(name)
    if "BHP_5_" in name:
        editors.bhp.bhp_5_build(name)
    if "BHP_6_" in name:
        editors.bhp.bhp_6_build(name)
    if "BHP_7_" in name:
        editors.bhp.bhp_7_build(name)
    if "BHP_8_" in name:
        editors.bhp.bhp_8_build(name)
    if "BHP_9_" in name:
        editors.bhp.bhp_9_build(name)
    if "BHP_10_" in name:
        editors.bhp.bhp_10_build(name)
# Commented out functional and HCYS functionality.
    """if "Functional Biomarker_1_" in name:
        editors.functional.functional_1_build(name)
    if "Functional Biomarker_2_" in name:
        editors.functional.functional_2_build(name)
    if "Functional Biomarker_3_" in name:
        editors.functional.functional_3_build(name)
    if "Functional Biomarker_4_" in name:
        editors.functional.functional_4_build(name)
    if "Functional Biomarker_5_" in name:
        editors.functional.functional_5_build(name)
    if "Functional Biomarker_6_" in name:
        editors.functional.functional_6_build(name)
    if "Functional Biomarker_7_" in name:
        editors.functional.functional_7_build(name)
    if "Functional Biomarker_8_" in name:
        editors.functional.functional_8_build(name)
    if "Functional Biomarker_9_" in name:
        editors.functional.functional_9_build(name)
    if "Functional Biomarker_10_" in name:
        editors.functional.functional_10_build(name)
    if "Functional Biomarker_1_" in name:
        editors.hcys.hcys_1_build(name)
    if "Functional Biomarker_2_" in name:
        editors.hcys.hcys_2_build(name)
    if "Functional Biomarker_3_" in name:
        editors.hcys.hcys_3_build(name)
    if "Functional Biomarker_4_" in name:
        editors.hcys.hcys_4_build(name)
    if "Functional Biomarker_5_" in name:
        editors.hcys.hcys_5_build(name)
    if "Functional Biomarker_6_" in name:
        editors.hcys.hcys_6_build(name)
    if "Functional Biomarker_7_" in name:
        editors.hcys.hcys_7_build(name)
    if "Functional Biomarker_8_" in name:
        editors.hcys.hcys_8_build(name)
    if "Functional Biomarker_9_" in name:
        editors.hcys.hcys_9_build(name)
    if "Functional Biomarker_10_" in name:
        editors.hcys.hcys_10_build(name)"""
