#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py [ingest|compute|report|app]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "ingest":
        print(">> ETL: loading CSV from data/input and saving to SQLite (data/warehouse/family_office.db)")
    elif cmd == "compute":
        print(">> COMPUTE: calculating NAV, allocations, performance, and creating views")
    elif cmd == "report":
        print(">> REPORT: generating reports/FamilyOffice_Report.xlsx")
    elif cmd == "app":
        print(">> APP: launching Streamlit dashboard (app/streamlit_app.py)")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
