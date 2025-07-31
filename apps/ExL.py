import marimo

__generated_with = "0.14.13"
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
def _(file_upload, mo, set_matches, yaml):

    # Final cell for processing and display
    if file_upload.value:
        try:
            filename = file_upload.name()
            content = file_upload.contents()
            data = yaml.safe_load(content)

            if not isinstance(data, dict) or "matches" not in data:
                status_message = mo.md(
                    f"❌ **Invalid Format.** File `{filename}` is missing the 'matches' key."
                )
            else:
                value_from_yaml = data["matches"]

                # Use the setter function to update the state's value
                set_matches(value_from_yaml)

                status_message = mo.md(
                    f"✅ **Success!** Loaded {len(value_from_yaml)} match(es) from `{filename}`"
                )

        except Exception as e:
            status_message = mo.md(f"❌ **An unexpected error occurred:** `{e}`")
    else:
        status_message = mo.md("📂 **Upload an Espanso YAML file to begin.**")


    return (status_message,)


@app.cell
def _(file_upload, mo, status_message):
    mo.vstack([
        file_upload,
        status_message
    ])
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
def _():
                # "actions": mo.hstack([mo.ui.button(
                #     label="Edit",
                #     value=i,  # Assign the row index to the button's value
                #     on_click=handle_edit_and_remove,  # Pass the handler directly
                # ), mo.ui.button(
                #     label="Delete",
                #     value=i,  # Assign the row index to the button's value
                #     on_click=handle_delete,  # Pass the handler directly
                #     kind="danger",
                # )], justify="start", gap=1),
    return


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
