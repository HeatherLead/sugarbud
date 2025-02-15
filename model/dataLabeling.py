import pandas as pd

file_path = "model/cbcInformation.xlsx"
df = pd.read_excel(file_path)

WBC_col = "WBC"
RBC_col = "RBC"
Hemoglobin_col = "HGB"
Platelets_col = "PLT"
MCV_col = "MCV"
RDW_col = "RDWCV"
Hematocrit_col = "HCT"
NEUT_col = "NEUTp" 
LYMP_col = "LYMp"

def classify_disease(row):
    diseases = []

    if row[Hemoglobin_col] < 12 and row[Hematocrit_col] < 36 and row[RBC_col] < 4.2:
        diseases.append("Anemia")

    if row[WBC_col] > 11 and row[NEUT_col] > 70 and row[LYMP_col] < 20:
        diseases.append("Leukemia/Infection")

    if row[Platelets_col] < 150 and row[Hematocrit_col] < 36:
        diseases.append("Thrombocytopenia (Low Platelets)")

    if row[RBC_col] > 6 and row[Hemoglobin_col] > 16.5 and row[Hematocrit_col] > 50:
        diseases.append("Polycythemia (High RBC)")

    if row[MCV_col] < 80 and row[RBC_col] >= 4:
        diseases.append("Thalassemia")

    if row[WBC_col] > 11 and row[Platelets_col] > 450:
        diseases.append("Possible Infection")

    if "PT" in row and "PTT" in row:
        if row["PT"] > 14 or row["PTT"] > 35:
            diseases.append("Clotting Disorder")

    return ", ".join(diseases) if diseases else "Normal"

df["Possible Disease"] = df.apply(classify_disease, axis=1)

output_file = "model/labelDataset.xlsx"
df.to_excel(output_file, index=False)

print(f"Processed data saved to {output_file}")
