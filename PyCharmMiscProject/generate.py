"""
Smart AI Toothbrush Dataset Generator
Generates synthetic data for oral lesion monitoring analysis
Saves as SINGLE merged CSV file for easy use in PyCharm
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

print("="*80)
print("SMART AI TOOTHBRUSH - DATASET GENERATOR")
print("="*80)

# ============================================================================
# DATASET 1: Patient Demographics and Risk Factors
# ============================================================================
print("\n[1/3] Generating Patient Demographics...")
n_patients = 500

patient_data = {
    'patient_id': [f'P{str(i).zfill(4)}' for i in range(1, n_patients + 1)],
    'age': np.random.randint(18, 80, n_patients),
    'gender': np.random.choice(['Male', 'Female'], n_patients, p=[0.6, 0.4]),
    'location': np.random.choice(['Sabah', 'Sarawak', 'Other'], n_patients, p=[0.45, 0.45, 0.1]),
    'ethnicity': np.random.choice(['Indigenous', 'Chinese', 'Malay', 'Other'], n_patients, p=[0.5, 0.2, 0.2, 0.1]),
    'betel_chewing': np.random.choice([0, 1], n_patients, p=[0.4, 0.6]),
    'tobacco_use': np.random.choice([0, 1], n_patients, p=[0.5, 0.5]),
    'alcohol_consumption': np.random.choice(['None', 'Occasional', 'Regular', 'Heavy'], n_patients, p=[0.3, 0.3, 0.25, 0.15]),
    'family_history_cancer': np.random.choice([0, 1], n_patients, p=[0.75, 0.25]),
    'oral_hygiene_score': np.random.randint(1, 11, n_patients),
    'rural_area': np.random.choice([0, 1], n_patients, p=[0.25, 0.75]),
}

df_patients = pd.DataFrame(patient_data)
print(f"✓ Created patient demographics: {len(df_patients)} records")

# ============================================================================
# DATASET 2: Lesion Detection and Monitoring Data
# ============================================================================
print("\n[2/3] Generating Lesion Detection Data...")
n_lesions = 800

lesion_data = {
    'lesion_id': [f'L{str(i).zfill(4)}' for i in range(1, n_lesions + 1)],
    'patient_id': np.random.choice(df_patients['patient_id'], n_lesions),
    'detection_date': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 300)) for _ in range(n_lesions)],
    'location_oral_cavity': np.random.choice(['Tongue', 'Buccal Mucosa', 'Floor of Mouth', 'Palate', 'Gingiva', 'Lip'],
                                             n_lesions, p=[0.3, 0.25, 0.15, 0.1, 0.12, 0.08]),
    'initial_size_mm': np.random.uniform(2, 20, n_lesions),
    'color': np.random.choice(['White', 'Red', 'Mixed', 'Normal'], n_lesions, p=[0.4, 0.3, 0.2, 0.1]),
    'texture': np.random.choice(['Smooth', 'Rough', 'Ulcerated', 'Raised'], n_lesions, p=[0.3, 0.3, 0.25, 0.15]),
    'pain_level': np.random.randint(0, 11, n_lesions),
    'ai_confidence_score': np.random.uniform(0.4, 0.99, n_lesions),
    'lesion_type_detected': np.random.choice(['Benign', 'Suspicious', 'High-Risk'], n_lesions, p=[0.6, 0.25, 0.15]),
}

df_lesions = pd.DataFrame(lesion_data)
print(f"✓ Created lesion detection: {len(df_lesions)} records")

# ============================================================================
# DATASET 3: Follow-up and Growth Monitoring (TARGET VARIABLE)
# ============================================================================
print("\n[3/3] Generating Follow-up Monitoring Data...")
n_followups = 2000

followup_data = {
    'followup_id': [f'F{str(i).zfill(5)}' for i in range(1, n_followups + 1)],
    'lesion_id': np.random.choice(df_lesions['lesion_id'], n_followups),
    'followup_date': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(n_followups)],
    'size_mm': np.random.uniform(1, 25, n_followups),
    'growth_rate_mm_per_month': np.random.uniform(-2, 5, n_followups),  # TARGET VARIABLE
    'color_change': np.random.choice([0, 1], n_followups, p=[0.7, 0.3]),
    'texture_change': np.random.choice([0, 1], n_followups, p=[0.75, 0.25]),
    'pain_change': np.random.randint(-3, 4, n_followups),
    'clinician_reviewed': np.random.choice([0, 1], n_followups, p=[0.4, 0.6]),
    'biopsy_recommended': np.random.choice([0, 1], n_followups, p=[0.85, 0.15]),
}

df_followups = pd.DataFrame(followup_data)
print(f"✓ Created follow-up monitoring: {len(df_followups)} records")

# ============================================================================
# MERGE ALL DATASETS INTO SINGLE CSV
# ============================================================================
print("\n" + "="*80)
print("MERGING DATASETS...")
print("="*80)

# Step 1: Merge follow-ups with lesions
print("\n[Merge 1/2] Merging follow-ups with lesion data...")
df_merged = df_followups.merge(df_lesions, on='lesion_id', how='left')
print(f"✓ After merge: {len(df_merged)} records")

# Step 2: Merge with patient demographics
print("\n[Merge 2/2] Merging with patient demographics...")
df_merged = df_merged.merge(df_patients, on='patient_id', how='left')
print(f"✓ After merge: {len(df_merged)} records")

# Check for missing values
print("\n📊 Checking data quality...")
missing_count = df_merged.isnull().sum().sum()
print(f"   Missing values: {missing_count}")

if missing_count > 0:
    print("\n⚠️  Removing rows with missing values...")
    df_merged = df_merged.dropna()
    print(f"✓ Clean dataset: {len(df_merged)} records")

# ============================================================================
# SAVE TO SINGLE CSV FILE
# ============================================================================
output_filename = '../../../Users/Asus/PyCharmMiscProject/smart_toothbrush_data.csv'
df_merged.to_csv(output_filename, index=False)

print("\n" + "="*80)
print("✅ DATASET GENERATION COMPLETE!")
print("="*80)

print(f"\n📁 File saved: {output_filename}")
print(f"📊 Total records: {len(df_merged):,}")
print(f"📋 Total columns: {len(df_merged.columns)}")

print("\n📋 Column Summary:")
print(f"   • Patient Info    : patient_id, age, gender, location, ethnicity")
print(f"   • Risk Factors    : betel_chewing, tobacco_use, alcohol_consumption")
print(f"   • Lesion Info     : lesion_id, location_oral_cavity, initial_size_mm, color, texture")
print(f"   • Follow-up Data  : followup_id, followup_date, size_mm, color_change, texture_change")
print(f"   • TARGET VARIABLE : growth_rate_mm_per_month ⭐")

print("\n🎯 Key Statistics:")
print(f"   • Betel chewing prevalence : {df_merged['betel_chewing'].mean()*100:.1f}%")
print(f"   • Tobacco use prevalence   : {df_merged['tobacco_use'].mean()*100:.1f}%")
print(f"   • Average age              : {df_merged['age'].mean():.1f} years")
print(f"   • Average growth rate      : {df_merged['growth_rate_mm_per_month'].mean():.2f} mm/month")
print(f"   • Rural area patients      : {df_merged['rural_area'].mean()*100:.1f}%")

print("\n💡 Next Steps:")
print("   1. Load data: df = pd.read_csv('smart_toothbrush_data.csv')")
print("   2. Run regression analysis on 'growth_rate_mm_per_month'")
print("   3. Run clustering on patient risk factors")

print("\n" + "="*80)

# Display first few rows
print("\n📊 Sample Data (first 5 rows):")
print(df_merged.head())

print("\n📋 All Columns:")
print(df_merged.columns.tolist())