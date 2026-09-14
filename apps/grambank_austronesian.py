# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair==6.2.2",
#     "marimo>=0.24.2",
#     "numpy==2.5.3",
#     "plotly==7.0.0",
#     "polars==1.44.2",
#     "toytree==3.0.11",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/grambank_austronesian.slides.json",
)


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    from pathlib import Path
    import json
    import io
    import re
    import urllib.request
    import html
    from collections import defaultdict

    import plotly.graph_objects as go
        # Works both locally and on GitHub Pages WASM
    try:
        # 1. Try fetching via HTTP (works in WASM / App Mode on GitHub Pages)
        import js
        from pyodide.http import open_url
    
        response = open_url("./public/slides_layout.json")
        slides_data = json.loads(response.read())
    
    except ImportError:
        # 2. Fallback to standard local file reading (for local notebook dev)
        with open("apps/public/slides_layout.json", "r") as f:
            slides_data = json.load(f)


    return alt, defaultdict, go, html, io, json, mo, pl, re, urllib


@app.cell
def _(mo):
    mo.md(r"""
    # Austronesian
    #Languages
    ### From Madagascar to Rapa Nui — 1,200 languages, two structural fascinations: phoneme inventories and the focus system.
    - Elihu Solano Norzagaray
    """)
    return


@app.cell
def _(mo):
    stat1 = mo.stat(
        value="1,200",
        label="member languages",
        bordered=True,
    )

    stat2 = mo.stat(
        value="1/5",
        label="of the world's languages",
        bordered=True,
    )

    stat3 = mo.stat(
        value="206°",
        label="of longitude spanned",
        bordered=True,
    )

    return stat1, stat2, stat3


@app.cell
def _(mo, stat1, stat2, stat3):
    mo.md(rf"""
    ## A family that spans 206° of longitude
    With approximately **1,200 members**, Austronesian covers about one-fifth of the world's languages. Before European colonial expansion it was the most widely distributed language family on Earth — from Madagascar off East Africa to Rapa Nui 2,200 miles west of Chile.
    {mo.hstack([stat1, stat2, stat3], widths="equal")}
    Major languages include Tagalog, Cebuano, Malay, Javanese, Malagasy, Fijian, Samoan, and Hawaiian. Javanese alone accounts for roughly a quarter of all Austronesian speakers.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Subgrouping at a glance
    The family splits into the Formosan languages of Taiwan (perhaps six primary branches) and the massive Malayo-Polynesian branch. The biggest, best-defined subgroup is Oceanic — the languages of Polynesia, Micronesia, and Austronesian Melanesia.
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ### PRIMARY BRANCH
    ## Formosan
    A cover term for ~14 surviving aboriginal languages of Taiwan. Several may each be a primary branch coordinate with all of Malayo-Polynesian.

    {mo.md("<p style='text-align: center; margin: 0;'>EX  Atayal · Amis · Paiwan</p>")}
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ### WMP
    ## Western Malayo-Polynesian
    A catchall for non-CEMP languages: Philippines, western Indonesia, mainland SE Asia, Madagascar, plus Chamorro & Palauan.

    {mo.md("<p style='text-align: center; margin: 0;'>EX Tagalog · Malay · Javanese · Malagasy </p>")}
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ### CMP
    ## Central Malayo-Polynesian
    Eastern Indonesia — Lesser Sundas from Sumbawa through Timor, and most of the Moluccas. Group is questioned by some scholars.

    {mo.md("<p style='text-align: center; margin: 0;'> EX Manggarai · Tetum · Buruese</p>")}
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ### SHWNG
    ## South Halmahera–West New Guinea
    Small group on Halmahera and the Doberai (Bird's Head) Peninsula of western New Guinea.


    {mo.md("<p style='text-align: center; margin: 0;'>EX Buli · Numfor-Biak · Waropen</p>")}
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ### OC
    ## Oceanic
    Largest & best-defined subgroup. All of Polynesia, all of Micronesia except Palauan & Chamorro, and AN languages of Melanesia east of the Mamberamo.


    {mo.md("<p style='text-align: center; margin: 0;'>EX Fijian · Tongan · Samoan · Māori · Hawaiian</p>")}
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ### OUTLIER
    ## Polynesian Outliers
    ~18 Polynesian-speaking societies scattered in Melanesia and Micronesia — genetic Polynesian languages outside Polynesia proper.


    {mo.md("<p style='text-align: center; margin: 0;'>EX Kapingamarangi · Tikopia · Anuta</p>")}
    """)
    return


@app.cell
def _(mo):
    mo.md(rf"""
    ## Phonology
    Inventories from the extreme minimal to the unusually rich, simple vowel systems, and a roster of rare consonant types found nowhere else.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## From the world's smallest to one of its largest
    Most Austronesian languages sit in a comfortable 16–22 consonant range with 4 or 5 vowels. The extremes are dramatic — and informative.

    Most words target a disyllabic (two-syllable) canonical shape. Javanese əri "thorn" — historically reduced to ri — regained its schwa to satisfy the disyllabic preference. Most Oceanic languages force every word to end in a vowel, either by dropping final consonants or by adding an echo vowel.
    """)
    return


@app.cell
def _(mo):

    # Phoneme datasets
    H_consonants = ["/p/", "/k/", "/ʔ/", "/m/", "/n/", "/l/", "/h/", "/w/"]
    H_vowels = ["/a/", "/e/", "/i/", "/o/", "/u/"]

    # Generate HTML badges for consonants and vowels
    H_consonant_badges = "".join(
        [f'<span class="badge badge-c">{c}</span>' for c in H_consonants]
    )
    H_vowel_badges = "".join(
        [f'<span class="badge badge-v">{v}</span>' for v in H_vowels]
    )

    hawaii =mo.md(
        f"""
    <div class="phoneme-card">
        <div class="phoneme-header">
            <span class="highlight">{len(H_consonants)}</span> consonants &middot; <span class="highlight">{len(H_vowels)}</span> vowels
        </div>
        <div class="phoneme-row">
            <span class="row-label">C</span>
            {H_consonant_badges}
        </div>
        <div class="phoneme-row">
            <span class="row-label">V</span>
            {H_vowel_badges}
        </div>
    </div>

    <style>
    .phoneme-card {{
        padding: 20px;
        border-radius: 6px;
        font-family: monospace;
        color: #4a5d78;
        display: inline-block;
        width: 100%;
        box-sizing: border-box;
    }}

    .phoneme-header {{
        font-size: 1.3rem;
        margin-bottom: 16px;
        letter-spacing: 0.5px;
    }}

    .highlight {{
        color: #f3ad38;
        font-weight: bold;
    }}

    .phoneme-row {{
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 10px;
    }}

    .row-label {{
        width: 16px;
        font-size: 0.85rem;
        color: #6c7d93;
    }}

    .badge {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 4px 10px;
        border-radius: 16px;
        font-size: 0.9rem;
        border: 1px solid;
        white-space: nowrap; /* Prevents text from breaking onto multiple lines */
        min-width: fit-content; /* Ensures container expands to fit IPA symbols */
    }}

    .badge-c {{
        border-color: #4a5d78;
        color: #4a5d78;
    }}

    .badge-v {{
        border-color: #f3ad38;
        color: #f3ad38;
    }}
    </style>
    """
    )
    return (hawaii,)


@app.cell
def _(mo):

    # Phoneme datasets
    N_consonants = [
        "/pʷ/", "/pᵐʷ/", "/mʷ/", "/mᶠʷ/", "/ᵐbʷ/", "/pʷʰ/",
        "/p/", "/pᵐ/", "/m/", "/m̥/", "/ᵐb/", "/pʰ/",
        "/t/", "/tⁿ/", "/n/", "/n̥/", "/ⁿd/", "/tʰ/", "/r/", "/r̥/", "/s/",
        "/c/", "/cⁿ̠/", "/ɲ/", "/ɲ̥/", "/ⁿ̠ɟ/", "/cʰ/",
        "/k/", "/kᵑ/", "/ŋ/", "/ŋ̥/", "/ᵑɡ/", "/kʰ/",
        "/w/", "/w̥/", "/w̃/", "/w̥̃/", "/h̃/"
    ]

    N_vowels = [
        "/i/", "/i:/", "/e/", "/e:/",
        "/a/", "/a:/",
        "/u/", "/u:/", "/o/", "/o:/"
    ]

    # Generate HTML badges for consonants and vowels
    N_consonant_badges = "".join(
        [f'<span class="badge badge-c">{c}</span>' for c in N_consonants]
    )
    N_vowel_badges = "".join(
        [f'<span class="badge badge-v">{v}</span>' for v in N_vowels]
    )

    nami =mo.md(
        f"""
    <div class="phoneme-card">
        <div class="phoneme-header">
            <span class="highlight">{len(N_consonants)}</span> consonants &middot; <span class="highlight">{len(N_vowels)}</span> vowels
        </div>
        <div class="phoneme-row">
            <span class="row-label">C</span>
            {N_consonant_badges}
        </div>
        <div class="phoneme-row">
            <span class="row-label">V</span>
            {N_vowel_badges}
        </div>
    </div>

    """
    )
    return (nami,)


@app.cell
def _(hawaii, mo):
    mo.md(rf"""
    ### MINIMAL INVENTORY
    ## Hawaiian
    {hawaii}
    """)
    return


@app.cell(hide_code=True)
def _(mo, nami):
    mo.md(rf"""
    ### Maximal INVENTORY
    ## Nami
    {nami}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## The Focus System

    The grammatical centerpiece of Philippine and Formosan languages — verbal affixes that select which argument is in **focus**, and a 100-year debate over what they really are.
    """)
    return


@app.cell
def _(mo):

    # Pill header tag
    tag1 = mo.md("`STATIVE VERBS`")

    # Main header and paragraph description
    header1 = mo.md("### States — often translate as English adjectives")

    body1 = mo.md(
        "Stative verbs describe conditions: being afraid, being sick, being new, "
        "being asleep, or color words. Many languages lack a separate adjective "
        "class — statives do that work."
    )

    # Example callout box using marimo's neutral callout styling
    examples1 = mo.callout(
        mo.md(
            """
            `> ma-` + numeral &rarr; `ma-gatos` *"one hundred"* (Maranao)  
            `> ma-` is the productive stative prefix
            """
        ),
        kind="neutral",
    )



    # Pill header tag
    tag2 = mo.md("`DYNAMIC VERBS`")

    # Main header and paragraph description
    header2 = mo.md("### Actions — and the home of the focus system")

 

            
    body2 = mo.md(
        "Dynamic verbs are morphologically richer. Formosan, Philippine, "
        "and many Sulawesi languages attach a large inventory of affixes"
        "to mark which argument is in focus — the system we examine next."
    )

    # Example callout box using marimo's neutral callout styling
    examples2 = mo.callout(
        mo.md(
            """
            `> -um-, -in-, -an, i- — focus affixes  
            `> All four appear on dynamic verb stems
            """

        ),
        kind="neutral",
    )



    # Stack elements together inside a card container
    card1 = mo.md(
        f"""
        {tag1}
        {header1}
        {body1}
        {examples1}
        """
    )

    # Stack elements together inside a card container
    card2 = mo.md(
        f"""
        {tag2}
        {header2}
        {body2}
        {examples2}
        """
    )

    return card1, card2


@app.cell
def _(card1, card2, mo):
    mo.md(rf"""
    ## Before focus: stative vs. dynamic
    The most fundamental split in Austronesian verb systems isn't tense or aspect — it's whether a verb describes a state or an action. Many Austronesian languages have no clean category of "adjectives"; that work is done by stative verbs.

    {mo.hstack([card1, card2], widths="equal")}
    **WHY THIS MATTERS** The stative/dynamic split is older than the focus system itself. When focus morphology erodes — as it has across much of Indonesia and the Pacific — stative verbs typically survive as the only morphologically distinct verb class.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### tagalog
    ## Four affixes, four focused arguments
    In Tagalog, the affix on the verb tells the listener which noun phrase is in focus — actor, patient, location, or instrument. The focused NP is marked by ang (common nouns) or si (personal names) and is always definite; non-focused NPs may be indefinite.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | Focus | Affix | Glossed as | Focused NP marker | Role picked out |
    | --- | --- | --- | --- | --- |
    | Actor focus (AF) | -um- (infix) | actor / subject | ang / si | the doer of the action |
    | Patient focus (PF) | -in- (past) / -in (nonpast) | patient / object | ang / si | the undergoer of the action |
    | Locative focus (LF) | -an (suffix) | location / goal | ang / si | the place where the action occurs |
    | Instrumental / benefactive focus (IF) | i- (prefix) | instrument / beneficiary | ang / si | the means or the beneficiary |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### FOCUS SYSTEM · TAGALOG EXAMPLES
    ## One verb, four sentences
    All four sentences describe a buying event involving **Maria**, **bread**, a **store**, and (in the last) **money**.

    What changes is which NP is focused — and the verb's affix tracks that choice.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ACTOR FOCUS



    $$
    \begin{array}{l}
    \begin{array}{ccccccc}
    \mathbf{\text{B-um-ilí}} & \text{si} & \text{Maria} & \text{ng} & \text{tinapay} & \text{sa} & \text{tindahan.} \\
    \mathbf{\text{\small Buy-AF}} & \text{\small si} & \text{\small Maria} & \text{\small ng} & \text{\small bread} & \text{\small sa} & \text{\small store.}
    \end{array} \\
    \text{“Maria bought some bread at the store.”}
    \end{array}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### PATIENT FOCUS



    $$
    \begin{array}{l}
    \begin{array}{ccccccc}
    \mathbf{\text{B-in-ilí}} & \text{ni} & \text{Maria} & \text{ang} & \text{tinapay} & \text{sa} & \text{tindahan.} \\
    \mathbf{\text{\small Buy-AF}} & \text{\small ni} & \text{\small Maria} & \text{\small ang} & \text{\small bread} & \text{\small sa} & \text{\small store.}
    \end{array} \\
    \text{"Maria bought the bread at the store."}
    \end{array}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LOCATIVE FOCUS


    $$
    \begin{array}{l}
    \begin{array}{ccccccc}
    \mathbf{\text{B-in-ilh-án}} & \text{ng} & \text{babae} & \text{ng} & \text{tinapay} & \text{ang} & \text{tindahan} & \text{ni}& \text{Aling}& \text{Maria.} \\
    \mathbf{\text{\small Buy-LF}} & \text{\small ng} & \text{\small woman} & \text{\small ng} & \text{\small bread} & \text{\small ang} & \text{\small store} & \text{\small ni} & \text{\small Aling} & \text{\small Maria.}
    \end{array} \\
    \text{"The woman bought some bread at Maria's store."}
    \end{array}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### INSTRUMENTAL FOCUS


    $$
    \begin{array}{l}
    \begin{array}{ccccccc}
    \mathbf{\text{I-b-in-ilí}} & \text{ni} & \text{Maria} & \text{ng} & \text{tinapay} & \text{ang} & \text{pera} & \text{nang}& \text{tatay-niyá.}\\
    \mathbf{\text{\small Buy-IF}} & \text{\small ni} & \text{\small Maria} & \text{\small ng} & \text{\small bread} & \text{\small ang} & \text{\small money} & \text{\small ni} & \text{\small father-her.}
    \end{array} \\
    \text{"Maria bought some bread with her father's money."}
    \end{array}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Voice, or case-marking?

    Since Bloomfield (1917), two schools have argued over what the focus system really is. The disagreement is not just terminological — it changes what you think a "subject" is in these languages.
    """)
    return


@app.cell
def _(mo):

    # Pill header tag
    voice = mo.md("`BLOOMFIELD, 1917`")

    # Main header and paragraph description
    v1 = mo.md("### Focus = voice")

    v2 = mo.md(
        "Tagalog has one active voice and three passives: a direct passive (patient), a local passive (locative), and an instrumental/benefactive passive. The 'focused' NP is the surface subject of a passive construction."
    )

    # Example callout box using marimo's neutral callout styling
    v3 = mo.callout(
        mo.md(
            """
    Affixes mark active vs. 3 passive voices.
            """
        ),
        kind="neutral",
    )



    # Pill header tag
    focus = mo.md("`MODERN INTERPRETATION`")

    # Main header and paragraph description
    f1 = mo.md("### Focus = case-marking")
 

            
    f2 = mo.md(
        "Focus affixes mark the case role of the subject on the verb. The system is not voice alternation but rich case agreement — the verb indexes which thematic role the subject bears."
    )

    # Example callout box using marimo's neutral callout styling
    f3 = mo.callout(
        mo.md(
            """
            Affixes mark the case role of the subject.
            """

        ),
        kind="neutral",
    )



    # Stack elements together inside a card container
    card3 = mo.md(
        f"""
        {voice}
        {v1}
        {v2}
        {v3}
        """
    )

    # Stack elements together inside a card container
    card4 = mo.md(
        f"""
        {focus}
        {f1}
        {f2}
        {f3}
        """
    )

    return card3, card4


@app.cell(hide_code=True)
def _(card3, card4, mo):
    mo.md(rf"""
    ## Before focus: stative vs. dynamic
    The most fundamental split in Austronesian verb systems isn't tense or aspect — it's whether a verb describes a state or an action. Many Austronesian languages have no clean category of "adjectives"; that work is done by stative verbs.

    {mo.hstack([card3, card4], widths="equal")}

    **WHY THIS MATTERS** Unlike a simple active–passive system, the focus system can promote a prepositional phrase — "at the store," "with the money" — to subject. ang tindahan "the store" can be the subject of "buy" when the verb carries -an.
    """)
    return


@app.cell
def _(mo):

    af = mo.md("ACTOR FOCUS")              
    aff = mo.md(
        "# *-um-"
    )
    afff = mo.callout(
        mo.md(
            """
            Survives robustly in Tagalog, Formosan languages.
            """
        ),
        kind="neutral",
    )
    card5 = mo.md(
        f"""
        {af}
        {aff}
        {afff}

        """
    )

    a3 = mo.md("LOCATIVE FOCUS")              
    a33 = mo.md(
        "# *-an"
    )
    a333 = mo.callout(
        mo.md(
            """
    Also survives as a nominalizer in many daughter languages.
            """
        ),
        kind="neutral",
    )
    card7 = mo.md(
        f"""
        {a3}
        {a33}
        {a333}
        """
    )

    a2 = mo.md("PATIENT FOCUS")              
    a22 = mo.md(
        "# *-en"
    )
    a222 = mo.callout(
        mo.md(
            """
    Fused with completive *-in- → *k-in-aen "was eaten by me."
            """
        ),
        kind="neutral",
    )
    card6 = mo.md(
        f"""
        {a2}
        {a22}
        {a222}
        """
    )



    a4 = mo.md("INSTRUMENTAL FOCUS")              
    a24 = mo.md(
        "# *-si"
    )
    a224 = mo.callout(
        mo.md(
            """
    Continues in Philippine-type languages; lost elsewhere.
            """
        ),
        kind="neutral",
    )
    card8 = mo.md(
        f"""
        {a4}
        {a24}
        {a224}
        """
    )
    return card5, card6, card7, card8


@app.cell(hide_code=True)
def _(card5, card6, card7, card8, mo):
    mo.md(rf"""
    ### PROTO-AUSTRONESIAN
    ##The focus system is old — and slowly eroding

    The four focus affixes reconstruct cleanly to Proto-Austronesian. Across 1,200 daughter languages, they have fared differently — robust in the Philippines and Formosa, reduced to nominalizers in much of Indonesia and the Pacific, lost entirely in Malay.

    {mo.hstack([card5, card6, card7, card8], widths="equal")}

    Where focus has been lost — as in Malay, modern Javanese, and most of Oceanic — the old affixes do not vanish. They survive as nominalizers, derivational pieces that turn verbs into nouns. The particle ni, which in Tagalog marks non-focused actors and possessors identically, has no grammatical role at all in Malay — it lingers only as a pejorative personal-name marker: si Gemuk "Chubby."
    """)
    return


@app.cell
def _():
    grambank_url_input  = "https://raw.githubusercontent.com/grambank/grambank/refs/heads/master/cldf/families.csv"
    glottolog_url_input  = "https://raw.githubusercontent.com/glottolog/glottolog-cldf/refs/heads/master/cldf/languages.csv"
    return glottolog_url_input, grambank_url_input


@app.cell
def _(glottolog_url_input, io, pl, urllib):
    # Helper to read remote CSV files using standard urllib
    def fetch_csv(url: str, **kwargs) -> pl.DataFrame:
        req = urllib.request.Request(url, headers={"User-Agent": "marimo-polars"})
        with urllib.request.urlopen(req) as resp:
            return pl.read_csv(io.BytesIO(resp.read()), **kwargs)

    # Load Glottolog tree and isolate aust1307
    df_trees = fetch_csv(
        glottolog_url_input,
        has_header=False,
        new_columns=["family_id", "newick_tree"],
        truncate_ragged_lines=True,
    )

    # Extract all unique Glottocodes appearing in the aust1307 tree
    austronesian_glottocodes = (
        df_trees.lazy()
        .filter(pl.col("family_id") == "aust1307")
        .select(
            pl.col("newick_tree")
            .str.extract_all(r"[a-z]{4}\d{4}")
            .alias("glottocode")
        )
        .explode("glottocode")
        .unique()
        .collect()
    )


    return


@app.cell
def _(grambank_url_input, io, pl, urllib):
    def fetch_bytes(url: str) -> io.BytesIO:
        req = urllib.request.Request(url, headers={"User-Agent": "marimo-polars"})
        with urllib.request.urlopen(req) as resp:
            return io.BytesIO(resp.read())

    # Ensure a URL has been provided before executing

    df_grambank_raw = pl.read_csv(
        fetch_bytes(grambank_url_input),
        has_header=False,
        new_columns=["family_id", "newick_tree"],
        separator=",",
        quote_char='"',
        truncate_ragged_lines=True,
    )

    # Extract all Glottocodes (4 letters followed by 4 digits) under aust1307
    df_grambank_aust = (
        df_grambank_raw.lazy()
        .filter(pl.col("family_id") == "aust1307")
        .select(
            pl.col("newick_tree")
            .str.extract_all(r"[a-z]{4}\d{4}")
            .alias("glottocode")
        )
        .explode("glottocode")
        .filter(pl.col("glottocode") != "aust1307")  # Remove root family code
        .unique()
        .collect()
    )

    return


@app.cell
def _(glottolog_url_input, io, pl, urllib):
    def load_source_csv(source: str, **kwargs) -> pl.DataFrame:
        source = source.strip()
        if source.startswith("http://") or source.startswith("https://"):
            req = urllib.request.Request(source, headers={"User-Agent": "marimo-polars"})
            with urllib.request.urlopen(req) as resp:
                return pl.read_csv(io.BytesIO(resp.read()), **kwargs)
        return pl.read_csv(source, **kwargs)


    df_glottolog_raw = load_source_csv(glottolog_url_input)

    # Identify key columns (accommodates standard names or 0-indexed column positions)
    cols = df_glottolog_raw.columns
    id_col = "id" if "id" in cols else ("glottocode" if "glottocode" in cols else cols[0])
    parent_col = cols[9] if len(cols) >= 10 else ("family_id" if "family_id" in cols else cols[1])
    name_col = "name" if "name" in cols else ("Name" if "Name" in cols else cols[1])
    level_col = "level" if "level" in cols else ("Level" if "Level" in cols else None)


    return (
        df_glottolog_raw,
        id_col,
        level_col,
        load_source_csv,
        name_col,
        parent_col,
    )


@app.cell
def _(defaultdict, df_glottolog_raw, id_col, level_col, parent_col, pl):
    # 1. Build adjacency mapping: parent_id -> list of child_ids
    parent_to_children = defaultdict(list)
    for child, parent in df_glottolog_raw.select([id_col, parent_col]).iter_rows():
        if parent is not None and str(parent).strip() != "":
            parent_to_children[str(parent)].append(str(child))

    # 2. BFS traversal to find all descendants under 'aust1307'
    root_family = "aust1307"
    austronesian_descendants = set()
    queue = [root_family]

    while queue:
        current_node = queue.pop(0)
        for child in parent_to_children.get(current_node, []):
            if child not in austronesian_descendants:
                austronesian_descendants.add(child)
                queue.append(child)

    # 3. Filter the DataFrame to only Austronesian descendants
    df_aust_all = df_glottolog_raw.filter(pl.col(id_col).is_in(austronesian_descendants))

    # 4. Filter down strictly to language-level (excluding sub-families and dialects)
    if level_col:
        df_aust_languages = df_aust_all.filter(pl.col(level_col).str.to_lowercase() == "language")
    else:
        df_aust_languages = df_aust_all

    return df_aust_languages, parent_to_children, root_family


@app.cell
def _(grambank_url_input, load_source_csv, pl, root_family):
    # Guard execution if Grambank input is missing

    gb_raw_table = load_source_csv(
        grambank_url_input,
        has_header=False,
        new_columns=["family_glotto", "tree_string"],
        separator=",",
        quote_char='"',
        truncate_ragged_lines=True,
    )

    gb_aust_codes = set(
        gb_raw_table.lazy()
        .filter(pl.col("family_glotto") == root_family)
        .select(
            pl.col("tree_string")
            .str.extract_all(r"[a-z]{4}\d{4}")
            .alias("code")
        )
        .explode("code")
        .unique()
        .collect()["code"]
        .to_list()
    )


    return gb_aust_codes, gb_raw_table


@app.cell
def _(
    df_aust_coded_values,
    df_aust_languages,
    df_glottolog_raw,
    gb_aust_codes,
    id_col,
    mo,
    name_col,
    pl,
):
    # Detect latitude and longitude columns flexibly
    lat_found = [c for c in df_glottolog_raw.columns if c.lower() in ("latitude", "lat")]
    lon_found = [c for c in df_glottolog_raw.columns if c.lower() in ("longitude", "lon", "long")]

    lat_col = lat_found[0] if lat_found else None
    lon_col = lon_found[0] if lon_found else None

    # Build consolidated Austronesian comparison DataFrame
    comparison_exprs = [
        pl.col(id_col).alias("glottocode"),
        pl.col(name_col).alias("language_name"),
        pl.col(id_col).is_in(gb_aust_codes).alias("is_in_grambank"),
    ]

    if lat_col and lon_col:
        comparison_exprs.extend([
            pl.col(lat_col).cast(pl.Float64, strict=False).alias("latitude"),
            pl.col(lon_col).cast(pl.Float64, strict=False).alias("longitude"),
        ])
    else:
        comparison_exprs.extend([
            pl.lit(None, dtype=pl.Float64).alias("latitude"),
            pl.lit(None, dtype=pl.Float64).alias("longitude"),
        ])

    df_comparison_result = df_aust_languages.lazy().select(comparison_exprs).collect()

    # Statistics
    # The true documented set: languages that have at least one feature in values.csv
    true_grambank_documented_codes = set(
        df_aust_coded_values.lazy()
        .select(pl.col("glottocode"))
        .unique()
        .collect()["glottocode"]
        .to_list()
    )

    # Re-run comparison against actual feature data
    df_true_comparison = (
        df_aust_languages.lazy()
        .select([
            pl.col(id_col).alias("glottocode"),
            pl.col(name_col).alias("language_name"),
            pl.col(id_col).is_in(true_grambank_documented_codes).alias("has_grambank_data"),
        ])
        .collect()
    )

    true_total = df_true_comparison.height
    true_doc = df_true_comparison.filter(pl.col("has_grambank_data")).height
    true_undoc = true_total - true_doc
    true_pct = (true_doc / true_total * 100) if true_total > 0 else 0.0

    aust_stats_panel = mo.hstack([
        mo.stat(label="Total Austronesian Languages (Glottolog)", value=str(true_total)),
        mo.stat(label="Documented in Grambank (values.csv)", value=str(true_doc)),
        mo.stat(label="Undocumented (0 Grambank data)", value=str(true_undoc)),
        mo.stat(label="True Grambank Coverage", value=f"{true_pct:.1f}%"),
    ], justify="space-between")

    return aust_stats_panel, lat_col, lon_col, true_grambank_documented_codes


@app.cell(hide_code=True)
def _(aust_stats_panel, mo):
    mo.md(rf"""
    ## Grambank Stats

    {aust_stats_panel
    }
    """)
    return


@app.cell
def _(
    df_glottolog_raw,
    gb_raw_table,
    id_col,
    mo,
    name_col,
    pl,
    re,
    root_family,
):

    # 1. Self-contained language name lookup
    name_lookup = dict(
        df_glottolog_raw.select([
            pl.col(id_col).cast(pl.String),
            pl.col(name_col).cast(pl.String),
        ]).iter_rows()
    )

    # 2. Recursive parser from Newick string into nested clade dictionary
    def parse_newick_to_clade(nwk_str: str) -> dict:
        nwk_str = nwk_str.strip().rstrip(";")
        tokens = re.findall(r"([(),])|([a-z0-9_]+)(?::\d+(?:\.\d+)?)?", nwk_str, re.IGNORECASE)
        stack = [[]]
    
        for sep, name in tokens:
            if sep == "(":
                stack.append([])
            elif sep == ",":
                continue
            elif sep == ")":
                children = stack.pop()
                stack[-1].append({"name": "", "children": children})
            elif name:
                if stack[-1] and stack[-1][-1].get("name") == "":
                    stack[-1][-1]["name"] = name
                else:
                    stack[-1].append({"name": name, "children": []})
                
        return stack[0][0] if stack[0] else {"name": root_family, "children": []}

    # 3. Extract Austronesian Newick tree from Grambank table
    raw_nwk_record = gb_raw_table.filter(pl.col("family_glotto") == root_family)
    aust_newick_string = raw_nwk_record["tree_string"].item(0) if raw_nwk_record.height > 0 else "()"

    full_aust_tree = parse_newick_to_clade(aust_newick_string)

    # 4. Build dropdown options to isolate subclades or view full family
    clade_dropdown_options = {"Full Austronesian Family": full_aust_tree}
    for branch in full_aust_tree.get("children", []):
        branch_id = branch.get("name", "")
        branch_label = f"Subclade: {name_lookup.get(branch_id, branch_id)} ({branch_id})"
        clade_dropdown_options[branch_label] = branch

    clade_selector = mo.ui.dropdown(
        options=clade_dropdown_options,
        value="Full Austronesian Family",
        label="Select Subclade to View:"
    )
    return clade_selector, name_lookup


@app.cell
def _(clade_selector, go, mo, name_lookup, true_grambank_documented_codes):
    # Reactively updates whenever clade_selector.value changes
    active_tree_node = clade_selector.value

    clade_x_lines = []
    clade_y_lines = []
    clade_leaf_data = []
    current_leaf_y = 0

    def layout_cladogram(node: dict, depth: float = 0.0) -> tuple[float, float]:
        global current_leaf_y
        children = node.get("children", [])
    
        if not children:
            y = float(current_leaf_y)
            current_leaf_y += 1
            leaf_code = node.get("name", "")
            clade_leaf_data.append({
                "x": depth,
                "y": y,
                "code": leaf_code,
                "name": name_lookup.get(leaf_code, leaf_code),
                "is_documented": leaf_code in true_grambank_documented_codes,
            })
            return depth, y

        # Compute child branch positions
        child_pts = [layout_cladogram(c, depth + 1.0) for c in children]
        child_ys = [p[1] for p in child_pts]
        node_y = sum(child_ys) / len(child_ys)
        node_x = depth

        # Vertical crossbar connecting daughter branches
        min_y, max_y = min(child_ys), max(child_ys)
        clade_x_lines.extend([node_x, node_x, None])
        clade_y_lines.extend([min_y, max_y, None])

        # Horizontal bars leading to each child
        for cx, cy in child_pts:
            clade_x_lines.extend([node_x, cx, None])
            clade_y_lines.extend([cy, cy, None])

        return node_x, node_y

    # Generate coordinate layout
    current_leaf_y = 0
    layout_cladogram(active_tree_node, 0.0)

    fig_cladogram = go.Figure()

    # 1. Cladogram branch lines
    fig_cladogram.add_trace(go.Scatter(
        x=clade_x_lines,
        y=clade_y_lines,
        mode="lines",
        line=dict(color="#94a3b8", width=1.2),
        hoverinfo="none",
        showlegend=False,
    ))

    # 2. Terminal taxa (language leaves)
    doc_colors = ["#059669" if l["is_documented"] else "#ea580c" for l in clade_leaf_data]
    doc_status_labels = [
        "Documented in Grambank" if l["is_documented"] else "Undocumented (0 features)" 
        for l in clade_leaf_data
    ]

    fig_cladogram.add_trace(go.Scatter(
        x=[l["x"] for l in clade_leaf_data],
        y=[l["y"] for l in clade_leaf_data],
        mode="markers+text" if len(clade_leaf_data) <= 80 else "markers",
        marker=dict(size=5, color=doc_colors),
        text=[f"  {l['name']}" for l in clade_leaf_data],
        textposition="middle right",
        textfont=dict(size=9, color="#1e293b"),
        customdata=[[l["name"], l["code"], status] for l, status in zip(clade_leaf_data, doc_status_labels)],
        hovertemplate="<b>%{customdata[0]}</b><br>Glottocode: %{customdata[1]}<br>Status: %{customdata[2]}<extra></extra>",
        showlegend=False,
    ))

    n_taxa = len(clade_leaf_data)
    fig_cladogram.update_layout(
        title=f"Phylogenetic Cladogram ({n_taxa} taxa) — Green = Documented | Orange = Undocumented",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="#ffffff",
        height=max(450, min(2000, n_taxa * 15)),
        margin=dict(l=20, r=180, t=50, b=20),
    )

    mo.vstack([
        mo.md("### Austronesian Phylogenetic Cladogram"),
        clade_selector,
        mo.ui.plotly(fig_cladogram),
    ])
    return


@app.cell
def _(
    df_aust_languages,
    df_lang_stats,
    id_col,
    lat_col,
    lon_col,
    name_col,
    pl,
    target_total_features,
):
    # Merge coordinates with completeness metrics
    df_aust_geo_merged = (
        df_aust_languages.lazy()
        .select([
            pl.col(id_col).alias("glottocode"),
            pl.col(name_col).alias("language_name"),
            pl.col(lat_col).cast(pl.Float64, strict=False).alias("latitude"),
            pl.col(lon_col).cast(pl.Float64, strict=False).alias("longitude"),
        ])
        .filter(pl.col("latitude").is_not_null() & pl.col("longitude").is_not_null())
        .join(df_lang_stats.lazy(), on="glottocode", how="left")
        .with_columns([
            pl.col("features_answered").is_not_null().alias("is_in_grambank"),
            pl.col("features_answered").fill_null(0),
            pl.col("features_unknown").fill_null(0),
            pl.col("pct_answered").fill_null(0.0),
            pl.when(pl.col("features_answered").is_null())
            .then(pl.lit("Undocumented (0 features)"))
            .when(pl.col("features_answered") == target_total_features)
            .then(pl.lit("100% Complete (195)"))
            .when(pl.col("pct_answered") >= 90)
            .then(pl.lit("90% - 99%"))
            .when(pl.col("pct_answered") >= 80)
            .then(pl.lit("80% - 89%"))
            .when(pl.col("pct_answered") >= 60)
            .then(pl.lit("60% - 79%"))
            .when(pl.col("pct_answered") >= 40)
            .then(pl.lit("40% - 59%"))
            .otherwise(pl.lit("< 40%"))
            .alias("completeness_bracket"),
        ])
        .collect()
    )

    return (df_aust_geo_merged,)


@app.cell
def _(alt, df_aust_coded_values, mo, pl, target_total_features):
    # Aggregate per language: how many of the 195 features are coded 0 or 1
    df_lang_stats = (
        df_aust_coded_values.lazy()
        .group_by("glottocode")
        .agg([
            pl.col("raw_value").filter(pl.col("raw_value").is_in(["0", "1"])).count().alias("features_answered"),
            pl.col("raw_value").filter(pl.col("raw_value") == "?").count().alias("features_unknown"),
        ])
        .with_columns([
            ((pl.col("features_answered") / target_total_features) * 100).alias("pct_answered"),
            (target_total_features - pl.col("features_answered") - pl.col("features_unknown")).alias("features_missing"),
        ])
        .collect()
    )

    # Bin into percentage tiers
    bracket_order = ["100% Complete (195)", "90% - 99%", "80% - 89%", "60% - 79%", "40% - 59%", "< 40%"]

    df_completeness_chart_data = (
        df_lang_stats.lazy()
        .with_columns(
            pl.when(pl.col("features_answered") == target_total_features).then(pl.lit("100% Complete (195)"))
            .when(pl.col("pct_answered") >= 90).then(pl.lit("90% - 99%"))
            .when(pl.col("pct_answered") >= 80).then(pl.lit("80% - 89%"))
            .when(pl.col("pct_answered") >= 60).then(pl.lit("60% - 79%"))
            .when(pl.col("pct_answered") >= 40).then(pl.lit("40% - 59%"))
            .otherwise(pl.lit("< 40%"))
            .alias("completeness_bracket")
        )
        .group_by("completeness_bracket")
        .agg(pl.len().alias("language_count"))
        .with_columns(
            ((pl.col("language_count") / df_lang_stats.height) * 100).round(1).alias("pct_of_sample")
        )
        .collect()
    )

    # Altair horizontal bar chart
    completeness_bar_chart = (
        alt.Chart(df_completeness_chart_data)
        .mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4, size=24)
        .encode(
            y=alt.Y("completeness_bracket:N", sort=bracket_order, title="Features Documented"),
            x=alt.X("language_count:Q", title="Number of Languages"),
            color=alt.Color("language_count:Q", scale=alt.Scale(scheme="blues"), legend=None),
            tooltip=[
                alt.Tooltip("completeness_bracket:N", title="Completeness"),
                alt.Tooltip("language_count:Q", title="Languages"),
                alt.Tooltip("pct_of_sample:Q", title="% of Austronesian Sample"),
            ]
        )
        .properties(
            width=580,
            height=240,
            title=f"Austronesian Languages by Grambank Feature Completeness (Total: {df_lang_stats.height})"
        )
    )

    mo.vstack([
        mo.md("### Feature Completeness Distribution"),
        completeness_bar_chart,
    ])
    return (df_lang_stats,)


@app.cell
def _(mo):

    # Embed the Glottolog page inside an iframe
    mo.Html(
        """
        <iframe 
            src="https://glottolog.org/resource/languoid/id/aust1307" 
            width="100%" 
            height="700px" 
            style="border: 1px solid #ccc; border-radius: 8px;">
        </iframe>
        """
    )
    return


@app.cell
def _(df_aust_geo_merged, html, json, mo):


    # Ensure palette is available
    tier_color_palette = {
        "100% Complete (195)": "#1e3a8a",
        "90% - 99%":           "#2563eb",
        "80% - 89%":           "#0d9488",
        "60% - 79%":           "#d97706",
        "40% - 59%":           "#ea580c",
        "< 40%":               "#dc2626",
        "Undocumented (0 features)": "#94a3b8",
    }

    # Prepare JSON data payload
    zoom_map_data = [
        {
            "name": row["language_name"],
            "code": row["glottocode"],
            "lat": row["latitude"],
            "lon": row["longitude"],
            "tier": row["completeness_bracket"],
            "color": tier_color_palette.get(row["completeness_bracket"], "#94a3b8"),
            "ans": row["features_answered"],
            "pct": round(row["pct_answered"], 1),
            "unk": row["features_unknown"],
            "is_doc": row["is_in_grambank"],
        }
        for row in df_aust_geo_merged.to_dicts()
    ]

    leaflet_zoom_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8" />
      <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
      <link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css" />
      <link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.Default.css" />
  
      <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
      <script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>

      <style>
        body, html, #map {{ height: 100%; margin: 0; padding: 0; background: #e2e8f0; font-family: sans-serif; }}
        .custom-tooltip {{
          background: rgba(15, 23, 42, 0.92); color: #ffffff; font-size: 12px; font-weight: 500;
          padding: 4px 8px; border-radius: 4px; border: none; box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        }}
        .legend {{
          background: white; padding: 10px 14px; font-size: 11px; line-height: 19px;
          border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }}
        .legend i {{ width: 10px; height: 10px; border-radius: 50%; float: left; margin-right: 8px; margin-top: 4px; }}
      </style>
    </head>
    <body>
      <div id="map"></div>
      <script>
        // 1. Initialize zoomable slippy map centered on Island SE Asia / Pacific
        const map = L.map('map', {{
          center: [-2, 140],
          zoom: 3,
          minZoom: 2,
          maxZoom: 14,
        }});

        // 2. Esri Light Gray Canvas basemap (free, unauthenticated, allows iframes, no watermark)
        L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
          attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
          maxZoom: 16
        }}).addTo(map);

        // 3. MarkerCluster with Spiderfy for overlapping languages
        const markers = L.markerClusterGroup({{
          maxClusterRadius: 28,          // Small cluster radius so points separate early
          spiderfyOnMaxZoom: true,       // Overlapping dots fan out in a circle when clicked
          showCoverageOnHover: false,
          disableClusteringAtZoom: 7     // Beyond zoom level 7, show every individual language
        }});

        const data = {json.dumps(zoom_map_data)};
        const colorLegend = {json.dumps(tier_color_palette)};
        const tierCounts = {{}};
        Object.keys(colorLegend).forEach(k => tierCounts[k] = 0);

        data.forEach(p => {{
          tierCounts[p.tier] = (tierCounts[p.tier] || 0) + 1;
          const isUndoc = !p.is_doc;

          const marker = L.circleMarker([p.lat, p.lon], {{
            radius: isUndoc ? 4 : 5.5,
            fillColor: p.color,
            color: isUndoc ? '#64748b' : '#0f172a',
            weight: 0.8,
            opacity: 0.9,
            fillOpacity: isUndoc ? 0.45 : 0.85
          }});

          // Instant floating label on hover
          marker.bindTooltip(`<b>${{p.name}}</b> (${{p.code}})`, {{
            className: 'custom-tooltip',
            direction: 'top',
            offset: [0, -6]
          }});

          // Persistent card on click
          marker.bindPopup(`
            <div style="font-size: 13px; line-height: 1.5; min-width: 180px;">
              <h4 style="margin: 0 0 4px 0; color: #0f172a;">${{p.name}}</h4>
              <span style="color: #64748b; font-size: 11px;">Glottocode: <code>${{p.code}}</code></span><br>
              <hr style="margin: 6px 0; border: none; border-top: 1px solid #e2e8f0;">
              Status: <b>${{p.tier}}</b><br>
              ${{p.is_doc 
                ? `Features Answered: <b>${{p.ans}} / 195</b> (${{p.pct}}%)<br>Unknown (?): <b>${{p.unk}}</b>`
                : '<span style="color: #ea580c; font-weight: 600;">0 features documented</span>'
              }}
            </div>
          `);

          markers.addLayer(marker);
        }});

        map.addLayer(markers);

        // 4. Legend
        const legend = L.control({{ position: 'bottomright' }});
        legend.onAdd = function() {{
          const div = L.DomUtil.create('div', 'legend');
          div.innerHTML = '<b>Feature Completeness</b><br>';
          Object.keys(colorLegend).forEach(tier => {{
            const count = tierCounts[tier] || 0;
            div.innerHTML += `<i style="background: ${{colorLegend[tier]}}"></i> ${{tier}} (${{count}})<br>`;
          }});
          return div;
        }};
        legend.addTo(map);
      </script>
    </body>
    </html>
    """

    zoom_map_view = mo.Html(
        f'<iframe srcdoc="{html.escape(leaflet_zoom_html)}" style="width: 100%; height: 580px; border: 1px solid #cbd5e1; border-radius: 8px;"></iframe>'
    )

    mo.vstack([
        mo.md("### Zoomable Austronesian Map (Scroll to Zoom, Drag to Pan)"),
        mo.md("*Tip: Hover over any point to read its name. In dense islands, clicking a cluster fans out the languages so individual varieties can be targeted.*"),
        zoom_map_view,
    ])
    return


@app.cell
def _():
    return


@app.cell
def _(
    df_glottolog_raw,
    gb_aust_codes,
    id_col,
    mo,
    name_col,
    parent_to_children,
    pl,
):
    # Build a nested JSON structure starting from root_family
    def get_taxonomy_node(node_id: str, max_depth: int = 3, current_depth: int = 0) -> dict:
        # Look up name from Glottolog DataFrame
        name_match = df_glottolog_raw.filter(pl.col(id_col) == node_id).select(name_col)
        node_name = name_match.item(0, 0) if name_match.height > 0 else node_id
    
        node = {
            "name": f"{node_name} ({node_id})",
            "is_documented": node_id in gb_aust_codes,
        }
    
        if current_depth < max_depth:
            children = parent_to_children.get(node_id, [])
            if children:
                node["children"] = [
                    get_taxonomy_node(child_id, max_depth, current_depth + 1)
                    for child_id in children
                ]
        return node

    tax_depth_slider = mo.ui.slider(start=1, stop=4, value=2, label="Taxonomy Expansion Depth:")

    return


@app.cell
def _():
    gb_values_url_input = "https://raw.githubusercontent.com/grambank/grambank/refs/heads/master/cldf/values.csv"

    gb_params_url_input = "https://raw.githubusercontent.com/grambank/grambank/refs/heads/master/cldf/parameters.csv"

    return gb_params_url_input, gb_values_url_input


@app.cell
def _(
    df_glottolog_raw,
    gb_aust_codes,
    gb_params_url_input,
    gb_values_url_input,
    id_col,
    load_source_csv,
    name_col,
    pl,
):
    # Load parameters to determine the total feature benchmark (195 features)
    df_gb_params = load_source_csv(gb_params_url_input).select([
        pl.col("ID").alias("parameter_id"),
        pl.col("Name").alias("feature_name"),
        pl.col("Description").alias("feature_desc"),
    ])
    target_total_features = df_gb_params.height  # 195

    # Filter values to Austronesian varieties
    df_gb_values_raw = load_source_csv(gb_values_url_input)

    df_aust_coded_values = (
        df_gb_values_raw.lazy()
        .filter(pl.col("Language_ID").is_in(gb_aust_codes))
        .select([
            pl.col("Language_ID").alias("glottocode"),
            pl.col("Parameter_ID").alias("parameter_id"),
            pl.col("Value").alias("raw_value"),
        ])
        .collect()
    )

    # Tally per language: answered (0 or 1), unknown (?), and missing
    df_language_completeness_scores = (
        df_aust_coded_values.lazy()
        .group_by("glottocode")
        .agg([
            pl.col("raw_value").filter(pl.col("raw_value").is_in(["0", "1"])).count().alias("answered_features"),
            pl.col("raw_value").filter(pl.col("raw_value") == "?").count().alias("unknown_features"),
        ])
        .with_columns([
            (target_total_features - pl.col("answered_features") - pl.col("unknown_features")).alias("missing_features"),
            ((pl.col("answered_features") / target_total_features) * 100).alias("pct_answered"),
        ])
        .join(
            df_glottolog_raw.select([pl.col(id_col).alias("glottocode"), pl.col(name_col).alias("language_name")]).lazy(),
            on="glottocode",
            how="left"
        )
        .collect()
    )

    # Categorize each language into an answered percentage bracket
    df_binned_language_counts = (
        df_language_completeness_scores.lazy()
        .with_columns(
            pl.when(pl.col("pct_answered") == 100).then(pl.lit("100% Complete (195)"))
            .when(pl.col("pct_answered") >= 90).then(pl.lit("90% - 99%"))
            .when(pl.col("pct_answered") >= 80).then(pl.lit("80% - 89%"))
            .when(pl.col("pct_answered") >= 60).then(pl.lit("60% - 79%"))
            .when(pl.col("pct_answered") >= 40).then(pl.lit("40% - 59%"))
            .otherwise(pl.lit("< 40%"))
            .alias("bracket")
        )
        .group_by("bracket")
        .agg(pl.len().alias("num_languages"))
        .with_columns(
            pl.when(pl.col("bracket") == "100% Complete (195)").then(6)
            .when(pl.col("bracket") == "90% - 99%").then(5)
            .when(pl.col("bracket") == "80% - 89%").then(4)
            .when(pl.col("bracket") == "60% - 79%").then(3)
            .when(pl.col("bracket") == "40% - 59%").then(2)
            .otherwise(1)
            .alias("sort_order")
        )
        .sort("sort_order", descending=True)
        .collect()
    )

    return df_aust_coded_values, df_gb_params, target_total_features


@app.cell
def _():
    return


@app.cell
def _(df_aust_coded_values, df_gb_params, mo, pl):
    # Interactive slider to pick Top N features
    n_features_slider = mo.ui.slider(start=3, stop=10, value=5, label="Top N Features:")

    # 1. Aggregate feature tallies across Austronesian
    df_feature_tallies = (
        df_aust_coded_values.lazy()
        .group_by("parameter_id")
        .agg([
            pl.col("raw_value").filter(pl.col("raw_value") == "1").count().alias("n_present"),
            pl.col("raw_value").filter(pl.col("raw_value") == "0").count().alias("n_absent"),
            pl.col("raw_value").filter(pl.col("raw_value") == "?").count().alias("n_unknown"),
        ])
        .with_columns([
            (pl.col("n_present") + pl.col("n_absent")).alias("n_coded_known"),
        ])
        .filter(pl.col("n_coded_known") >= 50)  # Filter for statistical significance
        .with_columns([
            ((pl.col("n_present") / pl.col("n_coded_known")) * 100).round(1).alias("pct_present"),
            ((pl.col("n_absent") / pl.col("n_coded_known")) * 100).round(1).alias("pct_absent"),
        ])
        .join(df_gb_params.lazy(), on="parameter_id", how="left")
        .collect()
    )

    return df_feature_tallies, n_features_slider


@app.cell
def _(alt, df_feature_tallies, n_features_slider, pl):

    # 2. Extract Top N Absent (negative scores) and Top N Present (positive scores)
    n_top = n_features_slider.value

    df_top_absent_diverging = (
        df_feature_tallies.sort("pct_absent", descending=True)
        .head(n_top)
        .with_columns([
            (-pl.col("pct_absent") / 100.0).alias("bias_score"),
            pl.lit("Uniformly Absent (0)").alias("category"),
        ])
    )

    df_top_present_diverging = (
        df_feature_tallies.sort("pct_present", descending=True)
        .head(n_top)
        .with_columns([
            (pl.col("pct_present") / 100.0).alias("bias_score"),
            pl.lit("Universally Present (1)").alias("category"),
        ])
    )

    # Combine using the full, untruncated feature text
    df_diverging_chart_data = (
        pl.concat([df_top_absent_diverging, df_top_present_diverging])
        .with_columns([
            (pl.col("parameter_id") + ": " + pl.col("feature_name")).alias("feature_label")
        ])
        .sort("bias_score", descending=False)
    )

    # 3. Build Diverging Bar Chart in Altair
    zero_line = alt.Chart(pl.DataFrame({"x": [0]})).mark_rule(color="#1e293b", strokeWidth=1.2).encode(x="x:Q")

    bars = (
        alt.Chart(df_diverging_chart_data)
        .mark_bar(stroke="#1e293b", strokeWidth=1.1, height=18)
        .encode(
            y=alt.Y(
                "feature_label:N",
                sort=alt.EncodingSortField(field="bias_score", order="ascending"),
                title=None,
                axis=alt.Axis(
                    labelFontSize=11,
                    labelColor="#1e293b",
                    labelLimit=0,  # Disables Vega-Lite pixel truncation completely
                    labelPadding=10,
                )
            ),
            x=alt.X(
                "bias_score:Q",
                title="Typological Bias Score (% Absent ← 0 → % Present)",
                scale=alt.Scale(domain=[-1.05, 1.05]),
                axis=alt.Axis(
                    values=[-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
                    grid=True,
                    gridColor="#e2e8f0"
                )
            ),
            color=alt.Color(
                "bias_score:Q",
                scale=alt.Scale(
                    domain=[-1.0, 0.0, 1.0],
                    range=["#4b6f96", "#f1f5f9", "#b9534f"]
                ),
                legend=None
            ),
            tooltip=[
                alt.Tooltip("parameter_id:N", title="Parameter ID"),
                alt.Tooltip("feature_name:N", title="Feature"),
                alt.Tooltip("category:N", title="Status"),
                alt.Tooltip("pct_present:Q", title="% Present (1)"),
                alt.Tooltip("pct_absent:Q", title="% Absent (0)"),
                alt.Tooltip("n_coded_known:Q", title="Languages Coded"),
                alt.Tooltip("feature_desc:N", title="Description"),
            ]
        )
    )

    return bars, n_top, zero_line


@app.cell
def _(bars, mo, n_features_slider, n_top, zero_line):

    diverging_feature_chart = (
        (bars + zero_line)
        .properties(
            width=520,
            height=max(220, n_top * 42),
            title=f"Top {n_top} Biased Austronesian Features (Family Typological Profile)"
        )
        .configure_view(stroke="#cbd5e1", strokeWidth=1)
    )

    mo.vstack([
        n_features_slider,
        diverging_feature_chart,
    ])
    return


@app.cell
def _(mo):
    apa_markdown = """
    ### Databases & Datasets
    * **Glottolog:**  
      Hammarström, H., Forkel, R., Haspelmath, M., & Bank, S. (2024). *Glottolog 5.0* (Version 5.0) [Data set]. Max Planck Institute for Evolutionary Anthropology. https://doi.org/10.5281/zenodo.10804357 [INDEX]
    * **Grambank:**  
      Skirgård, H., Haynie, H. J., Blasi, D. E., Hammarström, H., Collins, J., Lueders, J., Adams, T., Alfaro, B. N., Andreadis, N., Armoskaite, C., Baggaley, R. B., Bakulin, V., Bento, P., Berger, C. R., Bishop, P., Blaise, J., Blum, F., Bone, D., Bowern, C., … Greenhill, S. J. (2023). Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. *Science Advances*, 9(16), eadg6175. https://doi.org/10.1126/sciadv.adg6175 [INDEX]

    ### Academic Literature & Web Sources
    * **Journal Article (DOI: 10.1353/LAN.2017.0007):**  
      Keenan, E. L., & Chung, S. (2017). The Austronesian languages by Robert Blust (review). *Language*, 93(1), 220–239. https://doi.org/10.1353/lan.2017.0007 [INDEX]
    * **Website (Encyclopaedia Britannica):**  
      Encyclopaedia Britannica. (n.d.). *Austronesian languages*. Retrieved from https://www.britannica.com/topic/Austronesian-languages
    """

    bibtex_code = """```bibtex
    @article{skirgard2023grambank,
      title     = {Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss},
      author    = {Skirg{\\aa}rd, Hedvig and Haynie, Hannah J. and Blasi, Dami{\\'a}n E. and Hammarstr{\\"o}m, Harald and Collins, Jeremy and Lueders, Jay and Greenhill, Simon J. and others},
      journal   = {Science Advances},
      volume    = {9},
      number    = {16},
      pages     = {eadg6175},
      year      = {2023},
      publisher = {American Association for the Advancement of Science},
      doi       = {10.1126/sciadv.adg6175}
    }

    @misc{hammarstrom2024glottolog,
      author    = {Hammarstr{\\"o}m, Harald and Forkel, Robert and Haspelmath, Martin and Bank, Sebastian},
      title     = {Glottolog 5.0},
      year      = {2024},
      publisher = {Max Planck Institute for Evolutionary Anthropology},
      address   = {Leipzig},
      doi       = {10.5281/zenodo.10804357},
      url       = {https://glottolog.org}
    }

    @article{keenan2017austronesian,
      author    = {Keenan, Edward L. and Chung, Sandra},
      title     = {The Austronesian languages by Robert Blust (review)},
      journal   = {Language},
      volume    = {93},
      number    = {1},
      pages     = {220--239},
      year      = {2017},
      publisher = {Linguistic Society of America},
      doi       = {10.1353/lan.2017.0007}
    }

    @misc{britannica_austronesian,
      author       = {{Encyclopaedia Britannica}},
      title        = {Austronesian languages},
      howpublished = {\\url{https://www.britannica.com/topic/Austronesian-languages}},
      note         = {Online Reference}
    }
    ```"""

    references_tab = mo.ui.tabs({
        "APA (7th Edition)": mo.md(apa_markdown),
        "BibTeX Entries": mo.md(bibtex_code),
    })

    mo.vstack([
        mo.md("## References"),
        references_tab,
    ])
    return


if __name__ == "__main__":
    app.run()
