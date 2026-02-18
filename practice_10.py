# =========================
# A) LOAD KEYWORDS FROM A FILE
# -------------------------
# 1. Create a function called load_keywords(filename)
# 2. Open the file in read mode
# 3. Loop through each line in the file
# 4. Strip whitespace/newlines from each line
# 5. Store keywords in a list
# 6. Return the list


# =========================
# B) SCAN THE LOG FILE
# -------------------------
# 1. Create a function called scanner(filename, keywords)
# 2. Open the log file in read mode
# 3. Loop through each line and keep track of line numbers
# 4. For each keyword, check if it exists in the line
# 5. Remove the keyword from the line to clean the message
# 6. Store matches in a dictionary like:
#    results["ERROR"] = [(line_number, cleaned_text), ...]
# 7. Return the results dictionary


# =========================
# C) PRINT RESULTS WITH COLORS
# -------------------------
# 1. Define color codes for ERROR, WARNING, INFO
# 2. Loop through the results dictionary
# 3. Choose a color depending on the keyword
# 4. Print keyword, line number, and cleaned text
