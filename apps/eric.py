import marimo

__generated_with = "0.14.16"
app = marimo.App(width="full")


@app.cell
def _():
    import dataclasses
    import io
    import requests
    import urllib.parse
    from typing import List, Dict, Union, TypedDict

    import marimo as mo
    import polars as pl

    # A type hint for the error dictionary structure
    ErrorDict = TypedDict("ErrorDict", {"error": str})

    # A structured representation of a search result
    @dataclasses.dataclass
    class EricDocument:
        title: str
        description: str
        id: str
        url: str
        e_fulltextauth: bool
        publication_date: str = "N-A"
        authors: List[str] = dataclasses.field(default_factory=list)

        @classmethod
        def from_dict(cls, data: Dict) -> "EricDocument":
            """Factory method to create an instance from an API dictionary."""
            return cls(
                title=data.get("title", "N/A"),
                authors=data.get("author", []),
                description=data.get("description", "N/A"),
                publication_date=data.get("publicationdateyear", "N/A"),
                url=data.get("url", "N/A"),
                id=data.get("id", "N/A"),
                e_fulltextauth=data.get("e_fulltextauth") == "1",
            )

    # --- All Function Definitions ---

    def fetch_eric_data(
        query: str, num_rows: str
    ) -> Union[List[EricDocument], ErrorDict]:
        """Fetches and parses search results from the ERIC API."""
        if not query:
            return {"error": "Search query cannot be empty."}

        base_url = "https://api.ies.ed.gov/eric/"
        fields_to_request = "id,title,author,description,publicationdateyear,url,e_fulltextauth"
        api_params = {
            "search": query,
            "format": "json",
            "rows": num_rows,
            "fields": fields_to_request,
        }

        try:
            response = requests.get(base_url, params=api_params, timeout=15)
            response.raise_for_status()
            raw_data = response.json()
            docs = raw_data.get("response", {}).get("docs", [])
            return [EricDocument.from_dict(doc) for doc in docs]
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            return {"error": f"HTTP Error: Server returned status code {status_code}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Network connection error: {e}"}
        except ValueError:
            return {"error": "Failed to decode the JSON response from the server."}


    def format_documents_for_table(docs: List[EricDocument]) -> List[Dict]:
        """Transforms EricDocument objects into a list of dicts for mo.ui.table."""
        formatted_docs = []
        for doc in docs:
            if doc.url == "N/A":
                url = f"https://files.eric.ed.gov/fulltext/{doc.id}.pdf"
            elif doc.url != "N/A":
                url = doc.url
            else:
                url = None

            formatted_docs.append({
                "Title": doc.title,
                "Authors": "\n".join(doc.authors) if doc.authors else "N/A",
                "Abstract": doc.description,
                "Date": doc.publication_date,
                "URL": f"{url}" if url else "N/A",
    #            "ID": doc.id,
            })
        return formatted_docs
    return (
        EricDocument,
        ErrorDict,
        List,
        Union,
        fetch_eric_data,
        format_documents_for_table,
        io,
        mo,
        pl,
    )


@app.cell
def _(fetch_eric_data, mo):
    # State for results and loading status
    results, set_results = mo.state(None)
    loading, set_loading = mo.state(False)

    # UI Elements
    search_query = mo.ui.text(label="Search Query")
    results_dropdown = mo.ui.dropdown(
        options=["20", "50", "100"], label="Number of results", value="20"
    )

    def perform_search() -> None:
        """Function to be called on button click to fetch data."""
        set_loading(True)
        try:
            query = search_query.value
            num_results = results_dropdown.value
            set_results(fetch_eric_data(query, num_results))
        finally:
            set_loading(False)

    search_button = mo.ui.button(
        label="Search", on_click=lambda _: perform_search()
    )

    # Group UI controls together
    ui_controls = mo.vstack(
        [
            search_query,
            results_dropdown,
            search_button,
        ]
    )
    return loading, results, ui_controls


@app.cell
def _(
    EricDocument,
    ErrorDict,
    List,
    Union,
    format_documents_for_table,
    loading,
    mo,
    results,
):
    def create_results_table(
        is_loading: bool, search_results: Union[List[EricDocument], ErrorDict, None]
    ):
        """Renders a status message or the results table."""
        if is_loading:
            return mo.md("--- \n*Loading...*")
        if search_results is None:
            return mo.md("Enter a query and click Search to begin.")
        if isinstance(search_results, dict) and "error" in search_results:
            return mo.ui.callout(search_results["error"], kind="danger")
        if not search_results:
            return mo.md("No results found for your query.")

        table_data = format_documents_for_table(search_results)
        return mo.ui.table(
            table_data,
            pagination=True,
            page_size=10,
            label="Search Results",
            selection="multi",
            wrapped_columns=["Title", "Abstract"],
        )

    results_table = create_results_table(loading(), results())
    return (results_table,)


@app.cell
def _(io, mo, pl, results_table):
    def create_download_component(table_output):
        """Creates a download component based on the table's selected rows."""
        if not hasattr(table_output, "value") or not table_output.value:
            return mo.ui.button(label="Download Selected as CSV", disabled=True)

        selected_rows = table_output.value
        df = pl.DataFrame(selected_rows)
    
        buffer = io.BytesIO()
        df.write_csv(buffer)
        csv_data = buffer.getvalue()

        return mo.download(
            data=csv_data,
            filename="eric_selection.csv",
            mimetype="text/csv",
            label="Download Selected as CSV",
        )

    download_control = create_download_component(results_table)
    return (download_control,)


@app.cell
def _(download_control, mo, results_table, ui_controls):
    app_layout = mo.vstack(
        [
            mo.md("# ERIC Search Engine"),
            ui_controls,
            results_table,
            download_control,
        ]
    )

    app_layout
    return


if __name__ == "__main__":
    app.run()
