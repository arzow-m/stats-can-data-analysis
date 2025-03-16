import sys
import pandas as pd

def exclude_column(column):
    # exclude column 15 from being read
    return column != 15

def main(argv):
    print("Script started")

    if len(argv) != 3:
        print("Incorrect number of arguments", file=sys.stderr)
        sys.exit(1)

    input_occupation = argv[1]
    input_year = argv[2]

    # load stats csv file into a pandas dataframe, skip col 15 due to "mixed types error"
    try:
        df = pd.read_csv("14100328.csv", encoding="utf-8-sig", usecols=exclude_column)

    except Exception as err:
        print(f"Unable to open file '14100328.csv': {err}", file=sys.stderr)
        sys.exit(1)

    print("CSV loaded successfully!")

    # get the year and month from 'REF_DATE'
    # .str[:4] is a vectorized string operation that allows you to do string manipulation
    # only slice does not require method name 
    # i.e. for upper() it would be .str.upper()

    df["Year"] = df["REF_DATE"].str[:4]
    df["Month"] = df["REF_DATE"].str[5:7]

    # filter data based on the occupation and year (full-time hours is assumed with the question)
    filtered_df = df[
        (df["National Occupational Classification"] == input_occupation) &
        (df["Year"] == input_year) &
        (df["Job vacancy characteristics"] == "Full-time") &
        (df["Statistics"] == "Average offered hourly wage") &
        (df["VALUE"].notna())  # ensure VALUE is not empty
    ]

    # filter the df to only keep relevant columns
    filtered_df = filtered_df[["Year", "Month", "National Occupational Classification", "Job vacancy characteristics", "Statistics", "VALUE"]]

    if filtered_df.empty:
        print("No data found for the given filters.")
    else:
        # save filtered data to a new csv file
        # does not include the index column to the new file 
        filtered_df.to_csv("q2_data.csv", index=False, encoding="utf-8-sig")
        print("Filtered data saved successfully to 'q2_data.csv'.")

# call main 
main(sys.argv)