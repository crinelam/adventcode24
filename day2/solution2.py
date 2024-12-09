import numpy as np

def checkReport(report):
    decreasing = all(i > j for i, j in zip(report, report[1:]))
    if not decreasing:
        increasing = all(i < j for i, j in zip(report, report[1:]))
        if not increasing:
            return False # Not Decreasing or Increasing
    differences = np.diff(report)
    for diff in differences:
        if abs(diff) < 1 or abs(diff) > 3:
            return False # Difference between numbers incorrect
    return True

reports = []

with open("input") as file:
    for line in file:
        #print(line.rstrip())
        lineNums = line.rsplit()
        reports.append([int(num) for num in lineNums])

safeReports = 0

for report in reports:
    reportResult = checkReport(report)
    if not reportResult:
        for i in range(len(report)):
            newReport = report.copy()
            newReport.pop(i)
            if checkReport(newReport):
                safeReports += 1
                break
    else:
        safeReports += int(reportResult)

print(safeReports)