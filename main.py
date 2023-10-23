import editors.etoh

import editors.acidics

import editors.ultivotox

import editors.combined

import editors.bhp

import editors.functional

import editors.hcys

from os import listdir

from datetime import date

import os


def find_filenames(path_to_dir, suffix=".csv"):
    worklists = listdir(path_to_dir)
    return [filename for filename in worklists if filename.endswith(suffix)]


today = date.today()
today_corrected = str(today.strftime('%m%d%y'))
find_filenames(r"L:\\", suffix=".csv")
worklists = find_filenames(r"L:\\")
for name in worklists:
    if "ETOH_1_" + today_corrected in name:
        editors.etoh.etoh_1_build(name)
    if "ETOH_2_" + today_corrected in name:
        editors.etoh.etoh_2_build(name)
    if "ETOH_3_" + today_corrected in name:
        editors.etoh.etoh_3_build(name)
    if "ETOH_4_" + today_corrected in name:
        editors.etoh.etoh_4_build(name)
    if "ETOH_5_" + today_corrected in name:
        editors.etoh.etoh_5_build(name)
    if "ETOH_6_" + today_corrected in name:
        editors.etoh.etoh_6_build(name)
    if "ETOH_7_" + today_corrected in name:
        editors.etoh.etoh_7_build(name)
    if "ETOH_8_" + today_corrected in name:
        editors.etoh.etoh_8_build(name)
    if "ETOH_9_" + today_corrected in name:
        editors.etoh.etoh_9_build(name)
    if "ETOH_10_" + today_corrected in name:
        editors.etoh.etoh_10_build(name)
    if "ULTIVO_TOX_1_" + today_corrected in name:
        editors.ultivotox.ultivotox_1_build(name)
    if "ULTIVO_TOX_2_" + today_corrected in name:
        editors.ultivotox.ultivotox_2_build(name)
    if "ULTIVO_TOX_3_" + today_corrected in name:
        editors.ultivotox.ultivotox_3_build(name)
    if "ULTIVO_TOX_4_" + today_corrected in name:
        editors.ultivotox.ultivotox_4_build(name)
    if "ULTIVO_TOX_5_" + today_corrected in name:
        editors.ultivotox.ultivotox_5_build(name)
    if "ULTIVO_TOX_6_" + today_corrected in name:
        editors.ultivotox.ultivotox_6_build(name)
    if "ULTIVO_TOX_7_" + today_corrected in name:
        editors.ultivotox.ultivotox_7_build(name)
    if "ULTIVO_TOX_8_" + today_corrected in name:
        editors.ultivotox.ultivotox_8_build(name)
    if "ULTIVO_TOX_9_" + today_corrected in name:
        editors.ultivotox.ultivotox_9_build(name)
    if "ULTIVO_TOX_10_" + today_corrected in name:
        editors.ultivotox.ultivotox_10_build(name)
    if "ACIDIC_1_" + today_corrected in name:
        editors.acidics.acidics_1_build(name)
    if "ACIDIC_2_" + today_corrected in name:
        editors.acidics.acidics_2_build(name)
    if "ACIDIC_3_" + today_corrected in name:
        editors.acidics.acidics_3_build(name)
    if "ACIDIC_4_" + today_corrected in name:
        editors.acidics.acidics_4_build(name)
    if "ACIDIC_5_" + today_corrected in name:
        editors.acidics.acidics_5_build(name)
    if "ACIDIC_6_" + today_corrected in name:
        editors.acidics.acidics_6_build(name)
    if "ACIDIC_7_" + today_corrected in name:
        editors.acidics.acidics_7_build(name)
    if "ACIDIC_8_" + today_corrected in name:
        editors.acidics.acidics_8_build(name)
    if "ACIDIC_9_" + today_corrected in name:
        editors.acidics.acidics_9_build(name)
    if "ACIDIC_10_" + today_corrected in name:
        editors.acidics.acidics_10_build(name)
    if "COMBINED_1_" + today_corrected in name:
        editors.combined.combined_1_build(name)
    if "COMBINED_2_" + today_corrected in name:
        editors.combined.combined_2_build(name)
    if "COMBINED_3_" + today_corrected in name:
        editors.combined.combined_3_build(name)
    if "COMBINED_4_" + today_corrected in name:
        editors.combined.combined_4_build(name)
    if "COMBINED_5_" + today_corrected in name:
        editors.combined.combined_5_build(name)
    if "COMBINED_6_" + today_corrected in name:
        editors.combined.combined_6_build(name)
    if "COMBINED_7_" + today_corrected in name:
        editors.combined.combined_7_build(name)
    if "COMBINED_8_" + today_corrected in name:
        editors.combined.combined_8_build(name)
    if "COMBINED_9_" + today_corrected in name:
        editors.combined.combined_9_build(name)
    if "COMBINED_10_" + today_corrected in name:
        editors.combined.combined_10_build(name)
    if "BHP_1_" + today_corrected in name:
        editors.bhp.bhp_1_build(name)
    if "BHP_2_" + today_corrected in name:
        editors.bhp.bhp_2_build(name)
    if "BHP_3_" + today_corrected in name:
        editors.bhp.bhp_3_build(name)
    if "BHP_4_" + today_corrected in name:
        editors.bhp.bhp_4_build(name)
    if "BHP_5_" + today_corrected in name:
        editors.bhp.bhp_5_build(name)
    if "BHP_6_" + today_corrected in name:
        editors.bhp.bhp_6_build(name)
    if "BHP_7_" + today_corrected in name:
        editors.bhp.bhp_7_build(name)
    if "BHP_8_" + today_corrected in name:
        editors.bhp.bhp_8_build(name)
    if "BHP_9_" + today_corrected in name:
        editors.bhp.bhp_9_build(name)
    if "BHP_10_" + today_corrected in name:
        editors.bhp.bhp_10_build(name)
    if "Functional Biomarker_1_" + today_corrected in name:
        editors.functional.functional_1_build(name)
    if "Functional Biomarker_2_" + today_corrected in name:
        editors.functional.functional_2_build(name)
    if "Functional Biomarker_3_" + today_corrected in name:
        editors.functional.functional_3_build(name)
    if "Functional Biomarker_4_" + today_corrected in name:
        editors.functional.functional_4_build(name)
    if "Functional Biomarker_5_" + today_corrected in name:
        editors.functional.functional_5_build(name)
    if "Functional Biomarker_6_" + today_corrected in name:
        editors.functional.functional_6_build(name)
    if "Functional Biomarker_7_" + today_corrected in name:
        editors.functional.functional_7_build(name)
    if "Functional Biomarker_8_" + today_corrected in name:
        editors.functional.functional_8_build(name)
    if "Functional Biomarker_9_" + today_corrected in name:
        editors.functional.functional_9_build(name)
    if "Functional Biomarker_10_" + today_corrected in name:
        editors.functional.functional_10_build(name)
    if "Functional Biomarker_1_" + today_corrected in name:
        editors.hcys.hcys_1_build(name)
    if "Functional Biomarker_2_" + today_corrected in name:
        editors.hcys.hcys_2_build(name)
    if "Functional Biomarker_3_" + today_corrected in name:
        editors.hcys.hcys_3_build(name)
    if "Functional Biomarker_4_" + today_corrected in name:
        editors.hcys.hcys_4_build(name)
    if "Functional Biomarker_5_" + today_corrected in name:
        editors.hcys.hcys_5_build(name)
    if "Functional Biomarker_6_" + today_corrected in name:
        editors.hcys.hcys_6_build(name)
    if "Functional Biomarker_7_" + today_corrected in name:
        editors.hcys.hcys_7_build(name)
    if "Functional Biomarker_8_" + today_corrected in name:
        editors.hcys.hcys_8_build(name)
    if "Functional Biomarker_9_" + today_corrected in name:
        editors.hcys.hcys_9_build(name)
    if "Functional Biomarker_10_" + today_corrected in name:
        editors.hcys.hcys_10_build(name)

find_filenames(r"L:\Worklist Editor", suffix=".csv")
updated_worklists = find_filenames(r"L:\Worklist Editor")
for name in updated_worklists:
    if today_corrected in name:
        print("The Worklist Editor ran successfully")
    else:
        os.rename("L:\Worklist Editor\\" + name, "L:\Worklist Editor\Archive\\" + name)
