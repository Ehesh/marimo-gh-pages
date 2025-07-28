import marimo

__generated_with = "0.14.12"
app = marimo.App(width="columns", auto_download=["html"])


@app.cell(column=0)
def _(mo):
    mo.md(
        """
    <div style="background-color: #F1F5F9; padding: 30px; border-radius: 20px 5px 20px;">
        <h1 style="margin-bottom: 0.32em; font-size: 2em; text-align: left;">
            <strong>COMPUTATIONAL ANALYSIS AND VISUALIZATION OF GLOBAL LEXICAL INFLUENCE: A STUDY OF METHODOLOGICAL CHALLENGES IN THE WORLD LOANWORD DATABASE</strong>
        </h1>
        <h2 style="margin-top: 0.2em; font-size: 1.5em; text-align: left;">
            <strong>By:</strong> Elhú Solano Norzagaray    </h2>
    </div>
    """
    )
    return


@app.cell
def _(m1, m2, map1_description, map1_label, map2_description, map2_label, mo):

    map1_tab = mo.vstack([
        mo.md(r"""## Map 1: Languages that shared loan words with the most other languages."""),
        m1,
        mo.hstack(
        [
            mo.md(map1_label),
            mo.md(map1_description),
        ],
        # Optional: Control justification and spacing
        justify="start",  # Distributes space evenly around items
        align="start",          # Aligns items to the top if they have different heights
        gap=3.0,                 # Adds 2 rem (roughly 32px) of space between the blocks
        widths=[1, 2]
    )
    ])


    map2_tab = mo.vstack([
        mo.md(r"""## Map 2: Languages that received loan words from the most diverse set of contributor languages."""),
        m2,
        mo.hstack(
        [
            mo.md(map2_label),
            mo.md(map2_description),
        ],
        # Optional: Control justification and spacing
        justify="start",  # Distributes space evenly around items
        align="start",          # Aligns items to the top if they have different heights
        gap=3.0,                 # Adds 2 rem (roughly 32px) of space between the blocks
        widths=[1, 2]
    )

    ])

    tabs1 = mo.ui.tabs({
        "Map 1": map1_tab,
        "Map 2": map2_tab,    
    }) 


    mo.md(
        f"""
        <div style="background-color: #FAFAFA; padding: 10px; border-radius: 20px 5px 20px;">
            {tabs1}
        </div>
        """
    )



    return


@app.cell
def _(json):
    with open(mo.notebook_location() / "public" / "Assets" / "D_loan" / "map1.geojson", "r", encoding="utf-8") as f:
        map1 = json.load(f)# import the json data to dictionaries

    with open(mo.notebook_location() / "public" / "Assets" / "D_loan" / "map2.geojson", "r", encoding="utf-8") as f:
        map2 = json.load(f)

    # icon_map1 = "./icon_map1/"
    # icon_map2 = "./icon_map2/"

    tooltip_map1 = "<strong>Name:</strong><br>{{from_language}}<br><strong>Received from:</strong><br>{{details}}"
    tooltip_map2 = "<strong>Name:</strong><br>{{from_language}}<br><strong>Gave to:</strong><br>{{details}}"


    base_url_icon_map1 = "https://raw.githubusercontent.com/Ehesh/marimo-gh-pages/main/apps/public/Assets/D_loan/icon_map1/"
    base_url_icon_map2 = "https://raw.githubusercontent.com/Ehesh/marimo-gh-pages/main/apps/public/Assets/D_loan/icon_map2/"

    icon_map1_files = [
        "Arabic.svg",
        "Arabic_English.svg",
        "Arabic_English_French.svg",
        "Arabic_English_French_Portuguese.svg",
        "Arabic_English_French_Portuguese_Spanish.svg",
        "Arabic_English_Spanish.svg",
        "Arabic_French.svg",
        "Arabic_French_Portuguese_Spanish.svg",
        "English.svg",
        "English_French.svg",
        "English_French_Portuguese.svg",
        "English_French_Portuguese_Spanish.svg",
        "English_Portuguese.svg",
        "English_Portuguese_Spanish.svg",
        "English_Spanish.svg",
        "French_Portuguese_Spanish.svg",
        "French_Spanish.svg",
        "Portuguese.svg",
        "Portuguese_Spanish.svg",
        "Spanish.svg",
    ]


    icon_map2_files = [
        'English.svg',
        'English_Indonesian.svg',
        'English_Indonesian_Japanese.svg',
        'English_Indonesian_Japanese_Romanian.svg',
        'English_Indonesian_Japanese_Romanian_SeliceRomani.svg',
        'English_Indonesian_Japanese_SeliceRomani.svg',
        'English_Indonesian_Romanian_SeliceRomani.svg',
        'English_Indonesian_SeliceRomani.svg',
        'English_Japanese.svg',
        'English_Japanese_Romanian.svg',
        'English_Japanese_Romanian_SeliceRomani.svg',
        'English_Japanese_SeliceRomani.svg',
        'English_Romanian.svg',
        'Indonesian.svg',
        'Indonesian_Japanese_Romanian_SeliceRomani.svg',
        'Indonesian_Romanian.svg',
        'Indonesian_SeliceRomani.svg',
        'Japanese.',
        'Japanese_Romanian.svg',
        'Japanese_Romanian_SeliceRomani.svg',
        'Japanese_SeliceRomani.svg',
        'Romanian.svg',
        'Romanian_SeliceRomani.svg',
        'SeliceRomani.svg',
    ]

    icon_map1_urls = [f"{base_url_icon_map1}{file}" for file in icon_map1_files]
    icon_map2_urls = [f"{base_url_icon_map2}{file}" for file in icon_map2_files]



    return (
        icon_map1_urls,
        icon_map2_urls,
        map1,
        map2,
        tooltip_map1,
        tooltip_map2,
    )


@app.cell
def _():
    import marimo as mo
    import openlayers as ol
    import json
    from collections import defaultdict

    return defaultdict, json, mo, ol


@app.cell
def _(
    create_map_from_urls,
    icon_map1_urls,
    icon_map2_urls,
    map1,
    map2,
    tooltip_map1,
    tooltip_map2,
):
    m1 = create_map_from_urls(map1, icon_map1_urls, tooltip_map1)
    m2 = create_map_from_urls(map2, icon_map2_urls, tooltip_map2)
    return m1, m2


@app.cell
def _(ol):
    dm = ol.MapWidget(ol.View(center=(0, 0), zoom=1))
    return


@app.cell
def _():

    # Markdown content for the left block
    map1_label = f"""

    | Labels | Total loans |
    |:---|---|
    | <span style="background-color: #0072B2; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> Arabic | 960|
    | <span style="background-color: #4C4C4C; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> English | 1084|
    | <span style="background-color: #E69F00; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> French | 1068|
    | <span style="background-color: #CC79A7; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> Portuguese | 173|
    | <span style="background-color: #F0E442; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> Spanish | 1871|

    """

    # Markdown content for the right block
    map1_description = f"""
    ## This map highlights the five languages that contributed loan words to the greatest number of other languages within the dataset, indicating their significant influence as sources of lexical borrowing.
    """


    # Markdown content for the left block
    map2_label = f"""
    | Labels | Total loans |
    | :------------------------------ | :---------------- |
    | <span style="background-color: #4C4C4C; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> English |         1041        |
    | <span style="background-color: #56B4E9; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> Indonesian |        995         |
    | <span style="background-color: #D55E00; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> Japanese |           840      |
    | <span style="background-color: #A7A7A7; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> Romanian |          1281       |
    | <span style="background-color: #009E73; display: inline-block; width: 15px; height: 15px; border: 1px solid #ccc; vertical-align: middle; margin-right: 5px;"></span> SeliceRomani |        1391         |


    """

    # Markdown content for the right block
    map2_description = f"""
    ## This map illustrates the five languages that have borrowed words from the most diverse range of contributor languages within the dataset, reflecting their openness to lexical influence from various linguistic origins.
    """


    return map1_description, map1_label, map2_description, map2_label


@app.cell
def _():
    return


@app.cell
def _(defaultdict, ol):


    def create_map_from_urls(geojson_data_dict, icon_urls, tooltip_template="<strong>Details</strong><br>{{details}}"):
        """
        Creates a map from GeoJSON data, a list of icon URLs, and a tooltip template.

        Args:
            geojson_data_dict (dict): The Python dictionary of your GeoJSON data.
            icon_urls (list[str]): A list of full URLs to your .svg icons.
            tooltip_template (str): An HTML/Mustache string for the tooltip format.

        Returns:
            An OpenLayers map widget or None if an error occurs.
        """
        if not icon_urls:
            print("Error: The 'icon_urls' list cannot be empty.")
            return None

        # Create a dictionary mapping the filename to its full URL
        available_icons = {url.split('/')[-1]: url for url in icon_urls}

        grouped_features = defaultdict(list)
        for feature in geojson_data_dict.get('features', []):
            properties = feature.get('properties', {})
            icon_filename = properties.get('icon_file')

            if icon_filename and icon_filename in available_icons:
                # The icon_src_url is the direct web URL from our list
                icon_src_url = available_icons[icon_filename]
                grouped_features[icon_src_url].append(feature)
            else:
                print(f"Warning: Skipping feature. Icon '{icon_filename}' not found or not specified.")

        if not grouped_features:
            print("Error: No features could be matched with the available icons.")
            return None

        vector_layers = []
        for icon_url, features_in_group in grouped_features.items():
            group_geojson = {"type": "FeatureCollection", "features": features_in_group}
            vector_source = ol.VectorSource(geojson=group_geojson)
            # ol.FlatStyle `icon_src` accepts web URLs directly
            style = ol.FlatStyle(icon_src=icon_url, icon_width=30, icon_height=30)
            vector_layer = ol.VectorLayer(source=vector_source, style=style)
            vector_layers.append(vector_layer)

        map_widget = ol.MapWidget(
            ol.View(center=(0, 0), zoom=2),
            layers=[ol.BasemapLayer(), *vector_layers]
        )

        map_widget.add_tooltip(tooltip_template)

        return map_widget
    return (create_map_from_urls,)


@app.cell(column=1)
def _(mo):
    logos = mo.hstack(
        [
            mo.vstack(
                [
                    mo.image(src="https://raw.githubusercontent.com/Ehesh/marimo-gh-pages/main/apps/public/Assets/D_loan/logos/logo-delfin.webp", width=150, height=150),
                    mo.md("[Programa Delfín](https://www.programadelfin.org.mx/)")
                ],
                align="center",
            ),
            mo.vstack(
                [
                    mo.image(src="https://raw.githubusercontent.com/Ehesh/marimo-gh-pages/main/apps/public/Assets/D_loan/logos/logo-unison.webp", width=130, height=150),
                    mo.md("[UNISON](https://www.unison.mx/)")
                ],
                align="center",
            ),
            mo.vstack(
                [
                    mo.image(src="https://raw.githubusercontent.com/Ehesh/marimo-gh-pages/main/apps/public/Assets/D_loan/logos/logo-DLL.webp", width=150, height=150),
                    mo.md("[Dept. Letras y Lingüística](https://letrasylinguistica.unison.mx/)")
                ],
                align="center",
            ),
        ],
        justify="center",
        gap=5,
    )

    mo.md(
        f"""
        <div style="background-color: #F1F5F9; padding: 10px; border-radius: 5px 20px 5px;">
            {logos}
        </div>
        """
    )


    return


@app.cell
def _(AN, General_conclusions, Methodology, Problem_statement, References, mo):

    tabs2 = mo.ui.tabs({
        "PROBLEM STATEMENT": Problem_statement,
        "METHODOLOGY": Methodology,
        "GENERAL CONCLUSIONS": General_conclusions,
        "REFERENCES": References,
        "AUTHOR'S NOTE": AN
    })


    mo.md(
        f"""
        <div style="background-color: #FAFAFA; padding: 10px; border-radius: 20px 5px 20px;">
            {tabs2}
        </div>
        """
    )
    return


@app.cell
def _():
    Problem_statement = f"""
    ## Problem statement
    The study of language contact and lexical transfer between languages is a foundational piece for understanding the social and cultural dynamics that have shaped human communication throughout history. **Loanwords**, in particular, serve as empirical and quantifiable indicators of influence between different speech communities. In the digital age, the availability of large linguistic databases has opened up new avenues for analyzing these phenomena on an unprecedented global scale.

    One of the most significant tools in this field is the **World Loanword Database** (WOLD), which compiles information on loanwords in 41 languages from diverse families. Despite its potential, using these large corpora presents inherent challenges related to the quality, consistency, methodology and curation of data collection.

    This research project emerged from the intersection of corpus linguistics, data science, and data visualization. The initial goal was to use the WOLD dataset to quantify and analyze the impact of Spanish as a donor language, seeking to identify the recipient languages that have been most influenced by its lexicon. However, during preliminary exploration, it became clear that the very structure and state of the dataset represented a research problem in itself. Therefore, the problem statement was expanded to address two interconnected questions:

    1. According to WOLD data, which languages act as the most diverse "exporters" and "importers" of loanwords globally?

    2. What methodological challenges and data integrity issues arise when using a large-scale corpus like WOLD for this type of analysis, and how can they be addressed using modern computational tools?

    """

    Methodology = f"""
    ## Methodology

    This study was developed following a computational and quantitative research approach, implemented in a modern data science environment. The methodological process was divided into the following key phases:

    DATA ACQUISITION AND PREPARATION: Version 4.1 of the World Loanword Database (WOLD) was used, obtained from its official GitHub repository to ensure access to the most up-to-date version, overcoming an initial discrepancy with the outdated version on the main website. The analysis focused on the borrowings.csv[^CSV file] and languages.csv files. Data processing and manipulation were performed in a Marimo[^Marimo] notebook using the Python library Polars[^Polars], which was selected for its efficiency in handling large datasets. An initial inspection of data quality revealed that columns such as Source_Form_ID (completely null) and Comment (sparsely populated) did not provide relevant information and were therefore excluded from the analysis.


    METHODOLOGICAL PIVOT AND REDEFINITION OF OBJECTIVE: An initial objective to analyze the chronology of loanword adoption was explored. This approach was discarded due to the qualitative and ambiguous nature of the Age column found in the dataset (with values like 'Late Old Japanese' or 'recent loan'), which added dificulties for a quantitative chronological analysis. Consequently, the research objective was redefined to identify and visualize the languages with the greatest influence as lexical "exporters" (donors) and "importers" (recipients), to the most distinct languages.


    QUANTITATIVE ANALYSIS OF LINGUISTIC INFLUENCE: To determine the main "exporting" languages, the dataset was grouped by the Source_languoid (donor language) column, and a count of unique destination languages was performed. Similarly, to identify the "importing" languages, the data was grouped by the destination language, and the number of unique Source_languoid was counted. The five languages with the highest values in each category were isolated into new dataframes for subsequent visualization.


    GEOGRAPHIC VISUALIZATION AND DATA ENRICHMENT: Creating the final geographic visualizations involved several technical steps. The py-openlayers[^py-openlayers] library was used to generate dynamic and interactive maps, highlighting the use of large language models (LLMs)[^LLM] as an aid for generating and debugging Python[^Python] code. A critical lack of latitude and longitude data was detected in WOLD's languages.csv file, which was addressed through a three step data enrichment process: first, the Glottolog[^Glottolog] database was integrated to add coordinates for 52 languages; second, estimated coordinates for the remaining 72 languages (many of them extinct) were generated using an LLM[^LLM]; and third, the complete geographic dataset was consolidated into GeoJSON[^GeoJSON] format. Finally, custom map markers were designed with matplotlib.pyplot[^Matplotlib], converted to Base64[^base64] format, and integrated as vector layers into the maps.    

    [^Python]: A high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. It is widely used in web development, data science, machine learning, and automation.
    [^CSV file]: A comma-separated values file is a simple text file format used to store tabular data, such as a spreadsheet or database. Each line of the file is a data record, and each record consists of one or more fields, separated by commas.
    [^Marimo]: A Python-based reactive notebook environment. Unlike traditional notebooks, Marimo automatically updates the output of a cell whenever its dependencies change, ensuring that the entire notebook remains consistent. This makes it particularly useful for building interactive applications and dashboards.
    [^Polars]: A high-performance DataFrame library for Rust and Python. It is designed for large-scale data processing and is known for its speed, memory efficiency, and lazy evaluation capabilities. It's often compared to pandas but is generally faster for many operations.
    [^LLM]: A type of artificial intelligence model trained on a massive amount of text data. LLMs can understand and generate human-like text, and they are the technology behind many applications, including chatbots, content creation tools, and code generators.
    [^py-openlayers]: A Python library for creating interactive maps using the OpenLayers JavaScript library. It allows users to define map layers, markers, and other features in Python and then render them in a web browser. It is useful for geospatial data visualization.
    [^Matplotlib]: A python library for creating static, animated, and interactive visualizations in Python. It provides a vast array of plotting options, from simple line plots to complex 3D graphs, and is a used a lot in the scientific computing ecosystem in Python.
    [^GeoJSON]: An open standard format for encoding geographical data structures using JSON. It represents various geographical features, such as points, lines, and polygons, and their non-spatial attributes. It's widely used for mapping and data exchange on the web.
    [^Glottolog]: An open-access online bibliographic database that catalogs the world's languages, dialects, and language families. It provides comprehensive reference information, especially for lesser-known languages, and classifies them based on expert linguistic research.
    [^base64]: A group of binary-to-text encoding schemes that represent binary data in an ASCII string format. It's commonly used to embed images or other binary data directly into text-based formats like HTML, CSS, or JSON, especially when dealing with data transfer or storage where binary data is not natively supported.

    """

    General_conclusions = f"""
    ## General conclusions
    The results obtained through the computational analysis, along with the challenges encountered during the process, allow for a set of conclusions of both a linguistic and methodological nature.

    Obtained Results:

    The quantitative analysis of the WOLD corpus made it possible to identify two main groups of languages based on their role in lexical loan transfer:

    - **Main "Exporting" Languages** (those that have contributed loans to the largest number of different languages): English, French, Portuguese, Spanish, and Arabic.

    - **Main "Importing" Languages** (those that have received loans from the largest number of diverse sources): English, Selice Romani, Indonesian, Romanian, and Japanese.


    **Conclusions and Interpretation:** [^Disclaimer]

    1. **Historical and Power Correlation:** A strong correlation is observed between the main "exporting" languages and their history as centers of colonial, political, cultural or commercial power. Their documented global lexical influence is a direct reflection of their historical expansion.

    2. **Complex Contact Patterns:** The "importing" languages reveal more diverse and multifaceted contact patterns. The case of Indonesian, for example, suggests that a high diversity of loans may be the product of a historical position as a key nexus on global trade routes. English, for its part, stands out by appearing on both lists, demonstrating its role as both a donor and recipient, integrating and disseminating loans throughout the Anglosphere.

    3. **Critique of Data Sources as the Main Finding:** Perhaps the most significant conclusion of the study is the critique of the inherent limitations of large linguistic datasets like WOLD. The research process revealed critical shortcomings, such as the absence of geographical data for most of the referenced languages, which demanded external data enrichment.

    4. **Methodological Biases in Representation:** It is postulated that WOLD's attribution methodology, which prioritizes the ultimate etymological origin of a loan, may oversimplify contact networks by obscuring intermediate transmission routes. Likewise, the notable difference in data density between the map of "importing" languages and that of "exporting" languages suggests that the current corpus underrepresents the true extent of the influence of donor languages.

    In summary, this work not only visualizes patterns of language contact but also underscores the urgent need to develop digital linguistic corpora that are more complete, diversified, methodologically transparent and structurally sound to enable more robust and reliable analyses in the future.

    [^Disclaimer]: The following conclussions are **empirical** as the main idea behind the project was to learn and exercise python coding within Marimo. 

    """

    References = f"""
    ## References
    Hammarström, H., Forkel, R., Haspelmath, M., & Bank, S. (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [https://glottolog.org](https://glottolog.org)

    Haspelmath, M., & Tadmor, U. (Eds.). (2009). *World Loanword Database*. Max Planck Institute for Evolutionary Anthropology. (Disponible en línea en [http://wold.clld.org](http://wold.clld.org), consultado el 22 de julio de 2025).
    """


    AN = f"""
    ## Author's note
    This project began with a simple curiosity about the intersection of language and data, rather than a specific research question. My initial idea was very ambitious, and I soon realized I needed to narrow my focus and find a more manageable dataset. The opportunity came during a summer ([Programa Delfín](https://www.programadelfin.org.mx/)) where Dr. Zarina Estrada, in a talk on typology and linguistic diversity, mentioned the World Loanword Database (WOLD). That resource became the starting point for my exploration. I joined forces with Erubiel Aceves for project brainstorming and splitting the workload, he focused more on the linguistic research side, while I handled data curation.

    I wanted to use this as an excuse to toy with data science tools. As a beginner in Python for data science (and Python in general, actually), it was a very fun experience. I've always con sidered myself a tinkerer of sorts-using Google Colab to clone repos and change variables here and there just to see what would happen. Google Colab is a neat environment, but a couple of months ago, I ran into Marimo. Unlike traditional notebooks, Marimo's reactive nature felt more like building a dynamic web app than writing a static script. Seeing my plots and dataframes update automatically as I tweaked the code was a game-changer, making the iterative process of discovery feel fluid and intuitive. For data manipulation, I chose Polars. Marimo’s display of dataframes is absolutely beautiful.

    Perhaps the most defining aspect of my workflow was partnering with a Large Language Model (LLM) for coding. This was less about asking for complete solutions and more like pair programming with an AI. My role shifted from understanding every line of code to clearly articulating my goals, describing the data’s structure, and then refining the AI generated code. It required careful prompting and debugging, but it dramatically accelerated my ability to implement complex ideas, especially when it came to visualization.

    The final maps were an entire chapter in themselves. My initial attempts used folium, because LLMs aren't very familiar with the py-openlayers library and I couldn’t find any examples (only the latest YouTube Short from the Marimo team). I managed to create the maps in HTML with custom pins with folium, but then I ran into Marimo examples of py-openlayers. I rewrote what I had in GeoJSON. The WOLD dataset was full of holes where geographical coordinates should have been, which led me on a "data scavenging mission" first integrating the Glottolog database and then using an LLM to generate plausible coordinates for extinct languages.

    Looking back, this project taught me that modern data analysis is a process of creative problem-solving. It’s about embracing the learning curve and leveraging new technologies like AI to bridge the gap between an idea and execution.

    ---

    During this whole process, I’ve been going through a very tough time with mental health, so I want to take a moment to give special thanks to Dr. Zarina, and to my dear friends Erubiel A. and Angela V. for their support.

    I also want to thank the **Marimo** team for such a great tool.

    Some adittional references: 

    - Marimo website: https://marimo.io/
    - Marimo yt channel: https://www.youtube.com/@marimo-team
    - OpenLayers for python examples: https://eoda-dev.github.io/py-openlayers/
    """
    return AN, General_conclusions, Methodology, Problem_statement, References


if __name__ == "__main__":
    app.run()
