import random, pathlib, html
from PIL import Image

OUT = pathlib.Path("/home/claude/site")
BASE = "https://www.valor-ksa.com"

NAV = [("index.html", "Home"), ("about.html", "About Us"), ("products.html", "Products"),
       ("partners.html", "Our Partner"), ("enquire.html", "Enquire")]

PRODUCTS = [
    dict(slug="vitamin-d3", img="d3-adult.jpg", tint="--p-d3", name="Vitamin D3", strength="Natural 1200 IU · Oral Spray",
         alt="Vitamin D3 Natural 1200 IU oral spray, 30 ml pack", tag="Immunity + Bones", short="Adults: immunity, bones and muscle function.",
         bullets=["100% natural composition", "Contributes to normal function of the immune system",
                  "Supports maintenance of normal bones and teeth", "Supports maintenance of normal muscle function",
                  "Highly bioavailable formula"], meta="30 ml · Adults · food supplement"),
    dict(slug="vitamin-d3-children", img="d3-children.jpg", tint="--p-d3k", name="Vitamin D3 for Children", strength="400 IU · Oral Spray",
         alt="Vitamin D3 for Children 400 IU oral spray, 30 ml pack", tag="Growth + Immunity", short="Growth and immune support.",
         bullets=["Supports normal growth and development of bone", "Contributes to normal function of the immune system",
                  "Hypoallergenic, 100% natural composition", "Tooth-kind formula (sugar-free)", "Airless bottle"],
         meta="30 ml · 215 daily dosages · food supplement"),
    dict(slug="strong-iron", img="iron.jpg", tint="--p-iron", name="Strong Iron", strength="14 mg with B12, B6, C &amp; Folate",
         alt="Strong Iron 14 mg with B12, B6, C and Folate oral spray, 30 ml pack", tag="Energy + Blood", short="Energy, haemoglobin and cognition.",
         bullets=["Supports normal formation of red blood cells", "Contributes to reduction of tiredness and fatigue",
                  "Supports normal function of the immune system", "Contributes to normal haemoglobin formation and cognitive function",
                  "Vitamin C increases iron absorption"], meta="30 ml · 50-day supply · food supplement"),
    dict(slug="zinc", img="zinc.jpg", tint="--p-zinc", name="Zinc", strength="25 mg · Oral Spray",
         alt="Zinc 25 mg oral spray, 30 ml pack", tag="Immunity + Skin", short="Immunity, skin, nails and vision.",
         bullets=["Supports normal immune system function", "Maintains normal nails, bones and skin",
                  "Contributes to fertility and reproduction", "Supports vision and cognitive function",
                  "Tooth-kind formula (sugar-free) in an airless bottle"], meta="30 ml · 21 daily dosages · food supplement"),
    dict(slug="vitamin-b12", img="b12.jpg", tint="--p-b12", name="Vitamin B12", strength="1000 µg · Oral Spray",
         alt="Vitamin B12 1000 µg oral spray, 30 ml pack", tag="Energy + Nervous System", short="Energy, nervous system and red blood cells.",
         bullets=["Supports psychological function and nervous system", "Helps red blood cell formation",
                  "More energy, less tiredness", "Tooth-kind formula (sugar-free)", "Airless bottle"],
         meta="30 ml · 72 daily dosages · food supplement"),
]

STEPS = [("Registration", "Dossiers, approvals and local compliance."), ("Import &amp; clearance", "Documentation and customs handling."),
         ("Controlled storage", "Batch and expiry management."), ("Inventory planning", "Demand-aligned replenishment."),
         ("Nationwide delivery", "Pharmacy and retail coverage."), ("After-sales", "Orders, returns and enquiries.")]


for _p in PRODUCTS:
    _p["w"], _p["h"] = Image.open(OUT / "assets/img" / _p["img"]).size


def mist_svg():
    """Abstract oral-spray mist. Placeholder until the Higgsfield hero (asset H1) is approved."""
    rnd = random.Random(7)
    import math
    def group(cls, n, seed_shift):
        out = [f'<g class="{cls}">']
        for _ in range(n):
            d = rnd.random() ** 0.8
            ang = math.radians(-42 + rnd.uniform(-20, 20))
            x = 70 + math.cos(ang) * d * 420
            y = 330 + math.sin(ang) * d * 420
            r = 2 + d * 9 * rnd.random() + 1
            fill = rnd.choice(["#ffffff", "#c6d8f2", "#e0b13f", "#8fd3a8"])
            op = round(0.25 + (1 - d) * 0.5 * rnd.random() + 0.1, 2)
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" opacity="{op}"/>')
        out.append("</g>")
        return "".join(out)
    nozzle = ('<g><rect x="34" y="338" width="64" height="30" rx="6" fill="#e6edf6" transform="rotate(-42 66 353)"/>'
              '<rect x="14" y="352" width="30" height="12" rx="4" fill="#e0b13f" transform="rotate(-42 29 358)"/></g>')
    return (f'<svg viewBox="0 0 400 400" role="img" aria-label="Fine mist leaving an oral spray nozzle" focusable="false">'
            f'{nozzle}{group("mist-a", 70, 1)}{group("mist-b", 60, 2)}</svg>')


def utility():
    return ('<div class="utility"><div class="wrap"><span>Commercial Registration No. 4030538785</span>'
            '<span class="contact"><a href="mailto:Info@valor-ksa.com">Info@valor-ksa.com</a>'
            '<a href="tel:+966560592662">+966 56 059 2662</a></span></div></div>')


def header(current):
    links = "".join(
        f'<li><a class="link" href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a></li>'
        for href, label in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
{utility()}
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html"><img src="assets/img/logo-v2.png" alt="Valor Ideal Trading Company LLC" width="204" height="52"></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="nav" id="site-nav" aria-label="Main"><ul>{links}</ul>
<a class="btn btn--primary" href="enquire.html">Send an Enquiry</a></nav>
</div></header>'''


def cta():
    return '''<section class="cta" aria-labelledby="cta-h"><div class="wrap">
<div><h2 id="cta-h">Let's build healthier access</h2><p>Talk to our team about distribution, listings and availability.</p></div>
<a class="btn btn--primary" href="enquire.html">Send an Enquiry</a></div></section>'''


def footer():
    return '''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><img src="assets/img/logo-v2-light.png" alt="Valor Ideal Trading Company LLC" width="196" height="50">
<p>Health, wellness and nutritional supplement distribution across the Kingdom of Saudi Arabia.</p>
<p>Commercial Registration No. 4030538785</p></div>
<div><h2>Company</h2><ul><li><a href="about.html">About Us</a></li><li><a href="partners.html">Our Partner</a></li></ul></div>
<div><h2>Portfolio</h2><ul><li><a href="products.html">Products</a></li><li><a href="enquire.html">Enquire</a></li></ul></div>
<div><h2>Contact</h2><ul><li><a href="mailto:Info@valor-ksa.com">Info@valor-ksa.com</a></li>
<li><a href="tel:+966560592662">+966 56 059 2662</a></li><li>Kingdom of Saudi Arabia</li></ul></div>
</div>
<p class="legal">© 2026 Valor Ideal Trading Company LLC. Quality · Reliability · Compliance</p>
</div></footer>'''


def steps_list():
    items = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in STEPS)
    return f'<ol class="steps">{items}</ol>'


def page(fname, title, desc, body, current=None, extra_head="", head_class=""):
    url = f"{BASE}/" if fname == "index.html" else f"{BASE}/{fname}"
    t = html.escape(title, quote=True)
    d = html.escape(desc, quote=True)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og-valor.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a2858">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&amp;family=Public+Sans:wght@400;600;700&amp;display=swap">
<link rel="stylesheet" href="assets/css/style.css">
{extra_head}
</head>
<body>
{header(current or fname)}
<main id="main">
{body}
{cta()}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    (OUT / fname).write_text(doc, encoding="utf-8")


def page_head(h1, lede):
    return f'<section class="page-head"><div class="wrap"><h1>{h1}</h1><p class="lede">{lede}</p></div></section>'


# ------------------------------------------------------------------ HOME
minis = "".join(
    f'<li><a class="mini" style="--tint:var({p["tint"]})" href="products.html#{p["slug"]}">'
    f'<div class="pic"><img src="assets/img/{p["img"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}" loading="lazy" decoding="async"></div>'
    f'<h3>{p["name"]}</h3><p>{p["short"]}</p></a></li>' for p in PRODUCTS)

jsonld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Valor Ideal Trading Company LLC","url":"https://www.valor-ksa.com/","logo":"https://www.valor-ksa.com/assets/img/logo-v2.png","email":"Info@valor-ksa.com","telephone":"+966560592662","foundingDate":"2023","areaServed":"SA","description":"Distributor of EU-manufactured oral-spray food supplements across the Kingdom of Saudi Arabia."}</script>'''

home = f'''
<section class="hero"><div class="wrap">
<div>
<p class="kicker">Trusted distribution in the Kingdom</p>
<h1>European quality for the Saudi market</h1>
<p class="lede">Valor Ideal Trading combines a Saudi operating foundation, an EU-manufactured supplement portfolio and an end-to-end route-to-market model connecting international manufacturers with pharmacy, healthcare and retail channels.</p>
<div class="actions"><a class="btn btn--primary" href="products.html">Explore products</a><a class="btn btn--ghost" href="partners.html">Our manufacturing partner</a></div>
<ul class="facts"><li><strong>2023</strong>Established</li><li><strong>KSA</strong>Registered</li><li><strong>EU</strong>Manufactured</li></ul>
</div>
<div class="hero-art">{mist_svg()}</div>
</div></section>

<section class="section" aria-labelledby="what-h"><div class="wrap">
<div class="intro"><h2 id="what-h">A focused platform for trusted distribution</h2>
<p class="lede">A structured bridge connecting international manufacturers with Saudi pharmacy, healthcare and retail channels.</p></div>
<ul class="points">
<li><h3>Saudi foundation</h3><p>Established in 2023 as a Saudi LLC under Commercial Registration No. 4030538785.</p></li>
<li><h3>Manufacturing partner</h3><p>NorVita (Estonia), an EU specialist in oral-spray and liquid food supplements.</p></li>
<li><h3>Portfolio platform</h3><p>Oral sprays covering vitamin D3, iron, zinc and vitamin B12 across adult and children's needs.</p></li>
<li><h3>Route to market</h3><p>Registration, import, controlled storage, inventory planning, distribution and after-sales service.</p></li>
<li><h3>Partner value</h3><p>Local regulatory ownership, channel knowledge and responsive commercial support.</p></li>
<li><h3>Growth direction</h3><p>A scalable model designed to expand adult and children's wellness categories.</p></li>
</ul></div></section>

<section class="section section--mist" aria-labelledby="spray-h"><div class="wrap split">
<div><h2 id="spray-h">Why oral spray formats</h2>
<p class="lede">Convenient delivery designed for modern routines, built on a specialist European manufacturing platform.</p>
<a class="btn btn--outline" href="products.html">View the range</a></div>
<ul class="checks panel">
<li>Absorbed through the oral mucosa: reported by the manufacturer as up to 2.6× more effective than tablets and capsules</li>
<li>A few sprays under the tongue: no pills and no water</li>
<li>Sugar-free, tooth-kind formulations</li>
<li>Airless 30 ml bottles with 150–215 sprays per bottle</li>
</ul></div></section>

<section class="section" aria-labelledby="nor-h"><div class="wrap split">
<div><h2 id="nor-h">NorVita, Estonia</h2>
<p>Our portfolio is developed and produced by NorVita, an Estonian contract manufacturer specialising in liquid food supplements: oral sprays, gels, drops and single-serve formats.</p>
<a href="partners.html">About our manufacturing partner</a></div>
<ul class="checks"><li>Developed and produced in Estonia</li><li>ISO 22000, GMP and HACCP quality systems</li><li>Airless bottle platform</li></ul>
</div></section>

<section class="section section--foam" aria-labelledby="port-h"><div class="wrap">
<div class="intro"><h2 id="port-h">Five products, one platform</h2>
<p class="lede">Adult and children's formats for immunity, energy, bones, skin and nervous-system support. All five use a consistent 30 ml oral-spray format.</p></div>
<ul class="product-grid">{minis}</ul></div></section>

<section class="section" aria-labelledby="route-h"><div class="wrap">
<div class="intro"><h2 id="route-h">Distribution across the value chain</h2>
<p class="lede">A model designed to protect product integrity and availability.</p></div>
{steps_list()}</div></section>
'''
page("index.html", "Health & Wellness Distribution in Saudi Arabia | Valor Ideal Trading",
     "Valor Ideal Trading Company LLC distributes EU-manufactured oral-spray food supplements across the Kingdom of Saudi Arabia. Established 2023, C.R. 4030538785.",
     home, extra_head=jsonld)

# ------------------------------------------------------------------ PRODUCTS
cards = "".join(
    f'<li class="product" id="{p["slug"]}" style="--tint:var({p["tint"]})">'
    f'<div class="pic"><img src="assets/img/{p["img"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}" loading="lazy" decoding="async"></div>'
    f'<div><span class="tag">{p["tag"]}</span><h2>{p["name"]}</h2><p class="strength">{p["strength"]}</p>'
    f'<ul class="checks">{"".join(f"<li>{b}</li>" for b in p["bullets"])}</ul><p class="meta">{p["meta"]}</p></div></li>'
    for p in PRODUCTS)

table_rows = [("Vitamin D3", "Natural 1200 IU", "Adults", "Immunity, bones, muscle function", "30 ml"),
              ("Vitamin D3 for Children", "400 IU", "Children", "Bone growth, immunity", "30 ml · 215 daily dosages"),
              ("Strong Iron", "14 mg + B12, B6, C, folate", "Adults", "Red blood cells, energy, cognition", "30 ml · 50-day supply"),
              ("Zinc", "25 mg", "Adults", "Immunity, skin, nails, vision", "30 ml · 21 daily dosages"),
              ("Vitamin B12", "1000 µg", "Adults", "Nervous system, energy, red blood cells", "30 ml · 72 daily dosages")]
trs = "".join("<tr><th scope=\"row\">%s</th>%s</tr>" % (r[0], "".join(f"<td>{c}</td>" for c in r[1:])) for r in table_rows)

products = f'''
{page_head("Five launch products, one platform", "A focused oral-spray range covering daily wellness needs for adults and children.")}
<section class="section section--mist" aria-label="Format benefits"><div class="wrap">
<ul class="points">
<li><h3>Highly bioavailable</h3><p>Oral-mucosa delivery, reported by the manufacturer as up to 2.6× more effective than tablets and capsules.</p></li>
<li><h3>Easy to use</h3><p>A few sprays under the tongue: no pills and no water. Sugar-free, tooth-kind formulations.</p></li>
<li><h3>Airless bottle</h3><p>Airless 30 ml bottles protect micronutrients after opening, with 150–215 sprays per bottle.</p></li>
</ul></div></section>
<section class="section" aria-label="Products"><div class="wrap">
<ul class="catalogue">{cards}</ul>
<p class="note">Product claims, dosing, suitability and availability follow the final approved local label and registration dossier.</p>
</div></section>
<section class="section section--foam" aria-labelledby="sum-h"><div class="wrap">
<div class="intro"><h2 id="sum-h">Launch portfolio at a glance</h2>
<p class="lede">All five products share one 30 ml oral-spray platform: a single supply, storage and registration workflow.</p></div>
<div class="table-scroll" tabindex="0" role="region" aria-label="Range summary table, scrolls sideways on small screens">
<table><caption class="sr-only">Launch portfolio at a glance</caption>
<thead><tr><th scope="col">Product</th><th scope="col">Strength</th><th scope="col">Target</th><th scope="col">Key benefits</th><th scope="col">Pack</th></tr></thead>
<tbody>{trs}</tbody></table></div></div></section>
'''
page("products.html", "Products | Valor Ideal Trading",
     "Oral-spray food supplements distributed by Valor Ideal Trading: Vitamin D3 Natural 1200 IU, Vitamin D3 for Children 400 IU, Strong Iron 14 mg, Zinc 25 mg and Vitamin B12 1000 µg.",
     products)

# ------------------------------------------------------------------ ABOUT
about = f'''
{page_head("Saudi roots, European supply", "Established in 2023 in the Kingdom of Saudi Arabia.")}
<section class="section" aria-labelledby="ov-h"><div class="wrap split">
<div><h2 id="ov-h">Company overview</h2>
<p>Valor Ideal Trading Company LLC is a Saudi limited liability company specialising in the import, storage and distribution of health, wellness and nutritional supplement products.</p>
<p>We connect European manufacturing with local pharmacy, healthcare and retail channels through a disciplined, partnership-led model, building capability first in registration, compliance, controlled storage and inventory management, then growing the range.</p></div>
<div class="panel"><h3>Company identity</h3>
<dl class="idlist"><dt>Legal name</dt><dd>Valor Ideal Trading Company LLC</dd><dt>Legal form</dt><dd>Limited Liability Company</dd>
<dt>Established</dt><dd>2023</dd><dt>Country</dt><dd>Kingdom of Saudi Arabia</dd><dt>C.R. number</dt><dd>4030538785</dd></dl></div>
</div></section>
<section class="section section--mist" aria-label="Vision, mission and values"><div class="wrap"><div class="trio">
<div class="panel"><h3>Vision</h3><p>To become a trusted distribution partner for health and wellness products in Saudi Arabia, with quality, reliability and service at the centre.</p></div>
<div class="panel"><h3>Mission</h3><p>To provide manufacturers with a reliable, compliant and efficient route into the Saudi market while improving access to differentiated wellness products.</p></div>
<div class="panel"><h3>Values</h3><p>Quality excellence, operational discipline, regulatory compliance, customer focus and long-term partnership.</p></div>
</div></div></section>
<section class="section" aria-labelledby="op-h"><div class="wrap">
<div class="intro"><h2 id="op-h">Route-to-market capability</h2>
<p class="lede">Designed to protect product integrity and support availability across the value chain.</p></div>
{steps_list().replace("Dossiers, approvals and local compliance.", "Dossiers, approvals and label compliance managed locally.").replace("Pharmacy and retail coverage.", "Pharmacy, healthcare and retail coverage.").replace("Orders, returns and enquiries.", "Orders, returns and customer enquiries.")}
</div></section>
<section class="section section--foam" aria-labelledby="com-h"><div class="wrap split">
<div><h2 id="com-h">Supporting the Kingdom's health sector</h2>
<p>Valor Ideal Trading positions its growth within Saudi Arabia's healthcare and wellness development, contributing local market knowledge, access to differentiated wellness formats and capability development within the distribution sector.</p></div>
<div><h2>Built for partnership</h2>
<p>We work with manufacturers and channel partners who need disciplined commercial execution and dependable local representation inside the Kingdom.</p>
<p><strong>Quality · Reliability · Compliance</strong></p></div>
</div></section>
'''
page("about.html", "About Us | Valor Ideal Trading",
     "Valor Ideal Trading Company LLC — a Saudi limited liability company established in 2023 for health, wellness and nutritional supplement distribution. C.R. 4030538785.",
     about)

# ------------------------------------------------------------------ PARTNERS
partners = f'''
{page_head("NorVita — European manufacturing partner", "An Estonian specialist in liquid food supplements and oral-spray delivery formats.")}
<section class="section" aria-labelledby="eu-h"><div class="wrap split">
<div><h2 id="eu-h">European manufacturing excellence</h2>
<p>Our portfolio is developed and produced by NorVita, a contract manufacturer based in Estonia focusing exclusively on liquid food supplements: oral sprays, gels, drops and single-serve formats.</p>
<p>Manufacturing in the EU gives the portfolio a documented quality basis: certifications, specifications and product documentation that support registration and give channel partners confidence in what they stock.</p></div>
<div class="panel"><h3>NorVita</h3><p>Iru, Harjumaa — Estonia. Spray the health.</p>
<ul class="checks"><li>Developed and produced in Estonia</li><li>ISO 22000 quality system</li><li>GMP manufacturing practices</li><li>HACCP food-safety framework</li></ul></div>
</div></section>
<section class="section section--mist" aria-labelledby="plat-h"><div class="wrap">
<div class="intro"><h2 id="plat-h">Specialist formats and quality systems</h2></div>
<ul class="points" style="grid-template-columns:repeat(2,minmax(0,1fr))">
<li><h3>EU manufacturing</h3><p>All products developed and produced in Estonia within a specialist liquid-supplement facility.</p></li>
<li><h3>Quality systems</h3><p>Manufactured under ISO 22000, GMP and HACCP standards.</p></li>
<li><h3>Specialist focus</h3><p>Exclusively liquid food supplements: oral sprays, gels, drops and single-serve formats.</p></li>
<li><h3>Airless bottle platform</h3><p>Airless bottles protecting micronutrients after opening, with 150–215 sprays per bottle.</p></li>
</ul></div></section>
<section class="section" aria-labelledby="val-h"><div class="wrap">
<div class="intro"><h2 id="val-h">What this partnership delivers</h2></div>
<div class="trio">
<div><h3>For manufacturers</h3><p>Structured market entry, local regulatory and commercial support, and Saudi channel access.</p></div>
<div><h3>For pharmacies &amp; retailers</h3><p>Differentiated delivery formats, a documented manufacturing foundation and a consistent product platform.</p></div>
<div><h3>For healthcare partners</h3><p>Convenient oral-spray formats, clear product documentation and daily wellness categories.</p></div>
</div></div></section>
<section class="section section--foam"><div class="wrap split">
<div><h2>One platform, one workflow</h2>
<p>The five-product launch range shares a 30 ml oral-spray platform, supporting common storage, inventory and distribution processes while creating a foundation for future category expansion.</p></div>
<div><h2>Why Valor Ideal Trading</h2><ul class="checks">
<li>Saudi LLC under Commercial Registration No. 4030538785</li><li>EU-manufactured range under recognised quality systems</li>
<li>Local regulatory ownership and label compliance</li><li>Responsive order and after-sales support</li>
<li>One scalable model across adult and children's ranges</li></ul></div>
</div></section>
'''
page("partners.html", "Our Partner | Valor Ideal Trading",
     "Our portfolio is developed and produced by NorVita, an Estonian specialist in liquid food supplements, manufacturing under ISO 22000, GMP and HACCP.",
     partners)

# ------------------------------------------------------------------ ENQUIRE
types = ["Manufacturing / brand partnership", "Pharmacy or retailer enquiry", "Product availability", "Healthcare enquiry", "General business enquiry"]
opts = "".join(f"<option>{t}</option>" for t in types)
enquire = f'''
{page_head("Start a conversation", "Partnership, distribution, product availability and healthcare enquiries.")}
<section class="section"><div class="wrap enquiry">
<div><h2>Company contact</h2>
<dl class="idlist"><dt>Company</dt><dd>Valor Ideal Trading Company LLC</dd>
<dt>Email</dt><dd><a href="mailto:Info@valor-ksa.com">Info@valor-ksa.com</a></dd>
<dt>Telephone</dt><dd><a href="tel:+966560592662">+966 56 059 2662</a></dd>
<dt>Website</dt><dd>www.valor-ksa.com</dd><dt>C.R.</dt><dd>4030538785</dd><dt>Country</dt><dd>Kingdom of Saudi Arabia</dd></dl></div>
<div><h2>Send an enquiry</h2>
<form id="enquiry-form" action="https://formspree.io/f/YOUR_FORM_ID" method="post">
<div class="row"><div><label for="f-name">Full name <span class="req" aria-hidden="true">*</span></label><input id="f-name" name="name" autocomplete="name" required></div>
<div><label for="f-email">Business email <span class="req" aria-hidden="true">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div></div>
<div class="row"><div><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization"></div>
<div><label for="f-country">Country</label><input id="f-country" name="country" autocomplete="country-name"></div></div>
<div><label for="f-type">Enquiry type <span class="req" aria-hidden="true">*</span></label><select id="f-type" name="type" required>{opts}</select></div>
<div><label for="f-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="f-msg" name="message" required></textarea></div>
<div class="hp" aria-hidden="true"><label>Leave empty <input name="website" tabindex="-1" autocomplete="off"></label></div>
<div><button class="btn btn--primary" type="submit">Submit enquiry</button></div>
<p class="form-status" id="form-status" role="status" aria-live="polite"></p>
</form></div>
</div></section>
'''
page("enquire.html", "Enquire | Valor Ideal Trading",
     "Send a partnership, distribution, product or healthcare enquiry to Valor Ideal Trading Company LLC. Info@valor-ksa.com, +966 56 059 2662.",
     enquire)

# ------------------------------------------------------------------ sitemap + robots
urls = ["", "about.html", "products.html", "partners.html", "enquire.html"]
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{BASE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("built")
