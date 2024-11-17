import json
import os
from pathlib import Path


def merge_studio_folders(base_dir):
    # Create output directory
    output_dir = Path(base_dir) / "merged_studio"
    output_dir.mkdir(exist_ok=True)

    # Initialize merged graphs
    merged_graphs = {}

    # Find all module directories
    module_dirs = sorted([d for d in Path(base_dir).glob("module-*") if d.is_dir()])

    # Merge langgraph.json files
    for module_dir in module_dirs:
        langgraph_path = module_dir / "studio" / "langgraph.json"
        if langgraph_path.exists():
            with open(langgraph_path) as f:
                data = json.load(f)
                merged_graphs.update(data.get("graphs", {}))

    # Create merged langgraph.json
    merged_config = {
        "dockerfile_lines": [],
        "graphs": merged_graphs,
        "env": "./.env",
        "python_version": "3.11",
        "dependencies": ["."],
    }

    # Write merged langgraph.json
    with open(output_dir / "langgraph.json", "w") as f:
        json.dump(merged_config, f, indent=2)

    # Copy all Python files
    for module_dir in module_dirs:
        studio_dir = module_dir / "studio"
        if studio_dir.exists():
            for py_file in studio_dir.glob("*.py"):
                dest_file = output_dir / py_file.name
                dest_file.write_bytes(py_file.read_bytes())

    # Merge requirements.txt files
    requirements = set()
    for module_dir in module_dirs:
        req_file = module_dir / "studio" / "requirements.txt"
        if req_file.exists():
            requirements.update(req_file.read_text().splitlines())

    # Write merged requirements.txt
    with open(output_dir / "requirements.txt", "w") as f:
        f.write("\n".join(sorted(filter(None, requirements))) + "\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python merge_studio.py <directory_path>")
        sys.exit(1)
    merge_studio_folders(sys.argv[1])
