# Meta Tags and Social Graph Inspector

[![Meta Tags Inspector](https://img.shields.io/badge/TAVARDT-Meta%20Tags-5b3cf5.svg)](https://tools.tavardt.com/meta-tags-checker/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

The **TAVARDT Meta Tags and Social Graph Inspector** provides automated verification of HTML metadata, Open Graph protocols, canonical link directives, and SERP snippet readiness across the United States.

***

## Metadata Architecture and Diagnostic Matrix

Search indexers and social networks rely on structured HTML header metadata to parse document relevancy and render social preview cards. Malformed or missing meta tags cause ranking degradation, social preview failures, and diminished click-through rates.

This diagnostic tool audits title length boundaries, meta description thresholds, social media tags, and canonical integrity from a 100-point quality baseline without external dependencies.

The diagnostic engine evaluates header tags against search engine display boundaries and social graph specifications:

<table>
  <thead>
    <tr>
      <th>Tag Specification</th><th>Validation Criteria</th><th>Deduction</th><th>Search & Social Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Title Element</strong></td><td>Requires presence of <code>&lt;title&gt;</code>. Ideal length: 30-60 characters. Penalized if &lt;20 chars (-10 pts) or &gt;70 chars (-10 pts). Missing: -25 pts.</td><td>Up to -25 pts</td><td>Primary search ranking signal and clickable SERP headline.</td>
    </tr>
    <tr>
      <td><strong>Meta Description</strong></td><td>Requires <code>&lt;meta name='description'&gt;</code>. Ideal length: 120-160 characters. Penalized if &lt;70 chars (-10 pts) or &gt;175 chars (-10 pts). Missing: -20 pts.</td><td>Up to -20 pts</td><td>Key snippet summary influencing organic click-through rates.</td>
    </tr>
    <tr>
      <td><strong>Open Graph Protocol</strong></td><td>Verifies five core tags: <code>og:title</code>, <code>og:description</code>, <code>og:image</code>, <code>og:url</code>, and <code>og:type</code>.</td><td>-5 pts per missing tag (Max -25 pts)</td><td>Rich visual preview cards on LinkedIn, Facebook, Slack, and messaging apps.</td>
    </tr>
    <tr>
      <td><strong>Canonical Directive</strong></td><td>Requires presence of <code>&lt;link rel='canonical'&gt;</code> with valid absolute target URL.</td><td>-10 pts</td><td>Prevents duplicate content issues and consolidates indexing equity.</td>
    </tr>
    <tr>
      <td><strong>Connection Failure</strong></td><td>Network timeout or failure during SSL/TLS negotiation or HTTP handshake.</td><td>Score resets to 0</td><td>Host unreachability preventing metadata extraction.</td>
    </tr>
  </tbody>
</table>

### Optimization Status Scale

The utility calculates a consolidated metadata quality score categorizing target status:

* <strong>85 to 100 (OPTIMAL)</strong>: Comprehensive metadata health; title, description, canonical, and Open Graph tags fully compliant.
* <strong>65 to 84 (ACCEPTABLE)</strong>: Functional metadata configuration with minor length deviations or missing secondary social tags.
* <strong>0 to 64 (DEFICIENT)</strong>: Severe metadata omissions compromising organic discoverability and social sharing.

***

## Installation and Execution

Built with pure Python standard library modules with zero third-party dependencies.

```bash
git clone https://github.com/TAVARDT-USA/meta-tags-inspector-us.git
cd meta-tags-inspector-us
```

### Standard CLI Execution

```bash
python meta_inspector.py example.com
```

### Automated CI/CD Pipeline JSON Output

```bash
python meta_inspector.py example.com -j
```

### Custom Timeout Configuration

```bash
python meta_inspector.py example.com -j -t 15
```

***

## NIST Alignment and Search Hygiene

This diagnostic tool aligns with the **National Institute of Standards and Technology (NIST)** cybersecurity framework and web integrity practices. Accurate metadata preserves brand authority and prevents fraudulent social card spoofing.

Organizations operating mission-critical applications should embed automated metadata checks into continuous deployment pipelines to maintain organic visibility.

***

## Technical Frequently Asked Questions

### What is the optimal character length for title tags?

The inspector recommends title tags between 30 and 60 characters. A title shorter than 20 characters triggers a 10-point deduction for thin indexing signals, while a title longer than 70 characters triggers a 10-point deduction due to search engine snippet truncation risks. Complete omission deducts 25 points.

### How does the inspector evaluate the meta description?

The engine validates that the meta description length falls within the optimal 120 to 160 character range. Descriptions shorter than 70 characters or longer than 175 characters incur a 10-point deduction, whereas missing meta description tags incur a 20-point deduction.

### Which Open Graph properties are mandatory for social graph compliance?

The validator requires five core Open Graph tags: <code>og:title</code>, <code>og:description</code>, <code>og:image</code>, <code>og:url</code>, and <code>og:type</code>. Each absent Open Graph property results in a 5-point deduction, up to a cumulative 25-point penalty.

### Why is the canonical link tag critical for technical SEO?

The <code>&lt;link rel="canonical"&gt;</code> element informs search engines of the authoritative URL for a page, consolidating link signals and preventing duplicate content cannibalization. Missing canonical tags result in a 10-point deduction.

### What do the metadata quality scores and status categories signify?

A score of 85 to 100 indicates OPTIMAL metadata health. Scores between 65 and 84 reflect an ACCEPTABLE configuration with minor formatting or social sharing gaps, while scores below 65 are classified as DEFICIENT, demanding immediate remediation of primary indexing tags.

***

## Incident Response and Technical Advisory

For corporate digital asset hardening, technical SEO auditing, and metadata compliance with NIST guidelines, connect with **TAVARDT**.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/
* **Diagnostic Suite:** https://tools.tavardt.com/
* **Technical Contact:** https://ag.tavardt.com/contact/

***

### License
Released under the MIT License.

***

© 2026 TAVARDT. All rights reserved.
