import marimo

__generated_with = "0.14.16"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import dataclasses
    import requests
    import urllib.parse
    from typing import List, Dict, Union, TypedDict

    # A structured representation of a search result
    @dataclasses.dataclass
    class EricDocument:
        title: str
        description: str
        id: str
        url: str
        e_fulltextauth: bool
        publication_date: str = "N/A"
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
                # Correctly parse the boolean flag from the API's string response
                e_fulltextauth=data.get("e_fulltextauth") == "1",
            )
    # A type hint for the error dictionary structure
    ErrorDict = TypedDict("ErrorDict", {"error": str})
    return Dict, EricDocument, ErrorDict, List, Union, requests


@app.cell
def _(EricDocument, ErrorDict, List, Union, requests):
    def fetch_eric_data(
        query: str, num_rows: str
    ) -> Union[List[EricDocument], ErrorDict]:
        """Fetches and parses search results from the ERIC API."""
        if not query:
            return {"error": "Search query cannot be empty."}

        base_url = "https://api.ies.ed.gov/eric/"
        api_params = {
            "search": query,
            "format": "json",
            "rows": num_rows,
            "fields": "title,author,description,publicationdateyear,id,url,e_fulltextauth",
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

    return (fetch_eric_data,)


@app.cell
def _(fetch_eric_data, mo):
    # UI Elements
    search_query = mo.ui.text(label="Search Query")
    results_dropdown = mo.ui.dropdown(
        options=["20", "50", "100"], label="Number of results",value= "20"
    )

    # State for results and loading status
    results, set_results = mo.state(None)
    loading, set_loading = mo.state(False)

    def perform_search() -> None:
        """Fetches search results and updates the application state."""
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
    return loading, results, results_dropdown, search_button, search_query


@app.cell
def _(Dict, EricDocument, ErrorDict, List, Union, mo):
    def format_documents_for_table(docs: List[EricDocument]) -> List[Dict]:
        """Transforms EricDocument objects into a list of dicts for mo.ui.table."""
        formatted_docs = []
        for doc in docs:
            # Determine the URL and link text based on full-text availability
            if doc.url == "N/A":
                url = f"https://files.eric.ed.gov/fulltext/{doc.id}.pdf"
            elif doc.url != "N/A":
                url = doc.url
            else:
                url = None

            formatted_docs.append({
                "Title": doc.title,
                "Authors": "\n".join(doc.authors) if doc.authors else "N/A",
                "Date": doc.publication_date,
                "Abstract": doc.description,
                "URL": f"{url}" if url else "N/A",
                "id": doc.id,
            })
        return formatted_docs


    def render_results(
        is_loading: bool, search_results: Union[List[EricDocument], ErrorDict, None]
    ):
        """Renders the output based on the current application state."""
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
            wrapped_columns=["Title","Abstract", "Authors"],
            show_download= True

        )
    return (render_results,)


@app.cell
def _(
    loading,
    mo,
    render_results,
    results,
    results_dropdown,
    search_button,
    search_query,
):
    ui_controls = mo.vstack(
        [
            search_query,
            results_dropdown,
            search_button,
        ]
    )
    app_layout = mo.vstack(
        [
            mo.md("# ERIC Search Engine constructivism"),
            ui_controls,
            render_results(loading(), results()),
        ]
    )

    app_layout
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
