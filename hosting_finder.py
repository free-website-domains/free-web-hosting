#!/usr/bin/env python3
"""
Free Web Hosting & Free Domains CLI Finder (free-website-domains/free-web-hosting)
Zero-dependency CLI to search, filter, and export 125+ free web hosting & domain providers,
plus a helper to update referral/partner URLs across all documentation files.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

ROOT_DIR = Path(__file__).resolve().parent
PROVIDERS_PATH = ROOT_DIR / "providers.json"
SYNC_FILES = [
    ROOT_DIR / "README.md",
    ROOT_DIR / "llms.txt",
    ROOT_DIR / "docs" / "index.html",
    ROOT_DIR / "docs" / "llms.txt",
]


def load_data() -> Dict[str, Any]:
    with PROVIDERS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def filter_providers(
    providers: List[Dict[str, Any]],
    category: str | None = None,
    stack: str | None = None,
    search: str | None = None,
) -> List[Dict[str, Any]]:
    results = providers
    if category and category != "all":
        results = [p for p in results if p.get("category", "").lower() == category.lower()]
    if stack:
        stack_q = stack.lower()
        results = [
            p for p in results if any(stack_q in s.lower() for s in p.get("stack", []))
        ]
    if search:
        q = search.lower()
        results = [
            p
            for p in results
            if q in p.get("name", "").lower()
            or q in p.get("free_offer", "").lower()
            or any(q in s.lower() for s in p.get("stack", []))
        ]
    return results


def update_affiliate_links(pairs: List[str]) -> None:
    data = load_data()
    affiliates: Dict[str, str] = data.get("affiliates", {})
    for pair in pairs:
        if "=" not in pair:
            raise ValueError(f"Expected key=url format, got: {pair}")
        key, new_url = pair.split("=", 1)
        key = key.strip().lower()
        new_url = new_url.strip()
        if key not in affiliates:
            raise ValueError(
                f"Unknown partner '{key}'. Valid keys: {', '.join(affiliates.keys())}"
            )
        old_url = affiliates[key]
        affiliates[key] = new_url
        for p in data.get("providers", []):
            if p.get("name", "").lower() == key:
                p["url"] = new_url
        for file_path in SYNC_FILES:
            if file_path.exists() and old_url and old_url != new_url:
                text = file_path.read_text(encoding="utf-8")
                file_path.write_text(text.replace(old_url, new_url), encoding="utf-8")
        print(f"[OK] Updated {key}: {old_url} -> {new_url}")

    with PROVIDERS_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def print_table(providers: List[Dict[str, Any]]) -> None:
    if not providers:
        print("No matching providers found.")
        return
    header = f"{'Provider':<24} | {'Category':<8} | {'Storage / Specs':<26} | {'Free Offer / Tier':<52} | {'URL'}"
    print(header)
    print("-" * len(header))
    for p in providers:
        print(
            f"{p['name']:<24} | {p['category']:<8} | {p['storage'][:26]:<26} | {p['free_offer'][:52]:<52} | {p['url']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search and filter Free Web Hosting & Free Domain providers."
    )
    parser.add_argument(
        "-c",
        "--category",
        choices=["all", "deals", "static", "php", "cloud", "domains"],
        default="all",
        help="Filter by category (deals, static, php, cloud, domains)",
    )
    parser.add_argument(
        "-s",
        "--stack",
        help="Filter by technology stack (e.g. wordpress, php, docker, react, domain)",
    )
    parser.add_argument("-q", "--search", help="Keyword search across names and offers")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument(
        "--set-affiliate",
        nargs="+",
        metavar="PARTNER=URL",
        help="Update affiliate link(s) across README.md, docs/index.html, llms.txt & providers.json (e.g. hostinger=https://...)",
    )
    args = parser.parse_args()

    if args.set_affiliate:
        update_affiliate_links(args.set_affiliate)
        return

    data = load_data()
    matched = filter_providers(
        data.get("providers", []),
        category=args.category,
        stack=args.stack,
        search=args.search,
    )
    if args.json:
        print(json.dumps(matched, indent=2, ensure_ascii=False))
    else:
        print_table(matched)


if __name__ == "__main__":
    main()
