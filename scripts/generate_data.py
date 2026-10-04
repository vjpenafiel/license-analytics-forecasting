'''
This code is AI-generated and has not been manually reviewed to avoid bias in training the models.
It generates synthetic raw data and metadata for the Metro-Luzon Engineering License Analytics & Forecasting project.
Furthermore, it creates realistic user, product, feature, and license pool dimensions, as well as a large volume of license events with controlled anomalies and structural data quality issues.
'''

import os
import random
import uuid
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# GLOBAL CONFIGURATION
SEED = 42
N_USERS = 2_000
N_EVENTS = 1_000_000
CHUNK_SIZE = 100_000
START_DATE = "2026-01-01"
END_DATE = "2026-12-31"

random.seed(SEED)
np.random.seed(SEED)

# Directories
RAW_DIR = "/Users/victorpenafiel/Downloads/data/raw"
META_DIR = "/Users/victorpenafiel/Downloads/data/metadata"

# Hardcoded Realistic Product & Feature Catalog for MLEIC
REAL_PRODUCT_CATALOG = [
    {
        "product_id": "P001", "product_name": "AutoCAD", "vendor": "Autodesk", "version": "2026",
        "capacity": 200, "features": [
            ("F0101", "3D Modeling", "Core"), ("F0102", "2D Drafting", "Core"),
            ("F0103", "AutoLISP Scripting", "Automation"), ("F0104", "PDF/DWG Export", "Export")
        ]
    },
    {
        "product_id": "P002", "product_name": "Revit Architecture", "vendor": "Autodesk", "version": "2026",
        "capacity": 150, "features": [
            ("F0201", "BIM Modeling", "Core"), ("F0202", "MEP Analysis", "Analytics"),
            ("F0203", "Cloud Rendering", "Rendering"), ("F0204", "Cost Estimation Link", "Analytics")
        ]
    },
    {
        "product_id": "P003", "product_name": "Civil 3D", "vendor": "Autodesk", "version": "2025",
        "capacity": 100, "features": [
            ("F0301", "Pipe Networks", "Simulation"), ("F0302", "Corridor Modeling", "Core"),
            ("F0303", "Grading Optimization", "Optimization")
        ]
    },
    {
        "product_id": "P004", "product_name": "STAAD.Pro", "vendor": "Bentley Systems", "version": "V22",
        "capacity": 75, "features": [
            ("F0401", "Structural Steel Design", "Core"), ("F0402", "Concrete Design", "Core"),
            ("F0403", "Dynamic Seismic Analysis", "Simulation"), ("F0404", "Foundation Advanced", "Analytics")
        ]
    },
    {
        "product_id": "P005", "product_name": "MicroStation", "vendor": "Bentley Systems", "version": "CONNECT",
        "capacity": 50, "features": [
            ("F0501", "DGN CAD Drafting", "Core"), ("F0502", "Point Cloud Ingestion", "Visualization")
        ]
    },
    {
        "product_id": "P006", "product_name": "OpenRoads Designer", "vendor": "Bentley Systems", "version": "V10",
        "capacity": 40, "features": [
            ("F0601", "Terrain Modeling", "Core"), ("F0602", "Drainage Design", "Simulation")
        ]
    },
    {
        "product_id": "P007", "product_name": "Ansys Mechanical", "vendor": "Ansys", "version": "2025 R2",
        "capacity": 25, "features": [
            ("F0701", "FEA Stress Analysis", "Simulation"), ("F0702", "Thermal Dynamics", "Simulation"),
            ("F0703", "Fatigue & Fracture Analysis", "Analytics")
        ]
    },
    {
        "product_id": "P008", "product_name": "Ansys Fluent", "vendor": "Ansys", "version": "2025 R2",
        "capacity": 15, "features": [
            ("F0801", "CFD Wind Analysis", "Simulation"), ("F0802", "Multiphase Flow", "Simulation")
        ]
    },
    {
        "product_id": "P009", "product_name": "ArcGIS Pro", "vendor": "Esri", "version": "3.3",
        "capacity": 100, "features": [
            ("F0901", "Spatial Analyst", "Analytics"), ("F0902", "3D Analyst", "Visualization"),
            ("F0903", "Geocoding Engine", "Database"), ("F0904", "Drone2Map Processing", "Export")
        ]
    },
    {
        "product_id": "P010", "product_name": "SolidWorks Premium", "vendor": "Dassault Systèmes", "version": "2026",
        "capacity": 80, "features": [
            ("F1001", "3D Solid Modeling", "Core"), ("F1002", "Motion Simulation", "Simulation"),
            ("F1003", "Plastics Injection Mold", "Analytics")
        ]
    },
    {
        "product_id": "P011", "product_name": "CATIA V6", "vendor": "Dassault Systèmes", "version": "3DEXPERIENCE",
        "capacity": 20, "features": [
            ("F1101", "Surface Design", "Core"), ("F1102", "Aerodynamics Modeling", "Simulation")
        ]
    },
    {
        "product_id": "P012", "product_name": "MATLAB Enterprise", "vendor": "MathWorks", "version": "R2025b",
        "capacity": 120, "features": [
            ("F1201", "Signal Processing", "Analytics"), ("F1202", "Simulink Engine", "Simulation"),
            ("F1203", "Deep Learning Toolbox", "Analytics")
        ]
    },
    {
        "product_id": "P013", "product_name": "Tekla Structures", "vendor": "Trimble", "version": "2025",
        "capacity": 60, "features": [
            ("F1301", "Structural Steel Detailing", "Core"), ("F1302", "Rebar Detailing", "Core")
        ]
    },
    {
        "product_id": "P014", "product_name": "SketchUp Pro", "vendor": "Trimble", "version": "2025",
        "capacity": 150, "features": [
            ("F1401", "3D Conceptual Design", "Core"), ("F1402", "Layout Architectural", "Export")
        ]
    },
    {
        "product_id": "P015", "product_name": "Siemens NX", "vendor": "Siemens", "version": "2306",
        "capacity": 30, "features": [
            ("F1501", "Advanced CAD Design", "Core"), ("F1502", "Tooling & Die Design", "Core")
        ]
    }
]

def setup_directories():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(META_DIR, exist_ok=True)

def generate_dimensions():
    print("Generating catalog dimension tables for Metro-Luzon Engineering...")
    
    # 1. Users
    locations = ["BGC", "MNL", "MAK", "QC", "CEB", "DAV", "bgc", " mnl", "BGC ", None]
    roles = [
        "BIM Specialist", "Civil Engineer", "Structural Analyst", "CAD Technician",
        "GIS Analyst", "Project Manager", "Principal Architect", "CFD Specialist",
        "bim specialist", "CIVIL ENGINEER", " CAD Technician "
    ]
    
    users = []
    for i in range(1, N_USERS + 1):
        users.append({
            "user_id": f"U{i:06d}",
            "job_role": random.choice(roles),
            "location": random.choice(locations),
            "created_at": (pd.Timestamp(START_DATE) - pd.Timedelta(days=random.randint(30, 1000))).date()
        })
    users_df = pd.DataFrame(users)
    users_df.to_csv(f"{RAW_DIR}/users.csv", index=False)

    # 2. Products, Features, and Pools
    products, features, pools = [], [], []
    pool_counter = 1
    
    for prod in REAL_PRODUCT_CATALOG:
        products.append({
            "product_id": prod["product_id"],
            "product_name": prod["product_name"],
            "vendor": prod["vendor"],
            "version": prod["version"]
        })
        
        pool_id = f"LP{pool_counter:03d}"
        pools.append({
            "license_pool_id": pool_id,
            "product_id": prod["product_id"],
            "capacity": prod["capacity"],
            "valid_from": "2025-01-01",
            "valid_until": "2027-12-31"
        })
        pool_counter += 1
        
        for f_id, f_name, f_cat in prod["features"]:
            features.append({
                "feature_id": f_id,
                "product_id": prod["product_id"],
                "feature_name": f_name,
                "feature_category": f_cat,
                "version": f"v{prod['version']}"
            })
            
    pd.DataFrame(products).to_csv(f"{RAW_DIR}/software_products.csv", index=False)
    features_df = pd.DataFrame(features)
    features_df.to_csv(f"{RAW_DIR}/software_features.csv", index=False)
    pools_df = pd.DataFrame(pools)
    pools_df.to_csv(f"{RAW_DIR}/license_pools.csv", index=False)
    
    return users_df, pd.DataFrame(products), features_df, pools_df

def generate_events(users_df, features_df, pools_df):
    print("Generating license_events with controlled messiness & anomalies...")
    
    feature_to_product = dict(zip(features_df['feature_id'], features_df['product_id']))
    product_to_pool = dict(zip(pools_df['product_id'], pools_df['license_pool_id']))
    
    users_list = users_df['user_id'].tolist()
    feature_list = features_df['feature_id'].tolist()
    
    start_ts = pd.Timestamp(START_DATE).timestamp()
    end_ts = pd.Timestamp(END_DATE).timestamp()
    
    events_file = f"{RAW_DIR}/license_events.csv"
    anomaly_file = f"{META_DIR}/anomaly_ground_truth.csv"
    
    pd.DataFrame(columns=[
        "event_id", "event_timestamp", "user_id", "product_id", 
        "feature_id", "license_pool_id", "event_type", "session_id", "ingested_at"
    ]).to_csv(events_file, index=False)
    
    pd.DataFrame(columns=["session_id", "event_id", "anomaly_reason"]).to_csv(anomaly_file, index=False)
    
    total_sessions = N_EVENTS // 2
    sessions_generated = 0
    event_id_counter = 1
    
    while sessions_generated < total_sessions:
        chunk_sessions = min(CHUNK_SIZE // 2, total_sessions - sessions_generated)
        events_chunk = []
        anomalies_chunk = []
        
        for _ in range(chunk_sessions):
            session_id = f"S_{uuid.uuid4().hex[:10]}"
            user = random.choice(users_list)
            feature = random.choice(feature_list)
            product = feature_to_product[feature]
            pool = product_to_pool[product]
            
            # Baseline business hours in Manila (08:00 to 17:00 PHT)
            day_offset = random.uniform(0, end_ts - start_ts)
            base_time = pd.Timestamp(start_ts + day_offset, unit='s')
            base_time = base_time.replace(hour=int(np.clip(np.random.normal(12, 3), 8, 17)))
            
            duration_minutes = int(np.random.exponential(50) + 10)
            end_time = base_time + pd.Timedelta(minutes=duration_minutes)
            
            # Inject Anomalies (~0.25% ground truth)
            if random.random() < 0.0025:
                anomaly_type = random.choice(["48H_LONG_SESSION", "MIDNIGHT_BURST"])
                if anomaly_type == "48H_LONG_SESSION":
                    end_time = base_time + pd.Timedelta(hours=48)
                elif anomaly_type == "MIDNIGHT_BURST":
                    base_time = base_time.replace(hour=2)
                    end_time = base_time + pd.Timedelta(minutes=45)
                
                anomalies_chunk.append({
                    "session_id": session_id,
                    "event_id": event_id_counter,
                    "anomaly_reason": anomaly_type
                })

            ingested = datetime.now()
            
            # CHECKOUT
            events_chunk.append({
                "event_id": event_id_counter,
                "event_timestamp": base_time,
                "user_id": user,
                "product_id": product,
                "feature_id": feature,
                "license_pool_id": pool,
                "event_type": "CHECKOUT",
                "session_id": session_id,
                "ingested_at": ingested
            })
            event_id_counter += 1
            
            # CHECKIN
            events_chunk.append({
                "event_id": event_id_counter,
                "event_timestamp": end_time,
                "user_id": user,
                "product_id": product,
                "feature_id": feature,
                "license_pool_id": pool,
                "event_type": "CHECKIN",
                "session_id": session_id,
                "ingested_at": ingested
            })
            event_id_counter += 1

        df_chunk = pd.DataFrame(events_chunk)
        
        # Inject Structural Data Quality Errors (< 1% Total Noise)
        # 1. Orphan Checkouts / Checkins (Drop 0.3% of individual events)
        orphan_mask = np.random.rand(len(df_chunk)) < 0.003
        df_chunk = df_chunk[~orphan_mask]
        
        # 2. Duplicate Event Rows (Duplicate 0.2% of events)
        dup_mask = np.random.rand(len(df_chunk)) < 0.002
        dups = df_chunk[dup_mask].copy()
        if not dups.empty:
            dups["event_id"] = dups["event_id"] + 90_000_000  # distinct duplicated IDs
            df_chunk = pd.concat([df_chunk, dups], ignore_index=True)
            
        # 3. Invalid Foreign Keys (Corrupt 0.1% of FKs)
        fk_mask = np.random.rand(len(df_chunk)) < 0.001
        df_chunk.loc[fk_mask, "user_id"] = "U999999_INVALID"
        
        # Sort chronologically
        df_chunk = df_chunk.sort_values("event_timestamp")
        
        # Append to CSV
        df_chunk.to_csv(events_file, mode='a', header=False, index=False)
        if anomalies_chunk:
            pd.DataFrame(anomalies_chunk).to_csv(anomaly_file, mode='a', header=False, index=False)
            
        sessions_generated += chunk_sessions
        print(f"Generated {sessions_generated * 2} / {N_EVENTS} raw events...")

    print("\nData generation complete.")

if __name__ == "__main__":
    setup_directories()
    u, pr, f, lp = generate_dimensions()
    generate_events(u, f, lp)