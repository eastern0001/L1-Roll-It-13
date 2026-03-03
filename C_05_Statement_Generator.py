
def make_statement(statement, decoration):
    """Adds emoji / additional characters to the start of the headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# Main Routine
make_statement(statement="I Love Python", decoration="🐍")
make_statement(statement="Round Results", decoration="=")