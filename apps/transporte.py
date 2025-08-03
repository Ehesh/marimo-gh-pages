import marimo

__generated_with = "0.14.15"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    from datetime import datetime, timedelta
    import polars as pl
    import random


    return datetime, mo, pl, random, timedelta


@app.cell
def _(datetime, mo):

    # Create UI elements for month and year selection
    month_selector = mo.ui.number(value=datetime.now().month, label="Mes")
    year_selector = mo.ui.number(value=datetime.now().year, label="Anno")

    mo.hstack([month_selector, year_selector],justify="center", gap=5)
    return month_selector, year_selector


@app.cell
def _(mo):
    days_of_week = {
        'Lunes': 0,
        'Martes': 1,
        'Miercoles': 2,
        'Jueves': 3,
        'Viernes': 4,
        'Sabado': 5,
        'Domingo': 6
    }

    # Create the dropdown menu
    mid_week_drop = mo.ui.dropdown(
        options=days_of_week,
        label="Reunion entre semana:"
    )

    # Create the dropdown menu
    end_week_drop = mo.ui.dropdown(
        options=days_of_week,
        label="Reunion fin de semana:"
    )

    # Display the dropdown

    mo.hstack([mid_week_drop,end_week_drop],justify="center", gap=5)

    return end_week_drop, mid_week_drop


@app.cell
def _(end_week_drop, mid_week_drop):

    mid_week = mid_week_drop.value
    end_week = end_week_drop.value
    return


@app.cell
def _(
    datetime,
    end_week_drop,
    mid_week_drop,
    month_selector,
    timedelta,
    year_selector,
):
    # Function to get all Saturdays and Tuesdays for a given month and year
    def get_saturdays_and_tuesdays(year, month):
        # Start from the first day of the month
        start_date = datetime(year, month, 1)
        # Calculate the number of days in the month
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        num_days = (next_month - start_date).days

        # Generate all dates in the month
        dates = [start_date + timedelta(days=i) for i in range(num_days)]

        # Filter for Saturdays and Tuesdays
        saturdays_and_tuesdays = [date for date in dates if date.weekday() in [mid_week_drop.value, end_week_drop.value]]
        return saturdays_and_tuesdays

    # Get the list of Saturdays and Tuesdays for the selected month and year
    dates_list = get_saturdays_and_tuesdays(year_selector.value, month_selector.value)

    return (dates_list,)


@app.cell
def _(dates_list):
    dates = {
        date_obj.strftime("%Y-%m-%d")
        for date_obj in dates_list
    }

    return (dates,)


@app.cell
def _(dates, mo):

    # Create a dictionary to hold the switch components and their values
    # The key is the date, the value is the switch component
    date_switches = {
        date: mo.ui.switch(label="Omitir", value=False)
        for date in sorted(list(dates))
    }

    # Build the UI by iterating through the dictionary
    items = [
        mo.hstack([
            mo.ui.date(value=date),
            switch
        ])
        for date, switch in date_switches.items()
    ]

    # Display the UI
    mo.vstack(items, justify='space-around', align="center")

    return (date_switches,)


@app.cell
def _():
    return


@app.cell(column=1)
def _(mo):

    drivers_text = mo.ui.text_area(label="Raiteros",placeholder="Raiteros ...")
    drivees_text = mo.ui.text_area(label="Raiteados",placeholder="Raiteados ...")
    mo.hstack([drivers_text ,drivees_text],justify="center", gap=3)
    return drivees_text, drivers_text


@app.cell
def _(mo):
    note_text = mo.ui.text(label="Nota/Recordatorio")

    return (note_text,)


@app.cell
def _(note_text):
    note = "**Nota/Recordatorio:** " + note_text.value
    print(note)
    return (note,)


@app.cell(column=2)
def _(mo, note_text):
    run_button = mo.ui.run_button(label="Generar Programa",kind="success")
    mo.vstack([note_text,run_button],align="center", gap=3)

    return (run_button,)


@app.cell
def _(date_switches, drivees_text, drivers_text, pl, random, run_button):
    if run_button.value:
        drivers = drivers_text.value.split('\n')
        drivees = drivees_text.value.split('\n')

        # Reverted this line to your original logic.
        # This selects dates where the switch is OFF.
        selected_dates = [
            date for date, switch in date_switches.items() if not switch.value
        ]

        schedule_data = {}

        for date in selected_dates:
            shuffled_drivers = drivers.copy()
            random.shuffle(shuffled_drivers)

            shuffled_drivees = drivees.copy()
            random.shuffle(shuffled_drivees)

            temp_assignments = {
                driver: drivee for driver, drivee in zip(shuffled_drivers, shuffled_drivees)
            }
        
            date_column = [temp_assignments.get(driver) for driver in drivers]
            schedule_data[date] = date_column

        schedule_df = pl.DataFrame({"drivers": drivers})

        if selected_dates:
            schedule_df = schedule_df.with_columns(
                [pl.Series(date, schedule_data[date]) for date in selected_dates]
            )
    
        schedule_df
    return (schedule_df,)


@app.cell
def _(note, schedule_df):
    from great_tables import GT, style, loc, md

    gt_table = (
        GT(schedule_df, rowname_col="drivers")
        .opt_row_striping()
        .tab_header(
            title="Programa de transporte",
         #   subtitle="disponibilidad"
        )
        .tab_options(
            heading_align="left",
            column_labels_font_weight="bold",
            table_border_top_style="hidden",
            table_border_bottom_style="hidden",
            row_striping_background_color="#f5f5f5",
        )
        .tab_style(
            style=[
                style.fill(color="#356854"),
                style.text(color="white"),
            ],
            locations=loc.column_labels()
        )
        .tab_style(
            style=[
                style.fill(color="#5bb491"),
                style.text(color="white", weight="bold"),
            ],
            locations=loc.stub()
        )
        .cols_align(align="center")
        .tab_source_note(
            source_note=md(note)
        )
    )

    gt_table
    return (gt_table,)


@app.cell
def _(mo, schedule_df):
    # CSV download using polars
    csv_download = mo.download(
        data=schedule_df.write_csv().encode("utf-8"),
        filename="data.csv",
        mimetype="text/csv",
        label="Descargar CSV",
    )
    csv_download
    return


@app.cell
def _(gt_table, mo):
    import os
    import shutil
    import tempfile

    def _gt_to_png_bytes(gt_table):
        """
        Saves a great_tables GT object to a temporary PNG and returns its bytes.
        This safely handles file creation for external processes.
        """
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, "table.png")

        try:
            gt_table.save(file=file_path)
            with open(file_path, "rb") as f:
                image_bytes = f.read()
            return image_bytes
        finally:
            shutil.rmtree(temp_dir)


    # Assumes `gt_table` is your great_tables.GT object
    # By using a lambda, the expensive _gt_to_png_bytes function is only
    # called when the user clicks the download button.
    png_download = mo.download(
        data=lambda: _gt_to_png_bytes(gt_table),
        filename="Transporte.png",
        mimetype="image/png",
        label="Download as PNG",
    )
    return (png_download,)


@app.cell
def _():
    return


@app.cell
def _(png_download):
    png_download
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
