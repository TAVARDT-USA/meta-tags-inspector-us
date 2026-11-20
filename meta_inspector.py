#!/usr/bin/env python3
import sys
import re
import json
import ssl
import argparse
import urllib.request
import urllib.error

def inspect_metadata(target_url, timeout=8):
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "https://" + target_url
    target_url = target_url.rstrip("/")

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    results = {
        "target": target_url,
        "score": 100,
        "status": "PASS",
        "tags": {},
        "issues": [],
        "recommendations": []
    }

    req = urllib.request.Request(target_url, headers={"User-Agent": "Mozilla/5.0 (TAVARDT-Meta-Auditor/1.0)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="ignore")

        # 1. Title tag
        t_match = re.search(r'<title[^>]*>(.*?)</title>', body, re.I | re.DOTALL)
        if t_match:
            title_text = t_match.group(1).strip()
            results["tags"]["title"] = {"text": title_text, "length": len(title_text)}
            if len(title_text) < 20:
                results["score"] -= 10
                results["issues"].append(f"Title tag is short ({len(title_text)} chars). Recommended: 30-60 characters.")
                results["recommendations"].append("Expand title tag to 30-60 characters to maximize SERP visibility.")
            elif len(title_text) > 70:
                results["score"] -= 10
                results["issues"].append(f"Title tag is long ({len(title_text)} chars) and risk SERP truncation.")
                results["recommendations"].append("Keep title tag under 60 characters to prevent search snippet truncation.")
        else:
            results["score"] -= 25
            results["tags"]["title"] = None
            results["issues"].append("Missing <title> tag in HTML document.")
            results["recommendations"].append("Deploy a descriptive, unique <title> tag.")

        # 2. Meta description
        d_match = re.search(r'<meta[^>]+(?:name=["']description["'][^>]+content=["']([^"']*)["']|content=["']([^"']*)["'][^>]+name=["']description["'])', body, re.I)
        if d_match:
            desc_text = (d_match.group(1) or d_match.group(2) or "").strip()
            results["tags"]["description"] = {"text": desc_text, "length": len(desc_text)}
            if len(desc_text) < 70:
                results["score"] -= 10
                results["issues"].append(f"Meta description is short ({len(desc_text)} chars). Recommended: 120-160 characters.")
                results["recommendations"].append("Expand meta description to 120-160 characters.")
            elif len(desc_text) > 175:
                results["score"] -= 10
                results["issues"].append(f"Meta description is long ({len(desc_text)} chars) and may be truncated.")
                results["recommendations"].append("Shorten meta description to 120-160 characters.")
        else:
            results["score"] -= 20
            results["tags"]["description"] = None
            results["issues"].append("Missing <meta name='description'> tag.")
            results["recommendations"].append("Add a compelling meta description tag (120-160 characters).")

        # 3. Open Graph tags
        og_props = {}
        for prop in ["title", "description", "image", "url", "type"]:
            m = re.search(rf'<meta[^>]+(?:property=["']og:{prop}["'][^>]+content=["']([^"']*)["']|content=["']([^"']*)["'][^>]+property=["']og:{prop}["'])', body, re.I)
            if m:
                og_props[f"og:{prop}"] = m.group(1) or m.group(2)
            else:
                results["score"] -= 5
                results["issues"].append(f"Missing Open Graph tag: og:{prop}")
                results["recommendations"].append(f"Specify og:{prop} for optimized social sharing.")
        results["tags"]["open_graph"] = og_props

        # 4. Canonical link
        c_match = re.search(r'<link[^>]+(?:rel=["']canonical["'][^>]+href=["']([^"']*)["']|href=["']([^"']*)["'][^>]+rel=["']canonical["'])', body, re.I)
        if c_match:
            results["tags"]["canonical"] = c_match.group(1) or c_match.group(2)
        else:
            results["score"] -= 10
            results["tags"]["canonical"] = None
            results["issues"].append("Missing <link rel='canonical'> tag.")
            results["recommendations"].append("Add a canonical link tag to consolidate page signals.")

    except Exception as e:
        results["score"] = 0
        results["issues"].append(f"HTTP request error: {str(e)}")
        results["recommendations"].append("Verify server connectivity and HTTP 200 response.")

    results["score"] = max(0, min(100, results["score"]))
    if results["score"] >= 85:
        results["status"] = "OPTIMAL"
    elif results["score"] >= 65:
        results["status"] = "ACCEPTABLE"
    else:
        results["status"] = "DEFICIENT"

    return results

def main():
    parser = argparse.ArgumentParser(description="TAVARDT USA - Meta Tags and Social Graph Inspector")
    parser.add_argument("target", help="Target domain or URL to inspect")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--timeout", type=int, default=8, help="Request timeout in seconds")

    args = parser.parse_args()
    report = inspect_metadata(args.target, timeout=args.timeout)

    if args.json:
        print(json.dumps(report, indent=2))
        return

    print("=" * 60)
    print(" " + "TAVARDT USA - Meta Tags and Social Graph Inspector")
    print("=" * 60)
    print(f"Target: {report['target']}")
    print(f"Metadata Quality Score: {report['score']}/100")
    print(f"Optimization Status: {report['status']}")
    print("-" * 60)

    print(f"\n[Identified Warnings and Issues]:")
    if not report["issues"]:
        print(f"  - All required meta tags and social card protocols are configured properly.")
    else:
        for iss in report["issues"]:
            print(f"  * {iss}")

    print(f"\n[HTML and Social Tag Breakdown]:")
    for k, v in report["tags"].items():
        if isinstance(v, dict):
            print(f"  * {k}:")
            for sub_k, sub_v in v.items():
                print(f"      - {sub_k}: {sub_v}")
        else:
            print(f"  * {k}: {v}")

    if report["recommendations"]:
        print(f"\n[Optimization Recommendations]:")
        for rec in report["recommendations"]:
            print(f"  - {rec}")

    print("-" * 60)
    print(f"Full audit and preview suite: https://tools.tavardt.com/meta-tags-checker/")
    print("=" * 60)

if __name__ == "__main__":
    main()
