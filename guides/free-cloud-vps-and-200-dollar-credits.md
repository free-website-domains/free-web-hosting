# Free cloud VPS, Docker, and $200+ cloud credits (2026)

> Part of [Free web hosting and free domains](../README.md) • [Interactive web guide](https://free-website-domains.github.io/free-web-hosting/free-cloud-vps-credits.html)

Persistent **Node.js, Python, Go, Rust, and Docker** backends with root Linux SSH require **Always-Free Cloud VPS tiers**, **free PaaS containers**, or **$200+ startup cloud credits** rather than static or shared PHP hosting.

---

## Quick Navigation
- [1. Always-Free Cloud VPS Tiers (24/7 Root Linux Servers)](#1-always-free-cloud-vps-tiers-247-root-linux-servers)
- [2. Free Cloud Credits ($200 DigitalOcean & $30 Cloudways Trial)](#2-free-cloud-credits-200-digitalocean--30-cloudways-trial)
- [3. Free PaaS Hosting for Docker, Node.js & Python (No Credit Card)](#3-free-paas-hosting-for-docker-nodejs--python-no-credit-card)
- [4. Free Serverless & Edge Compute Platforms](#4-free-serverless--edge-compute-platforms)
- [5. Free Managed Databases to Pair With Your Cloud App](#5-free-managed-databases-to-pair-with-your-cloud-app)

---

## 1. Always-Free Cloud VPS Tiers (24/7 Root Linux Servers)

These major cloud providers give you real virtual machines with dedicated IPv4 addresses and root SSH access that **never go to sleep**:

| Cloud Provider | Always-Free VM Specs | Memory & SSD Storage | Outbound Bandwidth | Credit Card Needed? | Link |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Oracle Cloud Free Tier** | **Up to 4 ARM Ampere A1 vCPUs** + 2 AMD `e2.1.micro` VMs | **24 GB RAM** + **200 GB Block Storage** | **10 TB / month** | Verification only ($0) | [oracle.com/cloud/free](https://www.oracle.com/cloud/free/) |
| **Google Cloud (GCP)** | **1x `e2-micro` VM** *(in `us-west1`, `us-central1`, `us-east1`)* | 1 GB RAM (0.25 to 2 shared vCPU) + 30 GB HDD | 1 GB / month (North America) | Verification only | [cloud.google.com/free](https://cloud.google.com/free) |
| **AWS Free Tier** | **750 hrs/mo EC2 `t2.micro` or `t3.micro`** *(12 months)* | 1 GB RAM + 30 GB EBS SSD | 100 GB / month | Verification only | [aws.amazon.com/free](https://aws.amazon.com/free/) |
| **Azure Free Account** | **750 hrs/mo `B1s` Linux/Windows VM** *(12 months)* + $200 credit (30 days) | 1 GB RAM + 64 GB Managed Disk | 100 GB / month | Verification only | [azure.microsoft.com/free](https://azure.microsoft.com/free/) |

> **Pro Tip for Oracle Cloud:** You can split your free 4 ARM OCPUs + 24 GB RAM into multiple VMs (for example, 1x `2 OCPU / 12 GB RAM` for Docker + Nginx Proxy Manager, and 1x `2 OCPU / 12 GB RAM` for PostgreSQL/Redis) or run one powerful single node 24/7 for free.

---

## 2. Free Cloud Credits ($200 DigitalOcean & $30 Cloudways Trial)

Enterprise cloud consoles like AWS, GCP, and Oracle have steep learning curves and strict billing traps if you exceed egress quotas. For fast deployments, clean pricing, and predictable billing, use these developer cloud credits:

| Provider | Free Credit / Offer | What You Can Run for Free | Why Developers Choose It | Claim Offer |
| :--- | :--- | :--- | :--- | :---: |
| **DigitalOcean** | **$200 Free Credit** (60 days) + **3 Static Sites Free Forever** | NVMe Droplets (Ubuntu/Docker), Managed Kubernetes, Managed Postgres/MySQL, Spaces CDN | Simplest cloud UI, predictable flat-rate VPS ($4 to $6/mo after credit), 1-click Marketplace apps | [**Claim $200 Free Credit**](https://www.digitalocean.com/) |
| **Cloudways** | **$30 Free Hosting Credit / 3-Day Trial** *(No Credit Card Required)* | Managed WordPress, WooCommerce, Laravel, PHP 8.3 & Magento on DO/AWS/GCP | Zero sysadmin work: automated backups, Object Cache Pro, staging clones & 24/7 live chat | [**Start Free Cloud Trial**](https://www.cloudways.com/) |

---

## 3. Free PaaS Hosting for Docker, Node.js & Python (No Credit Card)

Do you want to deploy from a GitHub repo or `Dockerfile` **without entering a credit card**? These Platform-as-a-Service (PaaS) providers have genuine no-card free plans:

| PaaS Platform | Free Compute & RAM | Sleep Policy | Supported Languages & Runtimes | Link |
| :--- | :--- | :--- | :--- | :--- |
| **Hugging Face Spaces** | **2 vCPU + 16 GB RAM** + 50 GB Disk | Sleeps after **48 hours** of inactivity | **Any Docker container**, Python (FastAPI, Gradio, Streamlit), Node.js | [huggingface.co/spaces](https://huggingface.co/spaces) |
| **Render** | 0.1 CPU + **512 MB RAM** + 100 GB BW | Spins down after 15 mins idle (~30s wake) | Docker, Node.js, Python, Go, Rust, Ruby, Elixir | [render.com](https://render.com/) |
| **Koyeb** | 1 Eco Service (`0.1 vCPU`, **512 MB RAM**, 2 GB disk) | Sleeps when idle | Docker, Node.js, Python, Go, Rust, Java | [koyeb.com](https://www.koyeb.com/) |
| **PythonAnywhere** | 1 Web App + 512 MB Disk + Bash console | **Never sleeps** (1-click 3-month renew) | Python (Django, Flask, FastAPI, Bottle) + MySQL | [pythonanywhere.com](https://www.pythonanywhere.com/) |
| **Serv00** | 3 GB SSD + **512 MB RAM** + FreeBSD Shell | **Never sleeps** (24/7 daemon support) | Node.js, Python, Go, Rust, Ruby, PHP, PostgreSQL | [serv00.com](https://www.serv00.com/) |

---

## 4. Free Serverless & Edge Compute Platforms

Instead of paying for an idle server, deploy event-driven APIs and microservices that scale to zero automatically:

- **Cloudflare Workers:** **100,000 requests/day free**, 0ms cold start, runs JS/TS/Wasm globally ([workers.cloudflare.com](https://workers.cloudflare.com/)).
- **Google Cloud Run:** **2 million requests/month**, 360,000 GB-seconds memory, 180,000 vCPU-seconds **Always Free**, runs any stateless Docker container on HTTP!
- **AWS Lambda:** **1 million requests/month** and 400,000 GB-seconds compute **Always Free** (does not expire after 12 months).
- **Supabase Edge Functions:** **500,000 invocations/month** powered by Deno TypeScript.

---

## 5. Free Managed Databases to Pair With Your Cloud App

- **PostgreSQL:** **Supabase** (500 MB + Auth + Storage) or **Neon** (0.5 GiB serverless Postgres with branching).
- **MySQL:** **TiDB Cloud Serverless** (25 GiB free across 5 clusters) or **Aiven** (1 GB free MySQL without credit card).
- **MongoDB:** **MongoDB Atlas M0** (512 MB permanent free cluster on AWS/GCP/Azure).
- **SQLite at the Edge:** **Turso** (9 GB storage, 500 DBs) or **Cloudflare D1** (5 GB storage).
- **Redis:** **Upstash** (500,000 commands/month, 256 MB).

---

### Related Guides in This Repository
- [← Back to Main Directory (125+ Providers)](../README.md)
- [Free Domains & Free Site Domain Name Guide](./free-domains-and-subdomains.md)
- [Free Homepage & Static Website Hosting](./free-homepage-and-static-hosting.md)
- [Free WordPress, PHP & MySQL Hosting](./free-wordpress-and-php-mysql-hosting.md)
- [Free vs. Cheap Web Hosting Benchmark Comparison](./comparison-free-vs-cheap-hosting.md)
