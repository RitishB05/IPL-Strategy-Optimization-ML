import os
import shutil

# The target folder
target = "assets"
if not os.path.exists(target):
    os.makedirs(target)

# Mapping the specific IDs from your screenshot to descriptive names
mapping = {
    "671a8e15-3ea6-4654-9cdc-c82ac771e503.png": "roc_curves_comparison.png",
    "949a5f14-3642-4efb-ae20-63383b9f152a.png": "correlation_matrix_blue_red.png",
    "b5dbfccd-12a0-4d11-9a2b-5e679a39dff4.png": "correlation_matrix_magma.png",
    "3ed9af78-3ba3-4ad1-ba39-bcb90314d052.png": "eda_histograms_grid.png",
    "c6ecfdc8-e546-4474-b727-f99c937c1f63.png": "metrics_logreg_randomforest.png",
    "26b46e29-63b0-469d-8ef8-2858bfdc0187.png": "target_distribution_blue.png",
    "23d9c6cd-8b6a-4b04-b462-db5f2b492d37.png": "eda_histograms_simple.png",
    "93071436-5a04-433d-8cd5-66004d39190a.png": "target_distribution_green.png",
    "8623d747-a675-45d8-889e-2b8fa4261e6e.png": "model_accuracy_table.png",
    "4ed94d46-5c9c-44f7-a788-4791c98bdd6e.png": "metrics_xgb_svc_gb.png",
    "53a8bc3c-791e-4bd8-9e09-79b383242e08.png": "cm_random_forest.png",
    "b8eb780c-4ce0-4191-bd45-33ed595015ed.png": "cm_gradient_boosting.png",
    "b112b21c-51dd-45c3-bb36-d3295814f72b.png": "cm_logistic_regression.png",
    "22d2ab34-254c-4c1c-b6cb-fc44d3eab12b.png": "model_accuracy_bar_chart.png",
    "3df7aac2-bf55-43bf-a5bd-7ca56c41cc5c.png": "optimal_xi_output.png",
    "21192a80-2900-4a00-aad7-c9af7725269f.png": "cm_xgboost.png",
    "519be50f-fa69-4ad0-a9e6-9f00f3518d56.png": "cm_svc.png",
    "e71ee3b1-df04-46db-80ac-e6e26c0dd021.png": "raw_data_snapshot.png",
    "1446d9cc-52d5-4a59-a7c1-af237690a483.png": "aggregated_player_data.png"
}

def clean_and_organize():
    count = 0
    for old_name, new_name in mapping.items():
        if os.path.exists(old_name):
            try:
                shutil.move(old_name, os.path.join(target, new_name))
                print(f"✅ Success: {old_name} moved to assets/{new_name}")
                count += 1
            except Exception as e:
                print(f"❌ Error moving {old_name}: {e}")
    print(f"\nDone! {count} images organized into the assets folder.")

if __name__ == "__main__":
    clean_and_organize()