# Free domains and site domain names (2026)

> Part of [Free web hosting and free domains](../README.md) • [Interactive web guide](https://free-website-domains.github.io/free-web-hosting/free-domains.html)

After Freenom (`.tk`, `.ml`, `.ga`, `.cf`, `.gq`) closed, getting a reliable **free site domain name** means picking registries listed in the **Mozilla Public Suffix List (PSL)** or active developer GitOps registries that support Cloudflare DNS, GitHub Pages, Vercel, and Netlify.

---

## Quick Navigation
- [1. Best Free Top-Level Domains & Public Suffixes](#1-best-free-top-level-domains--public-suffixes)
- [2. How to Claim a Free `.me` or `.live` Domain (Students)](#2-how-to-claim-a-free-me-or-live-domain-students)
- [3. Step-by-Step: EU.org & DigitalPlat with Cloudflare DNS](#3-step-by-step-euorg--digitalplat-with-cloudflare-dns)
- [4. Step-by-Step: Developer Subdomains (`is-a.dev`, `js.org`, `Open Domains`)](#4-step-by-step-developer-subdomains-is-adev-jsorg-open-domains)
- [5. Free Dynamic DNS (DDNS) Domains for Home Servers & VPS](#5-free-dynamic-dns-ddns-domains-for-home-servers--vps)
- [6. When to Upgrade to a Free `.com` Bundle or $0.98 Domain](#6-when-to-upgrade-to-a-free-com-bundle-or-098-domain)

---

## 1. Best Free Top-Level Domains & Public Suffixes

Unlike basic subdomains, domains in the **Mozilla Public Suffix List (PSL)** allow full `NS` record delegation. That means you can attach them directly to **Cloudflare Free DNS**, manage SSL certificates independently, and isolate browser cookies.

| Registry | Free Extensions | Full `NS` Delegation? | Cloudflare Compatible? | Best For | Link |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **Namecheap (`nc.me`)** | `.me` *(1st year free)* | Yes (Full TLD) | Yes | Students with `.edu` email or GitHub Student Pack | [**Check Namecheap**](https://www.namecheap.com/) |
| **Name.com Student** | `.live`, `.studio`, `.software`, `.app`, `.dev` | Yes (Full TLD) | Yes | GitHub Student Developer Pack members | [name.com/partner/github-students](https://www.name.com/partner/github-students) |
| **EU.org Registry** | `.eu.org` *(e.g. `mysite.eu.org`)* | Yes (PSL since 1996) | Yes | Long-term hobby projects & personal sites | [nic.eu.org](https://nic.eu.org/) |
| **DigitalPlat FreeDomain** | `.dpdns.org`, `.qzz.io`, `.us.kg`, `.xx.kg` | Yes | Yes | Developers wanting fast Cloudflare-ready domains | [domain.digitalplat.org](https://domain.digitalplat.org/) |
| **Public Free Suffix** | `.is-a.si`, `.pfsdns.org`, `.no.kg`, `.so.kg` | Yes | Yes | Personal projects, REST APIs & AI agents | [publicfreesuffix.org](https://publicfreesuffix.org/) |
| **PP.UA Registry** | `.pp.ua` | Yes (PSL) | Yes | Personal websites (requires Telegram/SMS check) | [pp.ua](https://pp.ua/) |
| **GNAME Free Program** | `.eu.cc` | Yes | Yes | Startups, students & side projects | [gname.com/tld-eu-cc.html](https://www.gname.com/tld-eu-cc.html) |

---

## 2. How to Claim a Free `.me` or `.live` Domain (Students)

If you have an academic email address or student ID, you can register a real top-level **free site domain name** with zero catch during year one:

1. Apply for the [GitHub Student Developer Pack](https://education.github.com/pack) using your university email or student verification document.
2. Visit [**Namecheap (`nc.me`)**](https://www.namecheap.com/) to claim a **100% free `.me` domain for 1 year** (includes Free WhoisGuard domain privacy and free SSL deals).
3. You can also check **Name.com** inside the Student Pack for free `.live`, `.software`, or `.studio` domains.
4. Connect your new domain directly to [free homepage hosting](./free-homepage-and-static-hosting.md) on **GitHub Pages**, **Cloudflare Pages**, or **Vercel**.

---

## 3. Step-by-Step: EU.org & DigitalPlat with Cloudflare DNS

Because **EU.org** and **DigitalPlat FreeDomain** support full `NS` delegation, you can connect them to Cloudflare for free DDoS protection, Edge SSL, and CDN caching:

1. **Create a Cloudflare zone first** (for EU.org, nameservers must answer authoritatively before registration approval).
2. Alternatively, point `NS` records to **ClouDNS Free** or **Hurricane Electric (`dns.he.net`)** first so the zone responds with valid SOA/NS records.
3. Submit your domain request at `nic.eu.org` or `domain.digitalplat.org` with those authoritative nameservers.
4. Once approved, switch `NS` records to your Cloudflare pair (e.g., `alice.ns.cloudflare.com` and `bob.ns.cloudflare.com`) and point a `CNAME` record (`@` or `www`) to your [free static website host](./free-homepage-and-static-hosting.md).

---

## 4. Step-by-Step: Developer Subdomains (`is-a.dev`, `js.org`, `Open Domains`)

If you do not want to wait for manual registry review, GitOps community registries issue permanent **free domains** via a standard GitHub Pull Request:

### Example: Registering `yourname.is-a.dev`
1. Fork [`is-a-dev/register`](https://github.com/is-a-dev/register).
2. Create a file named `domains/yourname.json`:
   ```json
   {
     "owner": {
       "username": "your-github-username",
       "email": "you@example.com"
     },
     "records": {
       "CNAME": "your-github-username.github.io"
     }
   }
   ```
3. Open a Pull Request. Once automated CI checks verify your site is live and non-malicious, your `yourname.is-a.dev` domain propagates globally within minutes.

### Other Active GitOps Subdomain Registries
- **`*.js.org`**, Best for open-source JavaScript libraries and documentation ([js.org](https://js.org/)).
- **`*.is-cool.dev` / `*.is-a-fullstack.dev` / `*.is-local.org`**, Managed by [Open Domains](https://open-domains.net/).
- **`*.thedev.id` / `*.is-a-good.dev` / `*.is-pro.dev`**, Clean developer portfolio domains.
- **`*.cli.rs`**, Dedicated subdomain for Rust command-line tools.

---

## 5. Free Dynamic DNS (DDNS) Domains for Home Servers & VPS

Running a site from a Raspberry Pi, home lab, or a [free Cloud VPS](./free-cloud-vps-and-200-dollar-credits.md) with a changing IP address? Use a free DDNS domain with automatic cron updates:

```bash
# Example: Update your free *.duckdns.org IPv4 address via cron every 5 minutes
curl -s "https://www.duckdns.org/update?domains=YOUR_SUBDOMAIN&token=YOUR_TOKEN&ip="
```

Top zero-expiration DDNS providers:
- **DuckDNS (`*.duckdns.org`)**, Up to 5 subdomains, never expires, native Let's Encrypt `TXT` DNS-01 API.
- **deSEC (`*.dedyn.io`)**, Nonprofit DNSSEC-signed free domains with REST API and Certbot integration.
- **Dynu (`*.dynu.net`, `*.mywire.org`)**, 4 free hostnames that do not require monthly click-confirmations.

---

## 6. When to Upgrade to a Free `.com` Bundle or $0.98 Domain

Free subdomains and `.eu.org` domains are great for personal portfolios, APIs, and student demos. However, for SEO rankings, business credibility, and branded email (`hello@yourdomain.com`), a real top-level domain is essential:

- **All-in-One Free `.com` + Web Hosting Bundle:** [**Hostinger**](https://www.hostinger.com/) includes a **free `.com` or `.net` domain name for 1 year** plus 100 GB NVMe hosting and free business email (~$1.99 to $2.99/mo).
- **Lowest-Cost Standalone Domains:** [**Namecheap**](https://www.namecheap.com/) frequently offers `.xyz`, `.site`, `.online`, and `.store` domains starting around **$0.98/year** with free forever WhoisGuard privacy protection.

---

### Related Guides in This Repository
- [← Back to Main Directory (125+ Providers)](../README.md)
- [Best Free Homepage & Static Website Hosting](./free-homepage-and-static-hosting.md)
- [Best Free WordPress, PHP & MySQL Hosting](./free-wordpress-and-php-mysql-hosting.md)
- [Free Cloud VPS & $200 DigitalOcean Credits](./free-cloud-vps-and-200-dollar-credits.md)
- [Free vs. Cheap Web Hosting Benchmark Comparison](./comparison-free-vs-cheap-hosting.md)
