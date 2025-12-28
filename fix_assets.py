import os
import shutil

# Mapping based on your screenshot
mapping = {
    "download (2).png": "correlation_heatmap.png",
    "download (6).png": "roc_curve.png",
    "download (7).png": "cm_xgboost.png",
    "download (8).png": "cm_svc.png",
    "download (9).png": "cm_gradient_boosting.png",
    "download (10).png": "cm_random_forest.png",
    "download (11).png": "cm_logistic_regression.png",
    "download (4).png": "target_distribution.png",
    "download (1).png": "feature_distributions.png",
    "download (12).png": "selection_ratio.png",
    "download.png": "eda_plot_generic.png"
}

target_folder = "assets"
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

def rename_and_move():
    # Process the specific mapped files
    for old_name, new_name in mapping.items():
        if os.path.exists(old_name):
            shutil.move(old_name, os.path.join(target_folder, new_name))
            print(f"✅ Success: {old_name} -> {target_folder}/{new_name}")
    
    # Process the Screenshots (which have long timestamps)
    screenshots = [f for f in os.listdir('.') if f.startswith("Screenshot") and f.endswith(".png")]
    for i, snip in enumerate(screenshots):
        # We'll name these based on their order in the folder for now
        new_snip_name = f"result_table_{i+1}.png"
        shutil.move(snip, os.path.join(target_folder, new_snip_name))
        print(f"✅ Success: {snip} -> {target_folder}/{new_snip_name}")

if __name__ == "__main__":
    rename_and_move()
    print("\nAll images are now organized in /assets with descriptive names!")