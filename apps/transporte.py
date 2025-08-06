import marimo

__generated_with = "0.14.15"
app = marimo.App(width="columns")


@app.cell(column=0)
def _():
    import marimo as mo
    from datetime import datetime, timedelta
    import polars as pl
    import random
    from great_tables import GT, style, loc, md


    return GT, datetime, loc, md, mo, pl, random, style, timedelta


@app.function
def get_month_name(month_number):
    """
    Converts a month number (1-12) to its full name.
    """
    months = [
        "Número de mes inválido", # This is for a non-existent month 0
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]

    if 1 <= month_number <= 12:
        return months[month_number]
    else:
        return months[0]


@app.cell
def _(end_week_drop, items, mid_week_drop, mo, month_selector, year_selector):




    config = mo.hstack([mo.vstack([month_selector, year_selector,mid_week_drop,end_week_drop],justify="center",gap=3)
    ,mo.vstack(items, justify='space-around', align="center")], align="start",)
    return (config,)


@app.cell
def _(datetime, mo):

    # Create UI elements for month and year selection
    month_selector = mo.ui.number(value=datetime.now().month, label="Mes")
    year_selector = mo.ui.number(value=datetime.now().year, label="Año")


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
    def get_meeting_days(year, month):
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
        meeting_days = [date for date in dates if date.weekday() in [mid_week_drop.value, end_week_drop.value]]
        return meeting_days

    # Get the list of Saturdays and Tuesdays for the selected month and year
    dates_list = get_meeting_days(year_selector.value, month_selector.value)

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

    return date_switches, items


@app.cell(column=1)
def _(mo):

    drivers_text = mo.ui.text_area(label="Raiteros",placeholder="Raiteros ...")
    drivees_text = mo.ui.text_area(label="Raiteados",placeholder="Raiteados ...")
    driv_hstack = mo.hstack([drivers_text ,drivees_text],justify="center", gap=3)
    return driv_hstack, drivees_text, drivers_text


@app.cell
def _(mo):
    note_text = mo.ui.text(label="Nota/Recordatorio")

    return (note_text,)


@app.cell
def _(note_text):
    if not note_text.value == "":
        note = "**Nota/Recordatorio:** " + note_text.value
    else:
        note =note_text.value
    return (note,)


@app.cell
def _(mo):
    mo.md(
        r"""
    <div style="background-color: #C6D8E2; color: #4D4D4D; padding: 25px; border-radius: 15px;">
      <h1>Arreglo de transporte</h1>
    </div>
    """
    )
    return


@app.cell
def _(config, mo):
    mo.md(
        f"""
    <div style="background-color: #C6D8E2; color: #4D4D4D; padding: 25px; border-radius: 15px;">
        {config}
    </div>
    """
    )
    return


@app.cell
def _(driv_hstack, mo):
    mo.md(
        f"""
    <div style="background-color: #C6D8E2; color: #4D4D4D; padding: 25px; border-radius: 15px;">
        {driv_hstack}
    </div>
    """
    )
    return


@app.cell
def _(gen_vstack, mo):
    mo.md(
        f"""
    <div style="background-color: #C6D8E2; color: #4D4D4D; padding: 25px; border-radius: 15px;">
        {gen_vstack}
    </div>
    """
    )
    return


@app.cell
def _(message):
    message
    return


@app.cell
def _(mo, png_download):
    mo.md(
        f"""
    <div style="background-color: #C6D8E2; color: #4D4D4D; padding: 25px; border-radius: 15px; text-align: center;">
        {mo.as_html(png_download)}
    </div>
    """
    )
    return


@app.cell(column=2)
def _(date_switches, drivees_text, drivers_text, pl, random):
    def handle_schedule_gen():
        """
        Generates a schedule by randomly assigning drivees to drivers for selected dates,
        ensuring all drivers are accounted for.
        """
        drivers = [d.strip() for d in drivers_text.value.split("\n") if d.strip()]
        drivees = [d.strip() for d in drivees_text.value.split("\n") if d.strip()]

        if not drivers:
            return {"drivers": []}

        selected_dates = [
            date for date, switch in date_switches.items() if not switch.value
        ]

        schedule_data = {"drivers": drivers}

        for date in selected_dates:
            # Create shuffled copies for this date's random pairing
            shuffled_drivers = drivers.copy()
            random.shuffle(shuffled_drivers)

            shuffled_drivees = drivees.copy()
            random.shuffle(shuffled_drivees)

            # Create a temporary mapping of the random assignments for this date
            temp_assignments = {
                driver: drivee for driver, drivee in zip(shuffled_drivers, shuffled_drivees)
            }

            # Build the column for this date, ensuring the order matches the
            # original `drivers` list and that every driver has a value (or a space).
            date_column = [temp_assignments.get(driver, " ") for driver in drivers]
            schedule_data[date] = date_column

        return pl.DataFrame(schedule_data)
    return (handle_schedule_gen,)


@app.cell
def _(mo, note_text):
    generate_button = mo.ui.run_button(
        label="Generar Programa",
        kind="success"
    )

    gen_vstack = mo.vstack([note_text, generate_button], align="center", gap=3)
    return gen_vstack, generate_button


@app.cell
def _(create_schedule_table, generate_button, handle_schedule_gen, mo):

    if generate_button.value:
        schedule_df = handle_schedule_gen()
        gt_table = create_schedule_table(schedule_df)
        message = gt_table
    else:
        message = mo.md("Haga clic en 'Generar Programa' para ver la tabla.")

    return gt_table, message


@app.cell
def _(GT, loc, md, note, style):
    def create_schedule_table(data_frame):
        """Creates and styles a GT table from a given DataFrame."""
        return (
            GT(data_frame, rowname_col="drivers")
            .opt_row_striping()
            .tab_header(
                title="Programa de transporte",
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
                    style.fill(color="#4a6da7"),
                    style.text(color="white"),
                ],
                locations=loc.column_labels(),
            )
            .tab_style(
                style=[
                    style.fill(color="#4a6da7"),
                    style.text(color="white", weight="bold"),
                ],
                locations=loc.stub(),
            )
            .cols_align(align="center")
            .tab_source_note(source_note=md(note))
        )
    return (create_schedule_table,)


@app.cell
def _(filename, gt_table, mo):

    # def save_polars_to_csv(df, file_path):

    #     try:
    #         df.write_csv(file_path)
    #         print(f"Polars DataFrame successfully saved to {file_path}")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")

    # # Example usage:
    # # Create a sample Polars DataFrame

    # # Specify the file path
    # output_csv = nombre + ".csv"


    # csv_download = mo.ui.button(
    #     on_click= lambda value: save_polars_to_csv(schedule_df, output_csv),
    #     label="Guardar CSV"
    # )


    png_download = mo.ui.button(
        on_click= lambda value: gt_table.save(filename),
        label="Guardar PNG"
    )


    # png_download
    return (png_download,)


@app.cell
def _(month_selector):
    filename = "Programa_transporte_mes_" + get_month_name(month_selector.value) + ".png"
    return (filename,)


if __name__ == "__main__":
    app.run()
