#!/usr/bin/env python3

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, check=True, text=True, capture_output=True)


def clone_repo(repo_url: str, target_dir: Path) -> Path:
    repo_dir = target_dir / "repo"
    run(["git", "clone", "--depth", "1", repo_url, str(repo_dir)])
    return repo_dir


def detect_stack(repo_dir: Path):
    findings = {
        "stack": "unknown",
        "framework": None,
        "database": None,
        "signals": [],
    }

    package_json = repo_dir / "package.json"
    requirements_txt = repo_dir / "requirements.txt"
    pyproject_toml = repo_dir / "pyproject.toml"
    go_mod = repo_dir / "go.mod"
    composer_json = repo_dir / "composer.json"
    dockerfile = repo_dir / "Dockerfile"

    if package_json.exists():
        findings["stack"] = "nodejs"
        findings["signals"].append("package.json")
        content = package_json.read_text(encoding="utf-8", errors="ignore").lower()
        if "express" in content:
          findings["framework"] = "express"
        if "next" in content:
          findings["framework"] = "next.js"
        if "postgres" in content or "pg" in content or "prisma" in content:
          findings["database"] = "postgresql"

    elif requirements_txt.exists() or pyproject_toml.exists():
        findings["stack"] = "python"
        findings["signals"].append("requirements.txt/pyproject.toml")
        content = ""
        if requirements_txt.exists():
            content += requirements_txt.read_text(encoding="utf-8", errors="ignore").lower()
        if pyproject_toml.exists():
            content += pyproject_toml.read_text(encoding="utf-8", errors="ignore").lower()
        if "django" in content:
            findings["framework"] = "django"
        if "psycopg" in content or "postgres" in content:
            findings["database"] = "postgresql"

    elif go_mod.exists():
        findings["stack"] = "go"
        findings["signals"].append("go.mod")
        content = go_mod.read_text(encoding="utf-8", errors="ignore").lower()
        if "gin" in content:
            findings["framework"] = "gin"
        if "gorm" in content or "postgres" in content:
            findings["database"] = "postgresql"

    elif composer_json.exists():
        findings["stack"] = "php"
        findings["signals"].append("composer.json")
        content = composer_json.read_text(encoding="utf-8", errors="ignore").lower()
        if "laravel" in content:
            findings["framework"] = "laravel"
        if "symfony" in content:
            findings["framework"] = "symfony"
        if "postgres" in content or "pgsql" in content:
            findings["database"] = "postgresql"

    if dockerfile.exists():
        findings["signals"].append("Dockerfile")

    return findings


def list_key_files(repo_dir: Path):
    interesting = [
        "package.json",
        "package-lock.json",
        "requirements.txt",
        "pyproject.toml",
        "go.mod",
        "composer.json",
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        ".env.example",
        "README.md",
    ]
    found = []
    for relative in interesting:
        path = repo_dir / relative
        if path.exists():
            found.append(relative)
    return found


def build_prompt(repo_url: str, findings: dict, key_files: list[str]):
    return f"""Tu es un assistant DevOps pour Azure.

Analyse ce depot Git : {repo_url}

Contexte detecte automatiquement :
- stack probable : {findings['stack']}
- framework probable : {findings['framework']}
- base de donnees probable : {findings['database']}
- fichiers cles detectes : {", ".join(key_files) if key_files else "aucun"}

Je veux que tu repondes en JSON strict avec les champs suivants :
- stack
- framework
- database
- runtime
- package_manager
- build_command
- start_command
- dockerfile_strategy
- kubernetes_objects
- environment_variables
- observability_strategy

Reponds uniquement en JSON.
"""


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/analyze_repo.py <git_repo_url>", file=sys.stderr)
        sys.exit(1)

    repo_url = sys.argv[1]

    with tempfile.TemporaryDirectory() as tmp:
        base_dir = Path(tmp)
        repo_dir = clone_repo(repo_url, base_dir)
        findings = detect_stack(repo_dir)
        key_files = list_key_files(repo_dir)
        prompt = build_prompt(repo_url, findings, key_files)

        report = {
            "repo_url": repo_url,
            "stack_analysis": findings,
            "key_files": key_files,
            "prompt": prompt,
        }

        print(json.dumps(report, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
