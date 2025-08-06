import marimo

__generated_with = "0.14.15"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import yaml
    return mo, yaml


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # 🧠 Espanso Snippet Builder for Linguists

    This tool allows you to create, preview, and export YAML files compatible with [Espanso](https://espanso.org/) — tailored for linguists, conlangers, and typographic wizards. 

    Features:

    - 📂 Upload existing snippet YAMLs and validate them
    - 🧪 Add new `trigger` and `replace` pairs interactively
    - 📋 View your full snippet list in a table
    - 💾 Export your final snippet list as a valid `.yaml` file

    Perfect for building IPA shortcuts, gloss abbreviations, or typographic macros!
    """
    )
    return


@app.cell
def _(mo):

    file_upload = mo.ui.file(
        kind="area",
        filetypes=[".yaml", ".yml"]
    )
    return (file_upload,)


@app.cell
def _():
    # Data for the "Zapotec example" option
    ZAPOTEC_DATA = {
        "matches": [
            {"trigger": "1a", "replace": "à", "propagate_case": True},
            {"trigger": "2a", "replace": "á", "propagate_case": True},
            {"trigger": "3a", "replace": "a̋", "propagate_case": True},
            {"trigger": "4a", "replace": "â", "propagate_case": True},
            {"trigger": "5a", "replace": "ǎ", "propagate_case": True},
            {"trigger": "1e", "replace": "è", "propagate_case": True},
            {"trigger": "2e", "replace": "é", "propagate_case": True},
            {"trigger": "3e", "replace": "̋e̋", "propagate_case": True},
            {"trigger": "4e", "replace": "̂ê", "propagate_case": True},
            {"trigger": "5e", "replace": "ě", "propagate_case": True},
            {"trigger": "1i", "replace": "ì", "propagate_case": True},
            {"trigger": "2i", "replace": "í", "propagate_case": True},
            {"trigger": "3i", "replace": "i̋", "propagate_case": True},
            {"trigger": "4i", "replace": "î", "propagate_case": True},
            {"trigger": "5i", "replace": "ǐ", "propagate_case": True},
            {"trigger": "1o", "replace": "ò", "propagate_case": True},
            {"trigger": "2o", "replace": "ó", "propagate_case": True},
            {"trigger": "3o", "replace": "ő", "propagate_case": True},
            {"trigger": "4o", "replace": "ô", "propagate_case": True},
            {"trigger": "5o", "replace": "̌ǒ", "propagate_case": True},
            {"trigger": "1u", "replace": "ù", "propagate_case": True},
            {"trigger": "2u", "replace": "ú", "propagate_case": True},
            {"trigger": "3u", "replace": "ű", "propagate_case": True},
            {"trigger": "4u", "replace": "û", "propagate_case": True},
            {"trigger": "5u", "replace": "ǔ", "propagate_case": True},
            {"trigger": "1:e", "replace": "ë̀", "propagate_case": True},
            {"trigger": "2:e", "replace": "ë́", "propagate_case": True},
            {"trigger": "3:e", "replace": "ë̋", "propagate_case": True},
            {"trigger": "4:e", "replace": "ë̂", "propagate_case": True},
            {"trigger": "5:e", "replace": "ë̌", "propagate_case": True},
            {"trigger": ":e", "replace": "ë", "propagate_case": True},
            {"trigger": "_Ch", "replace": "C̲h̲", "propagate_case": True},
            {"trigger": "_ch", "replace": "c̲h̲", "propagate_case": True},
            {"trigger": "_t", "replace": "ṯ", "propagate_case": True},
            {"trigger": "_x", "replace": "x̱", "propagate_case": True},
            {"trigger": "@1", "replace": "̀\u00A0 "},
            {"trigger": "@2", "replace": "́\u00A0 "},
            {"trigger": "@3", "replace": "̋\u00A0 "},
            {"trigger": "@4", "replace": "̌\u00A0 "},
            {"trigger": "@5", "replace": "̂\u00A0 "},
        ]
    }

    # Data for the "IPA vowel example" option
    IPA_VOWEL_DATA = {
        "matches": [
            {"trigger": ":ee", "replace": "ɛ", "label": "Open-mid front unrounded vowel"},
            {"trigger": ":c", "replace": "ɔ", "label": "Open-mid back rounded vowel"},
            {"trigger": ":0", "replace": "ø", "label": "Close-mid front rounded vowel"},
            {"trigger": ":oe", "replace": "œ", "label": "Open-mid front rounded vowel"},
            {"trigger": ":w", "replace": "ɯ", "label": "Close back unrounded vowel"},
            {"trigger": ":y", "replace": "ɤ", "label": "Close-mid back unrounded vowel"},
            {"trigger": ":v", "replace": "ʌ", "label": "Open-mid back unrounded vowel"},
            {"trigger": ":a", "replace": "ɑ", "label": "Open back unrounded vowel"},
            {"trigger": ":av", "replace": "ɒ", "label": "Open back rounded vowel"},
            {"trigger": ":ad", "replace": "ɐ", "label": "Near-open central vowel"},
            {"trigger": ":I", "replace": "ɪ", "label": "Near-close near-front unrounded vowel"},
            {"trigger": ":Y", "replace": "ʏ", "label": "Near-close near-front rounded vowel"},
            {"trigger": ":ou", "replace": "ʊ", "label": "Near-close near-back rounded vowel"},
            {"trigger": ":e-", "replace": "ə", "label": "Mid central vowel (schwa)"},
            {"trigger": ":e<", "replace": "ɘ", "label": "Close-mid central unrounded vowel"},
            {"trigger": ":-o", "replace": "ɵ", "label": "Close-mid central rounded vowel"},
            {"trigger": ":3", "replace": "ɜ", "label": "Open-mid central unrounded vowel"},
            {"trigger": ":B", "replace": "ɞ", "label": "Open-mid central rounded vowel"},
            {"trigger": ":ae", "replace": "æ", "label": "Near-open front unrounded vowel"},
            {"trigger": ":ae+", "replace": "ɶ", "label": "Open front rounded vowel"},
        ]
    }
    return IPA_VOWEL_DATA, ZAPOTEC_DATA


@app.cell
def _(IPA_VOWEL_DATA, ZAPOTEC_DATA, file_upload, mo, radio, set_matches, yaml):
    # Initialize variables to hold the results of the logic
    matches_source = None
    status_ui = None

    # Determine the source of matches based on the radio button
    if radio.value == "Zapotec example":
        matches_source = ZAPOTEC_DATA["matches"]
        status_ui = mo.vstack([mo.md(
            f"✅ **Loaded:** {len(matches_source)} built-in Zapotec matches."
        ),mo.callout(mo.md("**NOTE**: There are some issues with rendering some diachritic marks such as grave accent **`** and acute accent **´**"), kind="info")]) 

    elif radio.value == "IPA vowel example":
        matches_source = IPA_VOWEL_DATA["matches"]
        status_ui = mo.md(
            f"✅ **Loaded:** {len(matches_source)} built-in IPA vowel matches."
        )

    elif radio.value == "Custom":
        # In "Custom" mode, the UI is the file uploader and a status message
        message = "📂 **Upload an Espanso YAML file to begin.**"
        if file_upload.value:
            try:
                filename = file_upload.name()
                content = file_upload.contents()
                data = yaml.safe_load(content)

                if isinstance(data, dict) and "matches" in data:
                    matches_source = data["matches"]
                    message = f"✅ **Success!** Loaded {len(matches_source)} match(es) from `{filename}`."
                else:
                    message = f"❌ **Invalid Format.** File `{filename}` is missing the 'matches' key."
            except Exception as e:
                message = f"❌ **An unexpected error occurred:** `{e}`"

        status_ui = mo.vstack([file_upload, mo.md(message)])

    # Update the global state. Defaults to an empty list if no source was found.
    set_matches(matches_source or [])

    # You can now display the radio button and the status UI together in a final cell.
    # Example: mo.vstack([radio, status_ui])
    return (status_ui,)


@app.cell
def _(mo):
    options = ["Zapotec example", "IPA vowel example", "Custom"]
    radio = mo.ui.radio(options=options)
    return (radio,)


@app.cell
def _(mo, radio, status_ui):
    mo.vstack([radio, status_ui])
    return


@app.cell
def _(mo):
    Warning = mo.callout(mo.md("**Reminder**: changing between options resets the current workspace below meaning you may loose data if not downloaded"), kind="danger")
    Warning
    return


@app.cell
def _(mo):
    trigger_text, set_trigger_text = mo.state("")
    replace_text, set_replace_text = mo.state("")
    propagate_case, set_propagate_case = mo.state(True)
    matches, set_matches = mo.state([])

    return (
        matches,
        propagate_case,
        replace_text,
        set_matches,
        set_propagate_case,
        set_replace_text,
        set_trigger_text,
        trigger_text,
    )


@app.cell
def _(
    matches,
    propagate_case,
    replace_text,
    set_matches,
    set_propagate_case,
    set_replace_text,
    set_trigger_text,
    trigger_text,
):
    # State variables
    # Functions
    def handle_add_match():
        """
        Adds the current form values to the matches state
        and clears the input fields for the next entry.
        """
        trigger = trigger_text()
        if not trigger:
            # Avoid adding matches with an empty trigger
            return
        new_match = {
            "trigger": trigger,
            "replace": replace_text(),
            "propagate_case": propagate_case(),
        }
        set_matches([new_match] + matches())
        # Reset the form fields to their default state
        set_trigger_text("")
        set_replace_text("")
        set_propagate_case(True)

    return (handle_add_match,)


@app.cell
def _(
    matches,
    set_matches,
    set_propagate_case,
    set_replace_text,
    set_trigger_text,
):
    def handle_edit_and_remove(index_to_edit):
        """
        Loads a match back into the form for editing and removes it from the list.
        Uses .get() for safe dictionary access to prevent KeyErrors.
        """
        match_to_edit = matches()[index_to_edit]

        # Use .get() with default values matching the form's initial state
        set_trigger_text(match_to_edit.get("trigger", ""))
        set_replace_text(match_to_edit.get("replace", ""))
        set_propagate_case(match_to_edit.get("propagate_case", True))

        # Create a new list excluding the item at the given index
        new_matches = [
            match for i, match in enumerate(matches()) if i != index_to_edit
        ]
        set_matches(new_matches)

    def handle_delete(index_to_delete):
        """
        Removes a match from the list at the given index.
        """
        new_matches = [
            match for i, match in enumerate(matches()) if i != index_to_delete
        ]
        set_matches(new_matches)
    return handle_delete, handle_edit_and_remove


@app.cell
def _(handle_delete, handle_edit_and_remove, matches, mo):
    current_matches = matches()
    if current_matches:
        data_for_table = [
            {
                "trigger": match.get("trigger", ""),
                "replace": match.get("replace", ""),
                "propagate_case": match.get("propagate_case", False),
                "edit": mo.ui.button(
                    label="Edit",
                    value=i,
                    on_click=handle_edit_and_remove,
                ),
                "delete": mo.ui.button(
                    label="Delete",
                    value=i,
                    on_click=handle_delete,
                    kind="danger",
                ),
            }
            for i, match in enumerate(current_matches)
        ]
        table = mo.ui.table(
            data=data_for_table,
            pagination=False,
            label=f"Espanso Matches ({len(current_matches)})",
            selection=None,
            show_column_summaries=None,
            show_data_types=False,
            show_download=False,
        )
    else:
        table = mo.md("No matches added yet.")
    return (table,)


@app.cell
def _(
    handle_add_match,
    mo,
    propagate_case,
    replace_text,
    set_propagate_case,
    set_replace_text,
    set_trigger_text,
    trigger_text,
):

    # Form elements
    trigger_input = mo.ui.text(
        label="Trigger",
        value=trigger_text(),
        on_change=set_trigger_text,
    )
    replace_input = mo.ui.text(
        label="Replace",
        value=replace_text(),
        on_change=set_replace_text,
    )
    case_switch = mo.ui.switch(
        value=propagate_case(),
        on_change=set_propagate_case,
        label="Propagate case",
    )
    add_button = mo.ui.button(
        label="Add Match",
        on_click=lambda _: handle_add_match(),
    )
    add_match_form = mo.vstack([
        mo.md("### Add a new match"),
        trigger_input,
        replace_input,
        case_switch,
        add_button,
    ])
    return (add_match_form,)


@app.cell
def _(add_match_form):
    # Display the form
    add_match_form
    return


@app.cell
def _(table):
        # display the entries
    table
    return


@app.cell
def _(yaml):
    def create_yaml_string(matches_data):
        """
        Converts a list of match dictionaries into a YAML string,
        preserving unicode characters.
        """
        if not matches_data:
            return ""

        export_data = {"matches": matches_data}

        # allow_unicode=True ensures special characters are not escaped.
        return yaml.dump(
            export_data,
            sort_keys=False,
            indent=2,
            allow_unicode=True,
        )
    return (create_yaml_string,)


@app.cell
def _(create_yaml_string, matches, mo):
    yaml_data = create_yaml_string(matches())

    export_ui = mo.download(
        data=yaml_data.encode("utf-8"),
        filename="matches.yml",
        label="Export to YAML",
        disabled=not yaml_data, # Disable button if there are no matches
    )

    export_ui
    return


if __name__ == "__main__":
    app.run()
