# Resume-Builder

## Description
This project is a resume builder I developed for building a beautiful LaTeX typset resume from jsonresume conforming yaml data.  This allows for easy iteration and tracking of changes via diffs.  It also allows for the data itself to be used in any context where jsonresume is supported.

## Usage
* Ensure you have docker installed and running.
* Install pyinvoke: `pip3 install invoke`
* Install builder requirements: `pip3 install builder/requirements.txt`
* Ensure you have jsonresume conforming yaml data in `data/`, to use mine clone the repo with: `git clone --recursive`.
* Build your pdf: `inv render --data={name-of-file}`.  *Do not include data/ path or .yaml suffix*

## Results
Here are some example's of the results, exported using `pdftoppm`.

![preview-page-1](preview-1.png)
![preview-page-2](preview-2.png)

## Showing off
And just because I'm a total nerd, here is an example of the text extracted from the pdf when running `pdftotext -layout {pdf_file}`.  This is great for ATS!

```
Joe Black
Experienced software engineer obsessed with blockchain
New York, NY          (646) 924-7718           me@joeblack.nyc             https://joeblack.nyc           joeblack949      joeblackwaslike



Summary
 Passionate engineer and linux expert with 7 years of experience seeking an engineering role where I can leaverage my expertise
 to help build the future of ethereum. I’m self-managed, determined, embody the principles of grit, and thrive in a fast-paced
 environment.

Awards
  Winner               Stanford Datajam, a hackathon sponsored by the US Department of Education. (2014)                      Palo Alto, CA

Skills
  Languages             Python 2, Python 3, Bash, Javascript, Solidity, Golang, Ruby/Rails, Flask, Pyramid
  Technologies          Linux, Unix, Docker, Kubernetes, AWS, SQL, NoSQL, RESTful APIs, Cryptography, CI/CD, Git/Github, LATEX
  Blockchain            Ethereum, Bitcoin, Decentralized Apps, Smart Contracts, P2P, Swarm, IPFS, ENS, Whisper, PSS, uPort, Truffle


Work Experience
  Co-founder & Software Engineer                                                                                         06/2017 – 12/2018
  Telephone                                                                                                                   New York, NY
  • Co-founded a start-up to fund and develop a privacy-focused decentralized communications solution.
  • Collaboratively architected a decentralized protocol and app using ethereum, solidity, python, and javascript.
  • Educated and advised co-founders on the constraints posed by decentralized architecture and the ICO funding
    process to better align the vision of the company and viability of the product.
  • Designed a decentralized services marketplace to incentivize the development of new features, build community,
    and support the underlying token economy.
  • Implemented daily automated email check-ins, leading to a 50% increase in team communication and morale.

  Software Engineer                                                                                                      04/2014 – Present
  Black Limited                                                                                                               New York, NY
  •   Founded a development and consulting company which I use for short-term contract work referred to me.
  •   Developed and deployed a privacy-focused crypto-commerce platform using python, flask, and bitcoin.
  •   Developed tools in python used by the Security Scorecard platform for IP attribution of vendors.
  •   Leveraged ML/NLP to identify inconsistencies across legal contracts for a law firm specializing in foreclosures.
  •   Developed open-source python projects such as the official BTCPay client, GPGKeyring, and Pricing.

  Software Engineer & DevOps                                                                                             08/2015 – 06/2017
  Call for America, LLC                                                                                                       New York, NY
  • Built and maintained a bare-metal kubernetes-based infrastructure to scale the Kazoo cloud PBX platform.
  • Slashed maintenance costs over 50% by automating the deployment and maintenance of critical infrastructure
    using docker, kubernetes, python, and bash.
  • Developed and implemented custom tools for containerizing self-configuring microservices using python, bash,
    C, and golang.
  • Diagnosed and upgraded overloaded MySQL servers to Percona, eliminating daily downtime entirely.
  • Increased platform stability over 30% by spearheading the development of tooling for spec-testing containers
    using bash and goss.
  • Led efforts to draft and implement testing, CI/CD, and documentation standards resulting in a 60% increase in
    developer productivity.
  • Developed many open-source projects such as TmplD, CouchDiscover, Docker-Debian, and Docker-Kazoo.

 Co-founder & Software Engineer                                                                                        06/2013 – 08/2015
 Unorthodox, LLC                                                                                                       San Francisco, CA
  • Co-founded and developed a small data-driven email-marketing platform with real-time analytics in python.
  • Improved delivery over 50% using MTA throttling based on provider history, IP reputation, and SMTP reject codes.
  • Implemented real-time analytics to improve campaign insights using python, AWS, URL redirection, and kibana.
  • Increased targeting relevancy over 100% by enriching existing demographic data using third-party data append
    APIs such as TowerData and FullContact.
  • Built tools to predict the actions of spam-filters based on content patterns and tokens using python and docker.



Extracurricular Activities
 Mentor                                                                                                                       2013 – 2015
 Noisebridge Hackerspace                                                                                               San Francisco, CA
  • Mentored hackers and students from local universities and code bootcamps with various engineering related
    projects and tasks.

 Speaker                                                                                                                             2014
 HackMiami Conference                                                                                                           Miami, FL
  • Delivered a bio-hacking talk discussing the usage of various technologies, proteins, and growth factors for cog-
    nitive enhancement with the co-founder of Hack Miami.



Education
 Computer Science                                                                                                        Indianapolis, IN
 Ivy Tech College


Open Source Projects
 BTCPay-python                                                                               https://github.com/btcpayserver/btcpay-python
 The official python client for the BTCPay Server API, an open-source payment processor for bitcoin and litecoin.
 python, cryptocurrency, bitcoin, RESTful APIs, BTCPay

 GPGKeyring                                                                                  https://github.com/joeblackwaslike/gpgkeyring
 A pythonic, object-oriented interface to performing cryptography operations and key management using Gnu Privacy Guard (GPG).
 python, cryptography, GPG

 Pricing                                                                                         https://github.com/joeblackwaslike/pricing
 A python package for aggregating, converting, and formatting of prices in a variety of currencies, including crypto and custom.
 python, pricing, money, localization, currency, cryptocurrency, currency exchange

 TmplD                                                                                            https://github.com/joeblackwaslike/tmpld
 Advanced configuration templating in jinja2 using cluster state for self-configuring, containerized, microservice architectures.
 python, containers, docker, kubernetes, jinja2, configuration, microservices

 Docker-Kazoo                                                                                https://github.com/telephoneorg/docker-kazoo
 The internet’s most downloaded docker image for the Kazoo Cloud PBX platform.
 kazoo, bash, docker, kubernetes

 Docker-Debian                                                                                      https://github.com/telephoneorg/debian
 Custom, minimal debian jessie/stretch distro for docker in only 24MB!
 linux, bash, docker, base-image

```




